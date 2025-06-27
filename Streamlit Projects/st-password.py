import streamlit as st
import random
import string

st.title("Random Password Generator")

length = st.slider("Password length:", 6, 30)
use_digits = st.checkbox("Include numbers", True)
use_specials = st.checkbox("Include special characters", True)

chars = string.ascii_letters
if use_digits:
    chars += string.digits
if use_specials:
    chars += string.punctuation

password = ''.join(random.choices(chars, k=length))
st.text_input("Generated password:", password)
