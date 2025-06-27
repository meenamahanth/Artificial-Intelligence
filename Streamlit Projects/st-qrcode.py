import streamlit as st
import qrcode
from PIL import Image
import io  # Import io for byte conversion

st.title("QR Code Generator")

text = st.text_input("Enter text or URL:")

if st.button("Generate"):
    img = qrcode.make(text)  # Generates a PIL Image

    # Convert the image to bytes without saving
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")  # Convert to PNG format

    # Display the image directly in Streamlit
    st.image(img_bytes.getvalue(), caption="Generated QR Code", use_container_width=True)
