# 1. Project Abstract
Tumors exhibit greater vascularization and lower blood oxygenation. Suspicious tumors may be detected by measuring the changes in oxygen saturation (SO2), noninvasively.  A method to perform 2D SO2 mapping of superficial human tissue is developed. Oxygenated and deoxygenated hemoglobin exhibit distinctive reflection patterns of light in response to both red and near-infrared (NIR) wavelengths. Using a multispectral imaging technique, SO2 mapping of a region of interest (ROI) can be performed. Light from red and NIR LEDs is sequentially projected on tissue while the image sequence is automatically recorded.  Frames are then isolated and processed at each illumination wavelength. LEDs are placed at a specific angle relative to the surface of the tissue so that the camera only captures reflected light that interacts with the targeted tissue. The frames are then analyzed with an algorithm that was designed to extract and process the light intensities frame by frame. Each frame is split into 10X10 pixels areas. The average intensity of each area is collected over time. Matching pixel coordinates are then used to produce SO2 maps. Both the device and the algorithm are validated by liquid phantoms that mimic the optical properties of oxygenated and deoxygenated tissues. Consequently, our product, utilizing 2D SO2 imaging technology, is capable of producing high-resolution images of SO2 mapping from targeted tissues based on the difference in vascularization.

# 2. Description of files
This device is working on a Raspberry Pi system.  Environment has to be set up to make sure the code's functionality. The setting up of the environment is described in section [4. Environment Setup]
This repository consists of several files.
The `README.md` is the description file.
The `GUI2.py` is the latest Graphical User Interface that combines all other python scripts
`GUI.py` is the first edition of the Graphical User Interface and can provide the most basic functions

**NOTE**: When downloading files, please make sure to store the files in the same folder, otherwise importing problems might happen. 


# 3. Script Execution
## 3.1 Platforms
Analyze process can be done in two platforms:
## 3.1.1 MATLAB
1. run the `GUI` on Raspberry Pi, capture image sequences and store them
2. manually export the image sequence files to another device with MATLAB installed
3. analyze using MATLAB scripts

## 3.1.2 Directly run on Raspberry Pi system via Python
1. run the `GUI` on Raspberry Pi, capture image sequences
2. analyze using `GUI`'s analyze function

## 3.2 Graphical User Interface
The GUI is a python script that can conduct all the necessary functions of the device.
### 3.2.1 Capture Image Sequence

# 4. Environment Setup
## 4.1 System
For the most comfortable user experience, please use a Raspberry Pi with at least model 3B.  Model 3B+ is favored. 
The model of Raspberry Pi can be found when you input the following command in terminal: 
```bash
$ cd ~
$ cat /proc/cpuinfo
```
Please make sure an appropriate operating system is installed in the Raspberry Pi:
```bash
pi@raspberrypi:~ $ cat /etc/os-release

PRETTY_NAME="Raspbian GNU/Linux 11 (bullseye)"
NAME="Raspbian GNU/Linux"
VERSION_ID="11"
VERSION="11 (bullseye)"
VERSION_CODENAME=bullseye
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

```


