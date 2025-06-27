import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter height in meters:")
weight = st.number_input("Enter weight in kilograms:")

if height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is {bmi:.2f}")
