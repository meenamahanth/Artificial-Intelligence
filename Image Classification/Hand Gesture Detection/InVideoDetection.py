import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2

# Load gesture recognizer
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# Open video
video = cv2.VideoCapture('input.mp4')  # Replace with your video file
if not video.isOpened():
    print("Error opening video file.")
    exit()

# Get video properties for saving output
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

# Define video writer to save output
out = cv2.VideoWriter('output_annotated.mp4',
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      fps, (frame_width, frame_height))

# MediaPipe drawing
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    result = recognizer.recognize(mp_image)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            proto = landmark_pb2.NormalizedLandmarkList()
            proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=lm.x, y=lm.y, z=lm.z) for lm in hand_landmarks
            ])
            mp_drawing.draw_landmarks(
                frame,
                proto,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

            # Highlight wrist landmark (landmark 0) with a big circle for visibility
            wrist = hand_landmarks[0]
            cx, cy = int(wrist.x * frame_width), int(wrist.y * frame_height)
            cv2.circle(frame, (cx, cy), 15, (0, 0, 255), thickness=3)  # Red circle

    if result.gestures:
        gesture = result.gestures[0][0]
        label = f"{gesture.category_name} ({gesture.score:.2f})"

        # Draw filled rectangle for label background
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
        cv2.rectangle(frame, (25, 25 - text_height - baseline), (25 + text_width, 25 + baseline + 10), (0, 255, 0), thickness=cv2.FILLED)

        # Put the text on top of the rectangle
        cv2.putText(frame, label, (25, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, (0, 0, 0), 3, cv2.LINE_AA)  # Black text for contrast

    cv2.imshow("Gesture Recognition", frame)
    out.write(frame)  # Write annotated frame to output video

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
