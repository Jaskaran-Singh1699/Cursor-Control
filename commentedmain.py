import cv2
import mediapipe as mp
import pyautogui

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize the hand detector
hand_detector = mp.solutions.hands.Hands()

# Initialize the drawing utilities
drawing_utils = mp.solutions.drawing_utils

# Get the screen width and height
screen_width, screen_height = pyautogui.size()

# Initialize the index_y variable to calculate the difference between index and thumb
index_y = 0

# Main loop
while True:
    # Capture a frame from the webcam
    _, frame = cap.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Get the frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with the hand detector
    output = hand_detector.process(rgb_frame)

    # Get the detected hands
    hands = output.multi_hand_landmarks

    # If hands are detected
    if hands:
        # Iterate through the detected hands
        for hand in hands:
            # Draw the landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand)

            # Get the landmarks
            landmarks = hand.landmark

            # Iterate through the landmarks
            for id, landmark in enumerate(landmarks):
                # Get the x and y coordinates of the landmark
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # If the landmark is the index finger tip
                if id == 8:
                    # Draw a yellow circle around the index finger tip
                    cv2.circle(img=frame, center=(x, y), radius=20, color=(0, 255, 255))

                    # Convert the coordinates to actual screen pixels
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                    # Move the cursor to the position of the index finger tip
                    pyautogui.moveTo(index_x, index_y)

                # If the landmark is the thumb tip
                elif id == 4:
                    # Draw a blue circle around the thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 0, 255))

                    # Convert the coordinates to actual screen pixels
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # If the distance between the index finger tip and thumb tip is less than 20 pixels
                    if abs(index_y - thumb_y) < 20:
                        # Perform a left click
                        print('left click')
                        pyautogui.leftClick()
                        pyautogui.sleep(1)

                # If the landmark is the mid finger tip
                elif id == 12:
                    # Draw a green circle around the mid finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))

                    # Convert the coordinates to actual screen pixels
                    mid_x = screen_width / frame_width * x
                    mid_y = screen_height / frame_height * y

                    # If the distance between the mid finger tip and thumb tip is less than 20 pixels
                    if abs(mid_y - thumb_y) < 20:
                        # Perform a right click
                        print('right click')
                        pyautogui.rightClick()
                        pyautogui.sleep(1)

                # If the landmark is the pinky finger tip
                elif id == 20:
                    # Draw a green circle around the pinky finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))

                    # Convert the coordinates to actual screen pixels
                    pinkey_x = screen_width / frame_width * x
                    pinkey_y = screen_height / frame_height * y

                    # If the distance between the pinky finger tip and thumb tip is less than 20 pixels
                    if abs(pinkey_y - thumb_y) < 20:
                        # Scroll up
                        print('scroll up')
                        pyautogui.scroll(500)
                        pyautogui.sleep(1)

                # If the landmark is the ring finger tip
                elif id == 16:
                    # Draw a green circle around the ring finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 0))

                    # Convert the coordinates to actual screen pixels
                    ring_x = screen_width / frame_width * x
                    ring_y = screen_height / frame_height * y

                    # If the distance between the ring finger tip and thumb tip is less than 20pixels
                    if abs(ring_y - thumb_y) < 20:
                        # Scroll down
                        print('scroll down')
                        pyautogui.scroll(-500)
                        pyautogui.sleep(1)

    # Display the frame
    cv2.imshow('Hand Gesture Recognition', frame)

    # Exit the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()