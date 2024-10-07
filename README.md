# Remote Security Camera with Motion Detection and Email Alert System

This project implements a motion detection system using OpenCV and Haar Cascade classifiers for detecting human body parts (face, full body, upper body, lower body). When a significant change is detected in the video feed (e.g., movement), a video is captured and saved locally, and an email alert is optionally sent.

## Features

- Detects human body parts using pre-trained Haar Cascade classifiers.
- Triggers video recording when significant motion is detected.
- Optionally sends an email notification with an alert.
  
## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- An email-sending module (`Email`) – should be implemented separately or adapted from an email library like `smtplib`.
- Haar Cascade XML files (for body, face, etc.)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/motion-detection.git
    cd motion-detection
    ```

2. Install dependencies:
    ```bash
    pip install opencv-python numpy
    ```

3. Download the required Haar Cascade XML files:
    - [Full Body Haar Cascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml)
    - [Face Haar Cascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
    - [Upper Body Haar Cascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_upperbody.xml)
    - [Lower Body Haar Cascade](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_lowerbody.xml)
   
   Place these XML files in the project directory.

## Usage

1. Open the `main.py` file and ensure the email-sending module is properly set up, or comment out that section if you don't need email notifications.

2. Run the program:
    ```bash
    python main.py
    ```

3. The program will start capturing video from the default webcam. If motion is detected, a video will be recorded, and an email alert (if enabled) will be sent.

### Quit
- To stop the program, press the `q` key.

## Code Overview

- **Motion Detection**: Background subtraction and morphological operations are used to detect changes in the video feed.
- **Haar Cascade**: Pre-trained Haar Cascades are used to detect human body parts (full body, face, upper body, lower body).
- **Video Capture**: Once motion is detected, the system records a video for a short duration (3 seconds).
- **Email Notification**: After video capture, the system can optionally send an email alert (commented out in the code).

## Potential Improvements

- Re-enable the email alert by uncommenting the `mailer.send()` part and configuring the email-sending logic.
- Improve the detection by adjusting the motion sensitivity.

