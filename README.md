# Car Racing Speed Analysis

## Description
This project utilizes OpenCV to analyze video footage of car racing and calculate the speed of vehicles based on pixel distance. The application detects moving objects, draws bounding boxes around them, and displays the estimated speed in meters per second (m/s) on the video feed in real-time.

## Features
- Real-time detection of moving objects in a video.
- Speed calculation based on movement between consecutive frames.
- Visual feedback with bounding boxes and speed overlay.
- Easy to use with any video file by updating the path.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/car-racing-speed-analysis.git
   cd car-racing-speed-analysis



![Screenshot 2025-06-02 120512](https://github.com/user-attachments/assets/df343885-7d57-49d2-ab9d-fe5dce428c63)


## How It Works
The project follows a systematic approach to analyze the video and calculate the speed of moving objects. Below is a detailed breakdown of the workflow:

### Workflow
- **Video Capture:** The script opens the specified video file and reads it frame by frame.
- **Preprocessing:** Each frame is converted to grayscale and blurred to reduce noise, making edge detection more effective.
- **Edge Detection:** The Canny edge detector is applied to identify edges in the blurred image.
- **Contour Detection:** Contours are extracted from the edge-detected image to locate potential moving objects.
- **Filtering Contours:** Contours are filtered based on area to ignore small or irrelevant detections.
- **Position Tracking:** The center position of each detected object is calculated, and the pixel distance traveled between frames is measured.
- **Speed Calculation:** The pixel distance is converted to real-world distance using a reference distance, and speed is calculated based on the frame rate.
- **Visualization:** Bounding boxes are drawn around detected objects, and the calculated speed is displayed on the video feed.
- **Real-time Display:** The processed frames are displayed in a window, allowing for real-time analysis.

### Model
The model used in this project is based on traditional computer vision techniques rather than machine learning. It leverages OpenCV's capabilities for image processing, including:
- Grayscale conversion
- Gaussian blurring
- Canny edge detection
- Contour detection and analysis

### Procedure
- **Initialization:** Set constants for frames per second (FPS), reference distance, and pixel distance.
- **Function Definition:** Define a function `calculate_speed` to convert pixel distance to speed in meters per second.
- **Video Processing Loop:**
  - Read each frame from the video.
  - Convert the frame to grayscale and apply Gaussian blur.
  - Detect edges and find contours.
  - For each contour, check if it meets the area threshold.
  - Calculate the center position and, if applicable, the pixel distance from the previous position.
  - Compute the speed and overlay it on the frame.
  - Display the processed frame with bounding boxes and speed annotations.
- **Exit Condition:** Allow the user to exit the video display by pressing 'q'.

