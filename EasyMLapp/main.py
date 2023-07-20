import streamlit as st
from easyml.helper import set_png_as_page_bg
set_png_as_page_bg()
st.title('EasyML.io')
st.subheader('A place where Machine Learning will be Easy to learn!!')

file = st.file_uploader("Pick a File.")
