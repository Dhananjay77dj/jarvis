import speech_recognition as sr
import pyttsx3
import os
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

def time():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('good morning sir')
    elif 12 <= hour <=16:
        speak('good afternoon boss')
    else:
        speak('good evening boss')
    speak('It\'s jarvis')
# def sendemail(to,content):


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
def time2():
    t= datetime.datetime.now().strftime("%H:%M")
    speak(f"the time is {t}")
    print(t)




if __name__ == "__main__":
    # speak('hi how are you')
    time()
    while True:
        query = command().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak("ACCORDING TO WIKIPEDIA")
            print(results)
            speak(results)
        elif 'open youtube' in query:  # Remove the space before and after "youtube"
            
            youtube_url = "https://www.youtube.com"
            
            speak('opening youtube')
                
            webbrowser.open(youtube_url)

    
        elif 'gpt' in query:
            webbrowser.open('https://chat.openai.com/?model=text-davinci-002-render-sha')
        elif 'open notepad' in query:
            subprocess.run('notepad.exe')
        elif 'open google' in query:  # Remove the space before and after "google"
            speak('opening google')
        
            webbrowser.open('https://www.google.com')
        elif 'system off' in query:
          os.system("shutdown /s /t 1")
              
        
        elif 'open cmd' in query:
            subprocess.run("start cmd", shell=True)

        elif 'open chess' in query:
          speak('opening youtube')
          url = 'https://www.chess.com/home'
        
          
          webbrowser.open(url)        
        
        elif 'the time' in query:
            time2()

        elif 'shutdown' in query:
            break