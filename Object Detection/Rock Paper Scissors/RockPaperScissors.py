from ultralytics import YOLO

# Load a model
model = YOLO("v4.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model(["test-rps.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    result.show()  # display to screen
    result.save(filename="rps-result.jpg")  # save to disk