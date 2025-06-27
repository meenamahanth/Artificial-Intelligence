# Image Classification Repository

> **Requires:** Python **3.11**


1. **Hand Gesture Detection**  
2. **Sample**

---

## 1. Hand Gesture Detection

This module implements hand-gesture recognition using a pre-trained `gesture_recognizer.task` model. It includes multiple scripts to process images, videos, and webcam input.

### Files & Usage

1. **`for-main.py`**  
   - **Description:** Downloads the required model file (`gesture_recognizer.task`) and four sample images:  
     - `pointing_up.jpg`  
     - `thumbs_down.jpg`  
     - `thumbs_up.jpg`  
     - `victory.jpg`  
   - **Usage:**
     ```bash
     python for-main.py
     ```

2. **`main.py`**  
   - **Description:** Runs the hand gesture detector on the four sample images using the downloaded `gesture_recognizer.task` model.  
   - **Inputs:**  
     - `gesture_recognizer.task` (model file)  
     - `pointing_up.jpg`, `thumbs_down.jpg`, `thumbs_up.jpg`, `victory.jpg`  
   - **Usage:**
     ```bash
     python main.py
     ```

3. **`InVideoDetection.py`**  
   - **Description:** Processes a video file (`input.mp4`) to detect hand gestures and generates an annotated output video (`output_annotated.mp4`).  
   - **Inputs:**  
     - `gesture_recognizer.task` (model file)  
     - `input.mp4`  
   - **Usage:**
     ```bash
     python InVideoDetection.py
     ```

4. **`webcam_gesture.py`**  
   - **Description:** Opens the webcam and performs real-time gesture recognition using `gesture_recognizer.task`.  
   - **Inputs:**  
     - `gesture_recognizer.task` (model file)  
   - **Usage:**
     ```bash
     python webcam_gesture.py
     ```

5. **`custom_webcam.py`**  
   - **Description:** Custom webcam interface for gesture prediction without requiring any additional files.  
   - **Usage:**
     ```bash
     python custom_webcam.py
     ```

---

## 2. Sample

Contains simple demonstration scripts for brightness and volume control using hand gestures.

### Files & Usage

1. **`BrightnessControl.py`**  
   - **Description:** Adjusts screen brightness based on the distance between the index finger and thumb.  
   - **Usage:**
     ```bash
     python BrightnessControl.py
     ```

2. **`VolumeControl.py`**  
   - **Description:** Controls system volume using the same finger-distance mechanism.  
   - **Usage:**
     ```bash
     python VolumeControl.py
     ```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Image-Classification
   ```

2. **Create and activate a virtual environment (Python 3.11):**
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```