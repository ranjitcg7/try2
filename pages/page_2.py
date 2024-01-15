import streamlit as st


st.title('This is Page 2')

if st.button("Home"):
    st.switch_page("streamlit_app.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")


