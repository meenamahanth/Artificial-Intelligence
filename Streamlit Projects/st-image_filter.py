import streamlit as st
import cv2
import numpy as np
from PIL import Image
st.set_page_config(page_title="Image Filter Gallery", layout="centered")
st.title("🖼️ Image Filter Gallery ")
st.sidebar.header("Choose a Filter")
filters = ["Original", "Grayscale", "Sepia", "Sketch", "Blur", "Emboss"]
selected_filter = st.sidebar.radio("Select Filter:", filters)
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
def apply_filter(image, filter_type):
    img_array = np.array(image)
    if filter_type == "Grayscale":
        return cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    elif filter_type == "Sepia":
        sepia_filter = np.array([[0.393, 0.769, 0.189],[0.349, 0.686, 0.168],[0.272, 0.534, 0.131]])
        sepia_img = cv2.transform(img_array, sepia_filter)
        sepia_img = np.clip(sepia_img, 0, 255)
        return sepia_img.astype(np.uint8)
    elif filter_type == "Sketch":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blur, scale=256)
        return sketch
    elif filter_type == "Blur":
        return cv2.GaussianBlur(img_array, (15, 15), 0)
    elif filter_type == "Emboss":
        kernel = np.array([[-2, -1, 0],[-1, 1, 1],[0, 1, 2]])
        embossed = cv2.filter2D(img_array, -1, kernel)
        return embossed
    else:  # Original
        return img_array
if uploaded_file:
    image = Image.open(uploaded_file)
    filtered_image = apply_filter(image, selected_filter)
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original Image", width=300)
    with col2:
        if selected_filter in ["Grayscale", "Sketch"]:
            st.image(filtered_image, caption=f"{selected_filter} Image", channels="GRAY", width=300)
        else:
            st.image(filtered_image, caption=f"{selected_filter} Image", width=300)