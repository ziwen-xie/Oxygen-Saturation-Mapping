
# Multispectral 2D Mapping for Oxygen Saturation in Tumor Detection

# Project Abstract
Tumors exhibit greater vascularization and lower blood oxygenation. Suspicious tumors may be detected by measuring the changes in oxygen saturation (SO2), noninvasively.  A method to perform 2D SO2 mapping of superficial human tissue is developed. Oxygenated and deoxygenated hemoglobin exhibit distinctive reflection patterns of light in response to both red and near-infrared (NIR) wavelengths. Using a multispectral imaging technique, SO2 mapping of a region of interest (ROI) can be performed. Light from red and NIR LEDs is sequentially projected on tissue while the image sequence is automatically recorded.  Frames are then isolated and processed at each illumination wavelength. LEDs are placed at a specific angle relative to the surface of the tissue so that the camera only captures reflected light that interacts with the targeted tissue. The frames are then analyzed with an algorithm that was designed to extract and process the light intensities frame by frame. Each frame is split into 10X10 pixels areas. The average intensity of each area is collected over time. Matching pixel coordinates are then used to produce SO2 maps. Both the device and the algorithm are validated by liquid phantoms that mimic the optical properties of oxygenated and deoxygenated tissues. Consequently, our product, utilizing 2D SO2 imaging technology, is capable of producing high-resolution images of SO2 mapping from targeted tissues based on the difference in vascularization.

# Description of files
This device is working on a Raspberry Pi system.  Environment has to be set up to make sure the code's functionality. The setting up of the environment is described in section [#environment setup](https://github.com/ziwen-xie/Oxygen-Saturation-Mapping#environment-setup)

# Run the script
There are two ways to run the scripts:
## MATLAB
1. run the GUI on Raspberry Pi, capture image sequences and store them
2. manually export the image sequence files to another device with MATLAB installed
3. analyze using MATLAB scripts

## Directly run on Raspberry Pi system via Python
1. run the GUI on Raspberry Pi, capture image sequences
2. analyze using GUI's analyze function

# Environment Setup


