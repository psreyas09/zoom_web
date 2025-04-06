import cv2
import mediapipe as mp
import numpy as np
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initial zoom level and previous distance for smoothing
previous_zoom_level = 1.0
previous_distance = None  # For smoothing

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a more natural feel
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    current_zoom_level = 1.0  # Default zoom level

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get thumb and index finger landmarks
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate distance between thumb and index finger
            distance = calculate_distance(thumb_tip, index_finger_tip)

            # Smooth the distance to reduce sensitivity
            smoothing_factor = 0.3  # Medium smoothing
            smoothed_distance = smoothing_factor * distance + (1 - smoothing_factor) * (previous_distance if previous_distance is not None else distance)
            distance = smoothed_distance
            previous_distance = distance

            # Adjust zoom level based on distance
            current_zoom_level = max(1.0, min(3.0, 1.0 + distance * 5))  # Medium scaling factor

    # Simulate global zoom based on changes in zoom level
    zoom_in_threshold = 0.25  # Medium threshold
    zoom_out_threshold = 0.25  # Medium threshold

    if current_zoom_level - previous_zoom_level > zoom_in_threshold:
        pyautogui.hotkey('ctrl', '=')  # Simulate zoom in
        previous_zoom_level = current_zoom_level
    elif previous_zoom_level - current_zoom_level > zoom_out_threshold:
        pyautogui.hotkey('ctrl', '-')  # Simulate zoom out
        previous_zoom_level = current_zoom_level

    # Debugging output (optional, remove in production)
    print(f"Current Zoom Level: {current_zoom_level}, Previous Zoom Level: {previous_zoom_level}")

    # Display the original frame (no local zoom applied)
    cv2.imshow("Hand Gesture Zoom", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()