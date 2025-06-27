import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Finger tip landmark indexes (from MediaPipe)
TIP_IDS = [4, 8, 12, 16, 20]

# Helper: check which fingers are up
def fingers_up(hand_landmarks):
    finger_states = []

    # Thumb
    if hand_landmarks.landmark[TIP_IDS[0]].x < hand_landmarks.landmark[TIP_IDS[0] - 1].x:
        finger_states.append(1)
    else:
        finger_states.append(0)

    # Other fingers
    for id in range(1, 5):
        if hand_landmarks.landmark[TIP_IDS[id]].y < hand_landmarks.landmark[TIP_IDS[id] - 2].y:
            finger_states.append(1)
        else:
            finger_states.append(0)

    return finger_states  # e.g., [1, 0, 0, 0, 0]

# Match finger states to gestures
def detect_custom_gesture(finger_states):
    if finger_states == [0, 1, 1, 0, 0]:
        return "Victory ✌️"
    elif finger_states == [0, 1, 0, 0, 0]:
        return "Pointing ☝️"
    elif finger_states == [1, 1, 1, 1, 1]:
        return "Open Palm ✋"
    elif finger_states == [0, 0, 0, 0, 0]:
        return "Fist ✊"
    elif finger_states == [1, 0, 0, 0, 1]:
        return "Call Me 🤙"
    else:
        return "Unknown"

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_states = fingers_up(hand_landmarks)
            gesture = detect_custom_gesture(finger_states)

            cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow("Custom Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
