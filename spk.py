from gtts import gTTS
import os
from googletrans import Translator

def speak_text_in_hindi():
    while True:
        # Get input from the user in English
        text = input("Type something in English (type 'exit' to stop): ")

        # Check if the user wants to exit
        if text.lower() == 'exit':
            break

        # Translate the English text to Hindi
        translator = Translator()
        translated_text = translator.translate(text, dest='hi').text

        # Create a gTTS object
        tts = gTTS(translated_text, lang='hi')

        # Save the speech as a temporary file
        tts.save("temp.mp3")

        # Play the speech
        os.system("start temp.mp3")

# Call the function to speak text in Hindi
speak_text_in_hindi()
