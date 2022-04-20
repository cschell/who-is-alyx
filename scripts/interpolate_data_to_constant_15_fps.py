"""
This script iterates over each vr-controllers.csv file and interpolates its data to a constant 15 fps; you'll need numpy, pandas and scipy for this script to work.
"""

import pathlib

import numpy as np
import pandas as pd

from scipy.spatial.transform import Rotation
from scipy.spatial.transform import Slerp

TARGET_FPS = 15

motion_data_csvs = list(pathlib.Path("players").glob("**/vr-controllers.csv"))

for csv_path in motion_data_csvs:
    session_data = pd.read_csv(csv_path, index_col="delta_time_ms")
    session_data.index = pd.to_timedelta(session_data.index, unit="ms")

    # we drop timestamp since it would require extra steps to interpolate
    session_data = session_data.drop(columns=["timestamp"])

    # create the target index with a constant step size of `milliseconds_per_frame`
    milliseconds_per_frame = 1000 / TARGET_FPS
    original_index = session_data.index.total_seconds() * 1000
    target_index = np.arange(original_index.min(), original_index.max(), milliseconds_per_frame)

    # collect any column that doesn't belong to a rotation (rotations have to be interpolated separately)
    features = [c for c in session_data.columns if "_rot_" not in c]

    # occasionally values of one of the controllers are nan for a few frames, we interpolate them using pandas method
    session_data.loc[:, features] = session_data[features].interpolate("time")

    # and make sure we don't have any nans in the position columns anymore
    assert not any(session_data[features].isna().any())

    # prepare DataFrame for interpolated data
    interpolated_features = pd.DataFrame(columns=session_data.columns, index=pd.TimedeltaIndex(target_index, name="timestamp", unit="ms"))

    # iterate over each column and interpolate the data
    for feature_name in features:
        column = session_data[feature_name]
        interpolated_features[feature_name] = np.interp(x=target_index, xp=original_index, fp=column)

    # rotation data are a bit more tricky, since they are represented with quaternions; we use the Slerp algorithm to interpolate these
    for joint in ["hmd", "left_controller", "right_controller"]:
        joint_orientation_features = [f"{joint}_rot_{c}" for c in "xyzw"]

        # SciPy's rotation logic is not able to deal with NaNs, so we drop these rows
        orientational_features = session_data[joint_orientation_features].dropna()

        # parse rotations with scipy
        rotations = Rotation.from_quat(orientational_features)

        # and use Scipy's Slerp to interpolate the rotations
        dropped_na_original_index = orientational_features.index.total_seconds() * 1000
        slerp = Slerp(dropped_na_original_index, rotations)

        interpolated_features[joint_orientation_features] = slerp(target_index).as_quat()

    assert not any(interpolated_features.isna().any())
    interpolated_features.index = (interpolated_features.index.total_seconds() * 1000).values.round(3)

    out_path = csv_path.with_stem(csv_path.stem + ".15fps")
    print(f"interpolated {csv_path} with {TARGET_FPS} fps to {out_path}")
    interpolated_features.to_csv(out_path, index_label=session_data.index.name)

print("finished.")
