import streamlit as st


st.title('This is Page 1')

if st.button("Home"):
    st.switch_page("app.py")
if st.button("Page 1"):
    st.switch_page("pages/page_1.py")
if st.button("Page 2"):
    st.switch_page("pages/page_2.py")