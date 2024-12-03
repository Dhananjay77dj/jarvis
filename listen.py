import speech_recognition as sr
from googletrans import Translator
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    # r = sr.Microphone()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.... ')
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language="hi")
    except:
        return
    query = str(query).lower()

    return query
# print(listen())

def translator(text): #convert hindi to english

   line = str(text)
   translate = Translator()
   result = translate.translate(line)
   data = result.text
   print(f'You : {data}')
   return data
def micexecution():
    query = listen()
    data = translator(query)
    return data
micexecution()