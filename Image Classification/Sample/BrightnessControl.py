import cv2
import mediapipe as mp
import numpy as np
import wmi

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

wmi_interface = wmi.WMI(namespace='wmi')
brightness_control = wmi_interface.WmiMonitorBrightnessMethods()[0]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        landmarks = result.multi_hand_landmarks[0]

        h, w, _ = img.shape
        thumb_tip = landmarks.landmark[4]
        index_tip = landmarks.landmark[8]

        x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
        x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

        mp_draw.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        length = np.hypot(x2 - x1, y2 - y1)

        # Map distance to brightness (0-100)
        brightness = np.interp(length, [30, 200], [0, 100])
        brightness_control.WmiSetBrightness(int(brightness), 0)

        cv2.putText(img, f'Brightness: {int(brightness)} %', (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("Brightness Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
