import streamlit as st

st.title("To-Do List")

task = st.text_input("Add a task:")
if st.button("Add Task"):
    st.session_state.tasks = st.session_state.get("tasks", []) + [task]

for i, t in enumerate(st.session_state.get("tasks", [])):
    if st.checkbox(t, key=i):
        st.session_state.tasks.pop(i)
        st.rerun()
