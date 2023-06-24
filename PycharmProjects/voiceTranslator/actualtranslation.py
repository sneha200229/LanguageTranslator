import webbrowser

import speech_recognition
# https://www.google.com/search?q=how+to+use+streamlit+audio&rlz=1C1CHZN_enIN1043IN1043&oq=how+to+use+streamlit+audio&aqs=chrome..69i57j33i160.5506j0j7&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:658421f6,vid:Y9riYFzFeOs
# https://www.projectpro.io/recipes/display-audio-streamlit





import streamlit as st
import requests
from numpy.distutils.fcompiler import none
from streamlit_lottie import st_lottie
import numpy as np
from pydub import AudioSegment

import speech_recognition as sr
recog=sr.Recognizer()
st.set_page_config(page_title="voice translation",page_icon=":tada:",layout="wide")
st.markdown("<h1 style='text-align: center; color:gray;'>LANGUAGE TRANSLATION </h1>", unsafe_allow_html=True)
audio=st.file_uploader("uploaded here",type=['mp3','wav'])
if audio:
    audio_segment = AudioSegment.from_file(audio)
    print(audio_segment)
    # chunks=silence.split_on_silence(audio_segment,min_silence_len=500,silence_thresh=audio_segment.dBFS-20,keep_silence=100)
    # for index,chunk in enumerate(chunks):
    #     chunk.export(str(index)+".wav",format="wav")
    #     with sr.AudioFile(str(index)+".wav") as source:
    #         recorded=recog.record(source)
    #         try:
    #             text=recog.recognize_google(recorded)
    #             print(text)
    #         except:
    #             print(none)

