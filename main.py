import speech_recognition as sr
import time
from time import ctime
import webbrowser


rec = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I didn\'t get that')
        except sr.RequestError:
            print('Sorry, I\'m not working right now')

    return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Mac')
    if 'what time' in voice_data:
        print(ctime()[11:])
    if ('what date' or 'what date today') in voice_data:
        print(ctime()[0:11])
    if 'search' in voice_data:
        search = record('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'directions' in voice_data:
        start = record('Where do you want directions from?')
        start_search = start.replace(' ', '+')
        end = record('Where do you want directions to?')
        end_search = end.replace(' ', '+')
    
        url = 'https://www.google.com/maps/dir/' + start_search + '/' + end_search
        webbrowser.get().open(url)
        print('Here are directions from ' + start + ' to ' + end)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
print('Hi, how can I help?')
while 1:
    voice_data = record()
    respond(voice_data)