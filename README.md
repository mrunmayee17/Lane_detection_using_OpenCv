# Vehicle_lane_detection
# Lane Detection with OpenCV

This project demonstrates lane detection in images and videos using OpenCV. It includes several utility functions for edge detection, region of interest selection, and optimizing lane lines in a video.

## Overview

- `test_image.jpg`: An example image for testing lane detection.

- `utility` folder: Contains utility functions for lane detection.

## Dependencies

Make sure you have the following Python libraries installed:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Matplotlib (`matplotlib`)

You can install these dependencies using pip:

```bash
pip install opencv-python numpy matplotlib

```


## Usage
* 		Clone the repository:


Copy code
git clone https://github.com/yourusername/lane-detection.git cd lane-detection
* 		Run the lane detection script:


Copy code
python lane_detection.py
* The script will process the video "test2.mp4" for lane detection and display the output.
* 		Press 'q' to exit the video playback.

<img width="1277" alt="Screenshot 2023-09-14 at 12 52 10 PM" src="https://github.com/mrunmayee17/Vehicle_lane_detection/assets/48186569/fa16470c-f8dc-445b-9b6c-3cb3facda832">

## Functions
* cannyimage: Performs Canny edge detection on an input image.
* region_of_interest: Defines a region of interest in the image where lane lines are expected.
* makeCoordinates: Calculates coordinates for drawing lane lines.
* optimizedLines: Optimizes and averages detected lane lines.
* display_line_image: Draws the detected lane lines on an image.

## Author
MRUNMAYEE RANE
* GitHub: https://github.com/mrunmayee17
