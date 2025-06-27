import streamlit as st
def calculate(expression):
    try:
        return eval(expression)
    except Exception:
        return "Error"
def main():
    st.title("Simple Calculator")
    # Put color picker in the sidebar
    color = st.sidebar.color_picker("Pick a Background Color", "#FFFFFF")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    expression = st.text_input("Enter expression (e.g., 2+3*4):")
    if st.button("Calculate"):
        result = calculate(expression)
        st.write(f"Result: {result}")
if __name__ == "__main__":
    main()