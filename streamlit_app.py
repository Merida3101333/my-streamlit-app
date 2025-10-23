import streamlit as st
st.set_page_config(page_title="Hello Streamlit", page_icon="🚀")
st.title("Hello, Streamlit Community Cloud! 🚀")
name = st.text_input("Your name", "World")
st.write(f"Hi, {name}!")
st.success("If you see this on the cloud, deployment worked!")
