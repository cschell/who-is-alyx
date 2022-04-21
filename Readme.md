# Who is Alyx? – A Virtual Reality Motion and Eye-Tracking Multi-Session Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6472410.svg)](https://doi.org/10.5281/zenodo.6472410)

This dataset contains over 57 hours of motion and eye-tracking data from 37 players of the virtual reality game [“Half-Life: Alyx”](https://www.half-life.com/en/alyx). Each player played the game on two separate days for about 45 minutes using a HTC Vive Pro.

Features:

- **Motion data**: xyz positions and orientation of the head mounted display and both controllers
- **Controller interactions**: buttons touched and pressed
- **Eye tracking data**: gaze direction, position of pupils, etc.
- **Screen recordings**: videos of what the player saw through their head mounted display (coming soon)
- **Demographic data**: age, sex, VR experience and body parameters

This dataset was created for biometric data research at the [Chair for Human Computer Interaction](https://hci.uni-wuerzburg.de/) at the University of Würzburg, Germany.

## Setup

We use [DVC](https://dvc.org) to manage the data. After [installing DVC](https://dvc.org/doc/install), you can download the data after cloning this repository:

```bash
dvc pull
```

## Data

### Demographic Data

We collected several data points from each player and recorded them in [sessions_info.csv](sessions_info.csv):

- `player id`: ID of each player, for reference purposes.
- `age`: age of each player on the date of the first session.
- `height in cm`: body height in the first session (with shoes).
- `weight in kg`: weight of the player.
- `gender`
- `experience in vr`
- `already played the game`: we asked each player if they have already played the game before the first session.
- `total number of sessions`: for some players there is just 1 session, the other 37 players there is 2 sessions.

### Motion Data

The data have been recorded with a [Python library](https://github.com/tianshengs/SteamVR_Tracking) using [OpenVR](https://github.com/ValveSoftware/openvr) with an average framerate of 15 fps. The csv files contain the raw data recording from each session.

- `timestamp`: recording time of each frame.
- `delta_time_ms`: time passed since recording start, in milliseconds.
- `<hmd/left_controller/right_controller>_pos_<x/y/z>`: x, y or z position of the respective controller; the y-axis points upwards (Unity default).
- `<hmd/left_controller/right_controller>_rot_<x/y/z/w>`: quaternion of the respective controller.
- controller buttons pressed - the mapping of the controller buttons can be found in [the Unity documentation](https://docs.unity3d.com/2018.4/Documentation/Manual/OpenVRControllers.html)
    - `left_controller_grip_button`: open menu
    - `left_controller_menu_button`: activate stimpack
    - `left_controller_trackpad_<pressed/touched/x/y>`: teleporting, x & y position control the direction the user faces after releasing the trackpad
    - `left_controller_trigger`: grab/interact
    - `right_controller_grip_button`: reload
    - `right_controller_menu_button`: activate stimpack
    - `right_controller_trackpad_<pressed/touched>`: switch weapon/device held in right hand
    - `right_controller_trackpad_<x/y>`: unused
    - `right_controller_trigger`: grab/shoot/interact
    - `<left/right>_controller_ul_button_<pressed/touched>`: controller button state as received from OpenVR ([doc](https://github.com/ValveSoftware/openvr/wiki/IVRSystem::GetControllerState)); each bit represents a button; this is redundant information, since its information is already decoded to the other columns. However, we leave it for verification purposes.

### Eye Tracking Data

The eye tracking data have been recorded with Unity and [SRanipal](https://forum.vive.com/topic/5642-sranipal-getting-started-steps/). The csv files contain the raw data recording from each session.

## Known Issues

There are some known issues with the dataset, please feel free to open an issue or write us if you find anything else.

### Dropping Framerate

Due to an error in the motion data recording script, the framerate of each recording quickly drops from an initial 60fps to about 10-15 fps. We provide a Python script to interpolate the data from each `vr-controllers.csv` to a constant 15 fps:

```bash
pip install -r requirements.txt # install required python packages (only required once for setup)
python scripts/interpolate_data_to_constant_15_fps.py # run script, may take a while
```

### Notes about Individual Sessions

- subject id: 1
    - date: 2021-12-22
    - No audio in screen recording, as the voice was recorded by accident. This was fixed in post.
- subject id: 10
    - date: 2022-01-17
    - Eye calibration does not seem to have worked
- subject id: 19
    - date: 2022-01-24
    - Eye motion recording failed
        - Constant values were recorded
        - No combined data file could be created, as the eye motion recording failed
    - Shorter record time, as the subject felt motion sick
- subject id: 24
    - date: 2022-02-04
    - Eye motion recording failed
        - Constant values were recorded
        - No combined data file could be created, as the eye motion recording failed
- subject id: 32
    - date: 2022-02-15
    - Eye tracking recording failed after about 29 Minutes
        - After that time, constant values were measured
- subject id: 39
    - date: 2022-02-18
    - The last ~2 Minutes of eyetracking data are faulty
- subject id: 35
    - date: 2022-02-21
    - The recording was interrupted as the game crashed
    

## Contact

We welcome any discussion, ideas and feedback around this dataset. Feel free to either open an issue on GitHub or directly contact [Christian Schell](mailto:christian.schell@uni-wuerzburg.de).

## Cite

```bibtex
@misc{
  who_is_alyx_2022,
  title={Who Is Alyx?},
  DOI={10.5281/zenodo.6472410},
  author={Christian Schell and Fabian Sieper and Marc E. Latoschik},
  year={2022}, month={Apr}
}
```

## License

All players gave their written consent for their pseudonymized data to be published for research purposes.

<p xmlns:cc="http://creativecommons.org/ns#">
  This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.hci.uni-wuerzburg.de">Christian Schell, Fabian Sieper, Marc E. Latoschik</a> is
  licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a>
</p>
