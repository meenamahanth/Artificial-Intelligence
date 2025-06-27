from ultralytics import YOLO
import cv2
import yt_dlp
import os

video_url = "https://youtu.be/ufUB64ScCDs"
video_filename = "youtube_video.mp4"

# Add logging to see download progress
def download_video(url, filename):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': filename,
        'quiet': False,
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print("❌ Download failed:", str(e))
        return False

# Download video
if not download_video(video_url, video_filename):
    print("❗ Aborting due to video download error.")
    exit(1)

# Load model
model = YOLO("v34.pt")

# Process video
cap = cv2.VideoCapture(video_filename)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    annotated = results[0].plot()
    cv2.imshow("YOLOv8 Drone Detection", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
os.remove(video_filename)
