import cv2
import numpy as np

def detect_and_highlight_studs(video_path):
    cap = cv2.VideoCapture(video_path)

    # Get the original frame size
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Set the desired window size
    window_width = 1920
    window_height = 1080

    # Calculate the scale factor
    scale_factor = min(window_width / frame_width, window_height / frame_height)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize the frame to fit within the window
        frame = cv2.resize(frame, None, fx=scale_factor, fy=scale_factor)

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise and aid edge detection
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Use Canny edge detector
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edged image
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Loop over the contours
        for contour in contours:
            # Approximate the contour to a polygon
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            # If the polygon has a sufficient number of vertices (studs usually have 8 corners)
            if len(approx) > 5:
                # Draw the contour on the frame
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), 2)

        # Display the result
        cv2.imshow('Studs Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Replace 'path/to/your/video.mp4' with the path to your video file
detect_and_highlight_studs('filmik.mp4')
