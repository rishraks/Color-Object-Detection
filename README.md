# Color Detection Project

This project enables real-time detection of user-defined color objects using a webcam. Users input a color name, and the program identifies objects of that color by converting it to its HSV range, applying a mask, and detecting contours.

## Libraries Used
- **Numpy**: For numerical operations and array handling.
- **OpenCV**: For image processing and real-time object detection.
- **Webcolors**: For converting color names to RGB values.
- **Pillow**: For image manipulation and additional utilities.

## Features
- Detects objects of a user-defined color in real time.
- Highlights detected objects using contours.
- Allows customization of colors through simple name input.

## How It Works
1. Users input the name of a color (e.g., "red", "blue").
2. The program retrieves the RGB value of the color using `webcolors`.
3. RGB values are converted to HSV for accurate color detection.
4. A mask is applied to filter the specified color range.
5. Detected objects are outlined using contours.

## Requirements
- Python 3.6 or higher
- Libraries: `numpy`, `opencv-python`, `webcolors`, `Pillow`

Install the dependencies using:
```bash
pip install numpy opencv-python webcolors Pillow
```

## Usage
- Clone this project
- Run the script using:
```bash
main.py
```
- Enter a color name when prompted.
- The program will display a video feed highlighting objects matching the specified color.