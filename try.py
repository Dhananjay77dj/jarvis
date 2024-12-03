import pyttsx3
import speech_recognition

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)  # Adjust this value as needed
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Use the Hindi voice

def speak():
    while True:
        audio = input("Enter something in Hindi: ")
        engine.say(audio)
        engine.runAndWait()

speak()


