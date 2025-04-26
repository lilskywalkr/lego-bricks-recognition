import cv2
import numpy as np
import skimage

brick_colors = {'blue': (162, 56, 2), 'red': (38, 33, 162), 'green': (60, 180, 120), 'orange': (40, 130, 220), 'pink': (160, 115, 225), 'brown': (45, 50, 82)}
FONT = cv2.FONT_HERSHEY_SIMPLEX


def find_closest_color(average_color):
    distances = {name: np.linalg.norm(np.array(average_color) - np.array(color)) for name, color in brick_colors.items()}
    closest_color = min(distances, key=distances.get)
    return closest_color


def brick_detection_and_color_recognition(video_path):
    cap = cv2.VideoCapture(video_path)

    # Get the original frame size
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Set the desired window size
    window_width = 1024
    window_height = 900

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
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)

        _, threshold = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)
        #cv2.imshow('brick detection', threshold)

        # Use Canny edge detector
        edges = cv2.Canny(threshold, 50, 150)

        segments = skimage.measure.label(edges)
        regions = skimage.measure.regionprops(segments)

        filtered_regions = [region for region in regions if region.area > 400]

        for region in filtered_regions:
            y, x = region.centroid
            cv2.line(frame, (int(x) + 200, int(y) - 200), (int(x), int(y)), (0, 0, 0), 10)
            region = region.slice
            image = frame[region]
            avg = np.mean(image, axis=(0, 1))
            color = find_closest_color(avg)
            cv2.putText(
                img=frame,
                text=color,
                org=((int(x) + 200, int(y) - 200)),
                fontFace=FONT,
                fontScale=2,
                color=(0, 0, 0),
                thickness=4,
            )

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
        cv2.imshow('Lego bricks and color detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Replace 'path/to/your/video.mp4' with the path to your video file
brick_detection_and_color_recognition('video/lego_bricks.mp4')
