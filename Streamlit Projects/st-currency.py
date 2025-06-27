import streamlit as st
from forex_python.converter import CurrencyRates

st.title("Currency Converter")

c = CurrencyRates()
amount = st.number_input("Enter amount:")
from_curr = st.text_input("From Currency (e.g., USD):")
to_curr = st.text_input("To Currency (e.g., INR):")

if st.button("Convert"):
    try:
        result = c.convert(from_curr, to_curr, amount)
        st.write(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    except:
        st.error("Invalid currency code or connection issue")
