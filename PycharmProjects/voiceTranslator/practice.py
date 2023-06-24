from fnmatch import translate

import streamlit as st
# from playsound import playsound
# import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
from google_trans_new import google_translator

# from googletrans import Translator
# from gtts import gTTS
# import os


audio_bytes = audio_recorder()
if audio_bytes:
    st.write("recording")
    st.audio(audio_bytes, format="audio/wav")
translator = google_translator()
translate_audio = translator.translate(audio_bytes,lang_tgt='fr')
st.write(translate_audio)


#
# flag = 0
# dic = ('afrikaans', 'af', 'albanian', 'sq','amharic', 'am', 'arabic', 'ar','armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be',
#        'bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)','zh-cn', 'chinese (traditional)',
#        'zh-tw', 'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo',
#        'estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german',
#        'de', 'greek', 'el', 'gujarati', 'gu', 'haitian creole', 'ht', 'hausa', 'ha', 'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
#        'hi', 'hmong', 'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian', 'id', 'irish', 'ga', 'italian',
#        'it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)',
#        'ku', 'kyrgyz', 'ky', 'lao', 'lo', 'latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb',
#        'macedonian', 'mk', 'malagasy', 'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
#        'mn', 'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa',
#        'polish', 'pl', 'portuguese', 'pt', 'punjabi',  'pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd',
#        'serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl',
#        'somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
#        'te', 'thai', 'th', 'turkish', 'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 'uz',
#        'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')
#
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.write("listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source)



# a=st.number_input("enter first number")
# b=st.number_input("enter second number")
# n=10
# for i in range(1,11):
#     st.write(i)



