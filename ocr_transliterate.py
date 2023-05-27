import streamlit as st
from PIL import Image
import pytesseract
from ai4bharat.transliteration import XlitEngine


@st.cache_resource
def load_model():
    xlit_engine = XlitEngine(beam_width=10, src_script_type = "indic")
    return xlit_engine

def load_text_from_image(image):
    text = pytesseract.image_to_string(image, lang="guj")
    return text

def load_transliteration_from_image(image, xlit_engine):
    text = pytesseract.image_to_string(image, lang="guj")
    docx_text = xlit_engine.translit_sentence(text, 'gu')
    return docx_text

def main():
    new_title = '<p style="font-size: 42px;">Vachanamrutji Transliteration App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    read_me = st.markdown("""
    This project was built using Streamlit and Ai4-bharat transliteration  
    to create transliterated version of Patranks from Gujarati to English.""")
    st.sidebar.title("Select Activity")
    xlit_engine = load_model()
    choice  = st.sidebar.selectbox("MODE",("About","Text from Image (Gujarati)","Transliterated version (English)"))
    text = ""
    if choice == "Text from Image (Gujarati)":
        read_me_0.empty()
        read_me.empty()
        # GlobalHydra.instance().clear()
        st.header('Text from Image (Gujarati)')
        st.subheader('Patrank screenshot:')
        st.write('Please upload a screenshot image of the Patrank (png/ jpg) to get Gujarati text from Image')
        with st.form("ocr_patrank"):
            img_file = st.file_uploader(label="patrank_ocr_version", label_visibility="hidden")
            submitted = st.form_submit_button("Submit")
        if submitted:
            # To read image file buffer as a PIL Image:
            image = Image.open(img_file)
            with st.spinner("Loading..."):
                text = load_text_from_image(image)
        st.write(text)
    elif choice == "Transliterated version (English)":
        st.header("Transliterated version (English)")
        read_me_0.empty()
        read_me.empty()
        st.subheader('Patrank screenshot:')
        st.write('Please upload a screenshot image of the Patrank (png/ jpg) to get a translilterated version in English.')
        with st.form("transliterate_patrank"):
            img_file = st.file_uploader(label="patrank_transliterated_version", label_visibility="hidden")
            submitted = st.form_submit_button("Submit")
        if submitted:
            # To read image file buffer as a PIL Image:
            image = Image.open(img_file)
            with st.spinner("Loading..."):
                text = load_transliteration_from_image(image, xlit_engine)
        st.write(text)      
    elif choice == "About":   
        print()
        

if __name__ == '__main__':
	main()
