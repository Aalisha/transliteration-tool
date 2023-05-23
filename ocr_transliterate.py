import streamlit as st
import pandas as pd
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os
import time ,sys
from streamlit_embedcode import github_gist
import urllib.request
import urllib
import moviepy.editor as moviepy
from pydoc import doc
import pdf2image
import pytesseract
from ai4bharat.transliteration import XlitEngine


@st.cache_resource
def load_model():
    xlit_engine = XlitEngine(beam_width=10, src_script_type = "indic")
    return xlit_engine

def main():
    new_title = '<p style="font-size: 42px;">Vachanamrutji Transliteration App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    This project was built using Streamlit and Ai4-bharat transliteration  
    to create Gujarati transliterated version of Patranks.""")
    st.sidebar.title("Select Activity")
    xlit_engine = load_model()
    choice  = st.sidebar.selectbox("MODE",("About","OCR version (Patrank)","Gujarati Transliterated version (Patrank)"))
    text = ""
    if choice == "OCR version (Patrank)":
        read_me_0.empty()
        read_me.empty()
        # GlobalHydra.instance().clear()
        st.header('OCR version')
        st.subheader('Patrank screenshot:')
        st.write('Please upload a screenshot image of the Patrank (png/ jpg)')
        img_file = st.file_uploader(label="patrank_ocr_version", label_visibility="hidden")
        if img_file is not None:
            # To read image file buffer as a PIL Image:
            image = Image.open(img_file)
            text = pytesseract.image_to_string(image, lang="guj")
            st.write(text)
    elif choice == "Gujarati Transliterated version (Patrank)":
        st.header("Gujarati transliterated version (Patrank)")
        read_me_0.empty()
        read_me.empty()
        st.subheader('Patrank screenshot:')
        st.write('Please upload a screenshot image of the Patrank (png/ jpg)')
        img_file = st.file_uploader(label="patrank_transliterated_version", label_visibility="hidden")
        if img_file is not None:
            # To read image file buffer as a PIL Image:
            image = Image.open(img_file)
            text = pytesseract.image_to_string(image, lang="guj")
            docx_text = xlit_engine.translit_sentence(text, 'gu')
            st.write(docx_text)
            
    elif choice == "About":   
        print()
        

if __name__ == '__main__':
	main()	
