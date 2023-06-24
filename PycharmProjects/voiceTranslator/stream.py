import webbrowser

import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="voice translation",page_icon=":tada:",layout="wide")
st.markdown("<h1 style='text-align: center; color:gray;'>LANGUAGE TRANSLATION </h1>", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_ph = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_qfbae4sb.json")


with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("WELCOME TO LANGUAGE TRANSLATION ARENA:wave:")
        st.write("This website is built by Arya Mangdare and Sneha Nandedkar using the AI application of voice capturing");
        st.write(
        "ABOUT THIS PROJECT:We made a voice translation web application which carries out the process of translation of one language to other.In this project the user may speak in english "
        "Microphone of the device will get turned on and capture the voice of user. The captured sentence will be shown which then will ask the user ,the language in which is wants to translate the language. Then the user is expected to call out the language, again the microphone will capture the wordings "
        "and will convert the same sentence into requested language and will be displayed on the screen.");
        st.write("---")
    with right_column:
        st_lottie(lottie_ph,height=300)
    # st.write("[learn more>](https://www.geeksforgeeks.org/flask-creating-first-simple-application/)")

url1='https://www.geeksforgeeks.org/flask-creating-first-simple-application/'
if st.button('start translation'):
    webbrowser.open_new_tab(url1)

     #displayed when the button is clicked

else:

    st.markdown("<h1 style='text-align: center;font-size:30px; color:pink;'>A DIFFERENT LANGUAGE IS A DOORWAY TO DIFFERENT WORLD  </h1>", unsafe_allow_html=True)#displayed when the button is unclicked
