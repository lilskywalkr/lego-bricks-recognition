# LEGO Brick Detection and Color Recognition

This project detects LEGO bricks in a video feed and recognizes their colors using computer vision techniques.  
It uses **OpenCV** for image processing and **scikit-image** for region detection.

---

## Features

- Detects LEGO bricks in real-time from a video.
- Recognizes brick colors based on predefined color mappings.
- Draws contours around detected bricks.
- Annotates bricks with their detected color names.
- Displays a live annotated video window.

---

## Technologies Used

- Python 3
- OpenCV
- NumPy
- scikit-image

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/lego-brick-detection.git
   cd lego-brick-detection
   
2. Install the required packages:

    ```bash
   pip install opencv-python scikit-image numpy
   
3. Place your video file inside a `video/` folder, for example:  
   `video/lego_bricks.mp4`

4. Run the program:

   ```bash
   python main.py
   
---

## How It Works

- The video frames are processed one by one.
- Each frame is resized to fit within a 1024x900 window.
- The frame is converted to grayscale and smoothed using Gaussian blur.
- Thresholding and Canny edge detection are applied to find edges.
- Bricks are detected by analyzing connected regions.
- The average color of each detected region is calculated.
- The closest predefined color is matched and labeled on the brick.
- Contours are drawn to highlight the detected bricks.

---

## Predefined Brick Colors

| Color Name | RGB Value           |
|------------|---------------------|
| Blue       | (162, 56, 2)         |
| Red        | (38, 33, 162)        |
| Green      | (60, 180, 120)       |
| Orange     | (40, 130, 220)       |
| Pink       | (160, 115, 225)      |
| Brown      | (45, 50, 82)         |

---

## Screenshots Overview

Here are some example screenshots showing how the system detects bricks:

![showcase_1](https://github.com/user-attachments/assets/e05099d9-69a4-45fe-a3a5-c9ee8adfd753)
![showcase_2](https://github.com/user-attachments/assets/cab0e859-5327-49ab-a4f7-7b64714d6071)
![showcase_3](https://github.com/user-attachments/assets/11555172-90c9-417f-be2d-da6e169ea588)

---

## Acknowledgments

- OpenCV documentation
- scikit-image library
- LEGO® for inspiring creativity
