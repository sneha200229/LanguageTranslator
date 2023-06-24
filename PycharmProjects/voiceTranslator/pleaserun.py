# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr#module
from googletrans import Translator
from gtts import gTTS
import os #module


flag = 0

# A tuple containing all the language and
# codes of the language will be detcted
dic = ('afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')


# Capture Voice
# takes command through microphone

def takecommandagain():
    r=sr.Recognizer() #object of recognizer class from sr module
    with sr.Microphone() as source:#ensure audio is taken from mic
        print("listening..(speak what you want to translate)")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1 #
        audio1=r.listen(source, phrase_time_limit=5)
        with open('lang.wav','wb') as f:
            f.write(audio1.get_wav_data())#used to write raw datain wav format to auio1 file
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio1, language='en-in')
        print(f"The User said {query}\n")

    except Exception as e:
        print("say that again please.....")
        return "None"
    return query




def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=5)
        with open('input.wav','wb') as f:
            f.write(audio.get_wav_data())
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User chose language {query}\n")

    except Exception as e:
        print("say that again please.....")
        return "None"
    return query




# Input from user
# Make input to lowercase
query = takecommandagain()
while (query == "None"):
    query = takecommandagain()


def destination_language():
    print("Enter the language in which you\
	want to convert : Ex. Hindi , English , etc.")
    print()

    # Input destination language in
    # which the user wants to translate
    to_lang = takecommand()


    while (to_lang == "None"):
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang


to_lang = destination_language()

# Mapping it with the code
while (to_lang not in dic):
    print("Language in which you are trying\
	to convert is currently not available ,\
	please input some other language")
    print()
    to_lang = destination_language()

to_lang = dic[dic.index(to_lang) + 1]

# invoking Translator
translator = Translator() #creating translator object

# Translating from src to dest
text_to_translate = translator.translate(query, dest=to_lang)#translate method of translator ogject
# to translate from one language to other

text = text_to_translate.text#The translate method returns a Translated object that
# contains the translated text. You can access the translated text using the text attribute of the Translated object

# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly


speak = gTTS(text=text, lang=to_lang, slow=False)#generates audio files from text strings
#Create a gTTS object: Create a gTTS object by passing the text you want to convert to speech as a parameter.

# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')

# Printing Output
print(text)
