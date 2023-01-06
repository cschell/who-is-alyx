# Who is Alyx? – A Virtual Reality Motion and Eye-Tracking Multi-Session Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6472410.svg)](https://doi.org/10.5281/zenodo.6472410)

This dataset contains over 57 hours of motion and eye-tracking data from 70 players of the virtual reality game [“Half-Life: Alyx”](https://www.half-life.com/en/alyx). Each player played the game on two separate days for about 45 minutes using a HTC Vive Pro.

Features:

- **Motion data**: xyz positions and orientation of the head mounted display and both controllers
- **Controller interactions**: buttons touched and pressed
- **Eye tracking data**: gaze direction, position of pupils, etc.
- **Screen recordings**: videos of what the player saw through their head mounted display (coming soon)
- **Demographic data**: age, sex, VR experience and body parameters

This dataset was created for biometric data research at the [Chair for Human Computer Interaction](https://hci.uni-wuerzburg.de/) at the University of Würzburg, Germany.

## Setup

You can  download the latest [release from GitHub](https://github.com/cschell/who-is-alyx/releases). If you want to use git, clone this repository and use [DVC](https://dvc.org) to retrieve the CSV files: After [installing DVC](https://dvc.org/doc/install) run `dvc pull` from the command line.

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

Due to an error in the motion data recording script, the framerate of the recordings from player 1 to 41 quickly drops from an initial 60fps to about 10-15 fps. We provide a Python script to interpolate the data from each `vr-controllers.csv` to a constant 15 fps:

```bash
pip install -r requirements.txt # install required python packages (only required once for setup)
python scripts/interpolate_data_to_constant_15_fps.py # run script, may take a while
```

### Notes about Individual Sessions

- player id: 1
    - date: 2021-12-22
    - No audio in screen recording, as the voice was recorded by accident. This was fixed in post.
- player id: 10
    - date: 2022-01-17
    - Eye calibration did not work
- player id: 19
    - date: 2022-01-24
    - Eye motion recording failed
    - Shorter record time, as the player felt motion sick
- player id: 24
    - date: 2022-02-04
    - Eye motion recording failed
- player id: 32
    - date: 2022-02-15
    - Eye tracking recording failed after about 29 Minutes – after that, constant values were measured
- player id: 39
    - date: 2022-02-18
    - The last ~2 Minutes of eyetracking data are faulty
- player id: 35
    - date: 2022-02-21
    - The recording was interrupted as the game crashed
- player id: 42
    - date: 2022-05-19
    - not started from the beginning but from the scene in the train
	- change of difficulty to "easy" mid-game
- player id: 42
    - date: 2022-05-23
    - controllers left/right switched during the game
	- eye recording failed after about 15 minutes
	- total_graph polar-h10 missing
- player id: 44
    - date: 2022-05-25
    - Eye motion, Voice, Body Data recording failed
- player id: 45
    - date: 2022-05-25
    - eye motion recording failed after about 29 minutes
	- headset was disconnected shortly
- player id: 49
    - date: 2022-06-02
    - Empathica recording failed
- player id: 50
    - date: 2022-06-08
    - No recording Body Data
- player id: 45
    - date: 2022-06-08
    - Empathica recording failed
- player id: 52
    - date: 2022-06-15
    - Empathica recording failed
- player id: 64
    - date: 2022-06-22
    - polar-h10 recording failed
- player id: 65
    - date: 2022-06-22
    - polar-h10 recording failed
- player id: 67
    - date: 2022-06-28
    - SteamVR crashes after 15min, so there are two CSV files for that session
- player id: 62
    - date: 2022-06-29
    - Empathica recording failed
- player id: 63
    - date: 2022-06-29
    - Empathica recording failed
- player id: 44
    - date: 2022-07-05
    - Eye motion recording failed
- player id: 72
    - date: 2022-07-20
    - polar-h10 recording failed
- player id: 65
    - date: 2022-08-03
    - polar-h10 recording failed
- player id: 75
    - date: 2022-08-18
    - 14:41:35 - 14:43:30 short break, briefly taken off the HMD
- player id: 72
    - date: 2022-08-18
    - polar-h10 recording failed after 35 min


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
  This work by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.hci.uni-wuerzburg.de">Christian Schell, Fabian Sieper, Lukas Schach, Marc E. Latoschik</a> is
  licensed under <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1">
  <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1"></a>
</p>
