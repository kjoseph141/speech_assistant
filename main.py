import speech_recognition as sr
import time
from time import ctime
import webbrowser
import pyttsx3 as tts
import playsound
import os
import random
from gtts import gTTS


rec = sr.Recognizer()



def record(ask=False):

    with sr.Microphone() as source:

        rec.pause_threshold = 1.0
        rec.adjust_for_ambient_noise(source, duration=1)

        if ask:
            speak(ask)
            
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            speak('Sorry, I didn\'t get that')
            
        except sr.RequestError:
            speak('Sorry, I\'m not working right now')
            

    return voice_data


def speak(audio_text):
    text_to_speech = gTTS(audio_text)
    rand_num = random.randint(1, 100000)
    audio_file_name = 'audio_file_' + str(rand_num) + '.mp3'
    text_to_speech.save(audio_file_name)
    playsound.playsound(audio_file_name)
    print(audio_text)
    os.remove(audio_file_name)


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Mac')

    if 'how are you' in voice_data:
        speak('I\'m well, thank you. How are you?')
        response = record()
        if 'well' or 'good' in response:
            speak('I\'m glad to hear that. How can I help you?')
        elif 'bad' or 'not' in response:
            speak('Sorry to hear that. How can I help you today?')
        else:
            speak('Ok. How can I help you?')

    if 'what can you' in voice_data:
        speak('I can do a few basic things like tell you the time and date, search the internet, or find directions.')
        
    if 'what time' in voice_data:
        speak(ctime()[11:])
        
    if 'what is date' in voice_data:
        speak(ctime()[0:11])
        
    if 'search' in voice_data:
        search = record('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
        
    if 'directions' in voice_data:
        start = record('Where do you want directions from?')
        start_search = start.replace(' ', '+')
        end = record('Where do you want directions to?')
        end_search = end.replace(' ', '+')
        url = 'https://www.google.com/maps/dir/' + start_search + '/' + end_search
        webbrowser.get().open(url)
        speak('Here are directions from ' + start + ' to ' + end)
        
    if 'stop' in voice_data:
        exit()


time.sleep(1)
speak('Hi, how can I help?')

while 1:
    voice_data = record()
    respond(voice_data)