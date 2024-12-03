import pydub
import pytube 
from pytube import YouTube

from pydub import AudioSegment
import pygame

# Function to play music directly from YouTube
def play_music_online(video_url):
    # Create a YouTube object
    video = YouTube(video_url)

    # Get the audio stream
    audio_stream = video.streams.filter(only_audio=True).first()

    # Get the audio URL
    audio_url = audio_stream.url

    # Create an AudioSegment object
    audio = AudioSegment.from_file(audio_url)

    # Initialize pygame and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    pygame.event.wait()

# Replace 'your_video_url' with the actual video URL
play_music_online('https://youtu.be/EMNNoqjY1Jo?si=qLNt6rx1kqcwmsSd')
