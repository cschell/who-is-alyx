# Who is Alyx? – A Virtual Reality Motion and Eye-Tracking Multi-Session Dataset

This dataset contains over 110 hours of motion, eye-tracking and physiological data from 71 players of the virtual reality game [“Half-Life: Alyx”](https://www.half-life.com/en/alyx). Each player played the game on two separate days for about 45 minutes using a HTC Vive Pro.

Features:

- **Motion data**: xyz positions and orientation of the HTC Vive headset and both controllers
- **Controller interactions**: buttons touched and pressed
- **Eye tracking data**: gaze direction, position of pupils, etc.
- **Screen recordings**: videos of what the players saw through their head mounted display
- **Demographic data**: age, sex, VR experience and body parameters
- **Physiological data**: for players 42 to 76 physiological data such as acceleration, blood volume
pulse (PPG/BVP), heart rate, inter-beat interval, skin conductance and peripheral and  skin temperature with an Empatica E4 wristband, as well as electrocardiogram data with a Polar H10 chest strap have been collected

The following table provides an overview over how many recordings there are for each device. Note, that 5 players only attended one session.

| Device                   | Sampling Rate | 1 Session | 2 Sessions |
|--------------------------|---------------|-----------|------------|
| **HTV Vive Pro (motions)**   | **combined**      | **5**         | **71**         |
|                          | ~ 15 Hz       | 4         | 37         |
|                          | 90 Hz         | 1         | 34         |
| **Eye-tracking**  |               | **8**         | **67**         |
| **Empatica E4 (wristband)**  |               | **8**         | **27**         |
| **Polar H10 (chest strap)**  |               | **3**         | **31**         |


This dataset was created for biometric data research at the [Chair for Human Computer Interaction](https://hci.uni-wuerzburg.de/) at the University of Würzburg, Germany.

## Research

This dataset has been created for academic research and is used in the following publications:

1. ["Who Is Alyx? A new Behavioral Biometric Dataset for User Identification in XR"](https://www.frontiersin.org/articles/10.3389/frvir.2023.1272234), 2023, C. Rack, T.  Fernando, M. Yalcin, A. Hotho, and M. E. Latoschik, *arXiv e-prints*
2. ["Extensible Motion-based Identification of XR Users using Non-Specific Motion Data"](https://arxiv.org/abs/2302.07517), 2023, C. Rack, K. Kobs, T. Fernando, A. Hotho, M. E. Latoschik, *arXiv e-prints*

## Setup

You can  download the latest [release from GitHub](https://github.com/cschell/who-is-alyx/releases). If you want to use git, clone this repository and use [DVC](https://dvc.org) to retrieve the CSV files: after [installing DVC](https://dvc.org/doc/install) run `dvc pull --jobs 5` from the command line.

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
- `total number of sessions`: either `1` or `2` sessions (a few players only attended once)

### Motion Data

The data have been recorded with a [Python library](https://github.com/tianshengs/SteamVR_Tracking) using [OpenVR](https://github.com/ValveSoftware/openvr) with an average framerate of 15 fps. The csv files contain the raw data recording from each session.

- `timestamp`: recording time of each frame.
- `delta_time_ms`: time passed since recording start, in milliseconds.
- `<hmd/left_controller/right_controller>_pos_<x/y/z>`: x, y or z position of the respective controller (in centimeters).
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

If you are working with tracking data, you might appreciate our ["Motion Learning Toolbox"](https://github.com/cschell/Motion-Learning-Toolbox), a Python library that provides our methods to clean and preprocess tracking data.

The data have been recorded using Steam OpenVR, so the axes represent the following directions: X: right; Y: up; Z: Forward. If you want to align the data with another dataset that has been recorded with Unity, you have to transform the system from right- to left handed by flipping the sign of all columns ending on `*_z` and `*_w`.

### Eye Tracking Data

The eye tracking data have been recorded with Unity and [SRanipal](https://forum.vive.com/topic/5642-sranipal-getting-started-steps/). The csv files contain the raw data recording from each session.

### Physiological Data

The physiological data was recorded by using two wearable sensory devices:
- Empatica E4 wristband: 
    - `Acceleration (ACC)`: 32 Hz, (x,y,z) values
    - `Electrodermal Activity (EDA)`: 4 Hz, skin conductance values in micro Siemens unit
    - `Photoplethysmography (PPG)`: 64 Hz, Blood Volume Pulse values  
    - `Heart Rate (HR)`: 0.1 Hz, beats per minute values
    - `Inter-beat interval (IBI)`: 64 Hz, time interval values between individual beats of the heart 
    - `Peripheral Body Temperature (TEMP)`: 4 Hz, temperature values in Celcius unit
- Polar H10 chest strap: 
    - `Acceleration (ACC)`: 200 Hz,  (x,y,z) values
    - `Electrocardiogram (ECG)`: 130 Hz, data values in millivolt unit


## Known Issues

There are some known issues with the dataset, please feel free to open an issue or write us if you find anything else.

### Dropping Framerate

Due to an error in the motion data recording script in the first part of our study, the framerate of the motion recordings from players 1 to 41 drops from an initial 60fps to about 10-15 fps over the course of each session. This issue was fixed starting with player 42.

As a fix, we provide a Python script to interpolate the data from each `vr-controllers.csv` to a constant 15 fps:

```bash
pip install -r requirements.txt # install required python packages (only required once for setup)
python scripts/interpolate_data_to_constant_15_fps.py # run script, may take a while
```

### Notes about Individual Sessions

- player id: 1
    - date: 2021-12-22
        - no audio in screen recording, as the voice was recorded by accident. This was fixed in post.
- player id: 10
    - date: 2022-01-17
        - eye calibration did not work
- player id: 19
    - date: 2022-01-24
        - eye motion recording failed
        - shorter record time, as the player felt motion sick
- player id: 24
    - date: 2022-02-04
     - eye motion recording failed
- player id: 32
    - date: 2022-02-15
        - eye tracking recording failed after about 29 minutes – after that, constant values were measured
- player id: 35
    - date: 2022-02-21
        - the recording was interrupted as the game crashed
- player id: 39
    - date: 2022-02-18
        - the last ~2 minutes of eyetracking data are faulty
- player id: 42
    - date: 2022-05-19
        - not started from the beginning but from the scene in the train
        - change of difficulty to "easy" mid-game
    - date: 2022-05-23
        - eye recording failed after about 15 minutes
- player id: 44
    - date: 2022-05-25
        - eye motion, voice, physiological data recording failed
    - date: 2022-07-05
        - eye motion recording failed
- player id: 45
    - date: 2022-05-25
        - eye motion recording failed after about 29 minutes
        - headset was disconnected shortly
    - date: 2022-06-08
        - empatica data recording failed after about 5 mins
- player id: 49
    - date: 2022-06-02
        - empatica recording failed after about 5 mins
- player id: 50
    - date: 2022-06-08
        - no recording physiological data
- player id: 52
    - date: 2022-06-15
     - empatica recording failed after about 2 minutes
- player id: 62
    - date: 2022-06-29
        - empatica recording failed after about 4 mins
- player id: 63
    - date: 2022-06-29
        - empatica recording failed
- player id: 64
    - date: 2022-06-22
        - polar-h10 recording failed after about 15 mins
- player id: 65
    - date: 2022-06-22
        - polar-h10 recording failed
    - date: 2022-08-03
        - polar-h10 recording failed after about 10-11 mins
- player id: 67
    - date: 2022-06-28
        - steamvr crashes after 15min, so there are two csv files for that session
        - Empatica recording failed after about 25 mins
- player id: 72
    - date: 2022-07-20
        - polar-h10 recording failed after about 20 mins
    - date: 2022-08-18
        - polar-h10 recording failed after about 44 mins
- player id: 75
    - date: 2022-08-18
        - 14:41:35 - 14:43:30 short break, briefly taken off the HMD


## Contact

We welcome any discussion, ideas and feedback around this dataset. Feel free to either open an issue on GitHub or directly contact [Christian Rack](mailto:christian.rack@uni-wuerzburg.de).

## Cite

```bibtex
@article{10.3389/frvir.2023.1272234,
	author = {Rack, Christian and Fernando, Tamara and Yalcin, Murat and Hotho, Andreas and Latoschik, Marc Erich},
    doi={10.3389/frvir.2023.1272234},
	journal = {Frontiers in Virtual Reality},
	title = {Who is Alyx? A new behavioral biometric dataset for user identification in XR},
	volume = {4},
	year = {2023}
}
```

## License

All players gave their written consent for their pseudonymized data to be published for research purposes.

<p xmlns:cc="http://creativecommons.org/ns#">
  This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://hci.uni-wuerzburg.de">Christian Rack, Fabian Sieper, Lukas Schach, Murat Yalcin, Marc E. Latoschik</a> is
  licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a>
</p>
