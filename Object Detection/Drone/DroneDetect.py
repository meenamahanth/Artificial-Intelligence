from ultralytics import YOLO

# Load a model
model = YOLO("v34.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model(["night-drone.png"])  # mutlidrone.jpg

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    result.save(filename="drone-result.jpg")  # multidrone-result.jpg