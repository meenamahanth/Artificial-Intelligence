import wget
import urllib.request
# After running this code this code downloads gesture_recognizer.task and
# Four images pointing_up.jpg, thumbs_down.jpg, thumbs_up.jpg, victory.jpg

# Download the MediaPipe model
model_url = "https://storage.googleapis.com/mediapipe-models/gesture_recognizer/gesture_recognizer/float16/1/gesture_recognizer.task"
wget.download(model_url, "gesture_recognizer.task")

# Download test images
image_names = ['thumbs_down.jpg', 'victory.jpg', 'thumbs_up.jpg', 'pointing_up.jpg']
base_url = 'https://storage.googleapis.com/mediapipe-tasks/gesture_recognizer/'

for name in image_names:
    urllib.request.urlretrieve(base_url + name, name)