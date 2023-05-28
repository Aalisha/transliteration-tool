import streamlit as st
from PIL import Image
import pytesseract
from ai4bharat.transliteration import XlitEngine

img = Image.open('Raj_Gurudev.png')
st.set_page_config(page_title='Vachanamrutji Transliteration tool', page_icon=img, layout="wide", initial_sidebar_state="expanded")
@st.cache_resource
def load_model():
    xlit_engine = XlitEngine(beam_width=10, src_script_type = "indic")
    return xlit_engine

def main():
    new_title = '<p style="font-size: 42px;">Vachanamrutji Transliteration App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    This project was built using Streamlit and Ai4-bharat transliteration  
    to create transliterated version of Patranks from Gujarati to English.""")
    st.sidebar.title("Select Activity")
    xlit_engine = load_model()
    values =["About", "Patrank Transliteration (English)"]
    choice  = st.sidebar.selectbox("MODE", values, index=1)
    text = ""
    docx_text = ""
    if choice == "Patrank Transliteration (English)":
        st.header("Patrank Transliteration (English)")
        read_me_0.empty()
        read_me.empty()
        st.write('Please upload an image screenshot of the Patrank (png/ jpg) to get a translilterated version from **Gujarati** in **English**.')
        img_file = st.file_uploader(label="patrank_transliterated_version", label_visibility="hidden")
        #submitted = st.form_submit_button("Submit")
        if img_file is not None:
            # To read image file buffer as a PIL Image:
            image = Image.open(img_file)
            with st.spinner("Loading..."):
                text = pytesseract.image_to_string(image, lang="guj")
                docx_text = xlit_engine.translit_sentence(text, 'gu')
        
            c1, c2 = st.columns(2)
            with c1:
                st.subheader('Original Text (Gujarati)')
                st.write(text)
            with c2:
                st.subheader("Transliterated Text (English)")
                st.write(docx_text)      
    elif choice == "About":   
        print()
        

if __name__ == '__main__':
	main()	
