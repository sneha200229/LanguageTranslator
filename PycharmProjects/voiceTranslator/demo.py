
import streamlit
import streamlit as st
from altair.vega import background

# from audio_recorder_streamlit import audio_recorder
# import recorder as recorder

#displaying an audio from local system in the streamlit app
st.set_page_config(page_title="voice translation",page_icon=":tada:",layout="wide")
st.markdown("<h1 style='text-align: center; color:gray;'>LANGUAGE TRANSLATION </h1>", unsafe_allow_html=True)

st.sidebar.title("YOU WILL BE HEARING THE CAPTURED VOICE")
st.write("INPUT SENTENCE")
audio1=open('lang.wav','rb')
audio_bytes1= audio1.read()
st.audio(audio_bytes1, format='audio/ogg')
st.divider()
st.write("INPUT LANGUAGE")
audio1=open('input.wav','rb')
audio_bytes1= audio1.read()
st.audio(audio_bytes1, format='audio/ogg')
st.divider()

st.write("OUTPUT GENERATED")
audio_file = open('captured_voice.mp3','rb') #enter the filename with filepath
audio_bytes = audio_file.read() #reading the file
st.audio(audio_bytes, format='audio/ogg') #displaying the audio
