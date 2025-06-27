import streamlit as st
from fpdf import FPDF

st.title("Resume Builder")

name = st.text_input("Full Name")
email = st.text_input("Email")
summary = st.text_area("Summary")

if st.button("Generate Resume"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=name, ln=True)
    pdf.cell(200, 10, txt=email, ln=True)
    pdf.multi_cell(0, 10, summary)
    pdf.output("resume.pdf")
    st.success("Resume generated as resume.pdf")
