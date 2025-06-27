import streamlit as st

st.title("Temperature Converter")

temp = st.number_input("Enter temperature:")
unit = st.selectbox("Select unit:", ["Celsius", "Fahrenheit", "Kelvin"])

if unit == "Celsius":
    st.write(f"Fahrenheit: {temp * 9/5 + 32}")
    st.write(f"Kelvin: {temp + 273.15}")
elif unit == "Fahrenheit":
    st.write(f"Celsius: {(temp - 32) * 5/9}")
    st.write(f"Kelvin: {(temp - 32) * 5/9 + 273.15}")
else:
    st.write(f"Celsius: {temp - 273.15}")
    st.write(f"Fahrenheit: {(temp - 273.15) * 9/5 + 32}")
