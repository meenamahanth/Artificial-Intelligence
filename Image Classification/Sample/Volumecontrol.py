import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Get default audio device using Pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_range = volume.GetVolumeRange()  # (min, max, step)
min_vol = vol_range[0]
max_vol = vol_range[1]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]

        # Get coordinates of thumb tip and index finger tip
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]

        h, w, _ = img.shape
        x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
        x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

        # Draw landmarks and connections
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Draw circles on tips
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # Calculate distance between thumb and index finger
        length = np.hypot(x2 - x1, y2 - y1)

        # Convert length to volume level
        # Adjust these min/max lengths depending on your webcam distance
        vol = np.interp(length, [30, 200], [min_vol, max_vol])
        volume.SetMasterVolumeLevel(vol, None)

        # Show volume percentage on screen
        vol_percent = np.interp(length, [30, 200], [0, 100])
        cv2.putText(img, f'Vol: {int(vol_percent)} %', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Volume Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
