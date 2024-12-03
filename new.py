import speech_recognition as sr
import pyttsx3
import wikipedia
import subprocess
import pyautogui
import time

import webbrowser
import datetime

# dic = {'me':'trivedidhananjay000@gmail.com','me2':'dhananjaytrivedi18@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.... ')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')
        return query
    except Exception as e:
        print(e)
        print('say this again please.....')
        return 'None'
    
    
if __name__ == "__main__":
    # speak('hi how are you')
    # time()
    while True:
        query = command().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=10)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)
            speak(results)
        elif 'gpt' in query:
            webbrowser.open('https://www.youtube.com')