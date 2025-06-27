import streamlit as st
import matplotlib.pyplot as plt

st.title("Plot Generator")

data = st.text_input("Enter comma-separated numbers:", "10,20,30")
plot_type = st.selectbox("Select plot type:", ["Bar", "Line", "Pie"])

nums = list(map(int, data.split(',')))

fig, ax = plt.subplots()
if plot_type == "Bar":
    ax.bar(range(len(nums)), nums)
elif plot_type == "Line":
    ax.plot(nums)
elif plot_type == "Pie":
    ax.pie(nums, labels=[str(i) for i in nums], autopct='%1.1f%%')
st.pyplot(fig)
