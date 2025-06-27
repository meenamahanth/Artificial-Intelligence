from ultralytics import YOLO
import cv2

# Load a pretrained YOLO model
model = YOLO("v34.pt")

# Open video file
cap = cv2.VideoCapture("NightDroneVideo.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on the current frame
    results = model(frame)

    # Plot the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Drone Detection", annotated_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
