# First run for-main.py file and it download the four images and gesture_recoginizer.task file
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.framework.formats import landmark_pb2
import matplotlib.pyplot as plt


# Image list
IMAGE_FILENAMES = ['thumbs_down.jpg', 'victory.jpg', 'thumbs_up.jpg', 'pointing_up.jpg']

# Setup recognizer
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# Process images
images = []
results = []

for file in IMAGE_FILENAMES:
    image = mp.Image.create_from_file(file)
    result = recognizer.recognize(image)
    top_gesture = result.gestures[0][0]
    landmarks = result.hand_landmarks
    images.append((image.numpy_view(), top_gesture, landmarks))

# Drawing setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Show results
rows, cols = 2, 2
plt.figure(figsize=(10, 10))

for idx, (img, gesture, hand_landmarks) in enumerate(images):
    ax = plt.subplot(rows, cols, idx + 1)
    image = img.copy()

    for lm_list in hand_landmarks:
        proto = landmark_pb2.NormalizedLandmarkList()
        proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=lm.x, y=lm.y, z=lm.z) for lm in lm_list
        ])
        mp_drawing.draw_landmarks(
            image,
            proto,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )

    ax.imshow(image)
    ax.set_title(f"{gesture.category_name} ({gesture.score:.2f})")
    ax.axis('off')

plt.tight_layout()
plt.show()
