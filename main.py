import speech_recognition as sr
import time
from time import ctime
import webbrowser
import pyttsx3 as tts 


rec = sr.Recognizer()
engine = tts.init()
voice_selection = engine.getProperty('voices')[7]
engine.setProperty('voice', voice_selection.id)



def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            engine.say(ask)
            engine.runAndWait()
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            engine.say('Sorry, I didn\'t get that')
            engine.runAndWait()
        except sr.RequestError:
            engine.say('Sorry, I\'m not working right now')
            engine.runAndWait()

    return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        engine.say('My name is Mac')
        engine.runAndWait()
    if 'what time' in voice_data:
        engine.say(ctime()[11:])
        engine.runAndWait()
    if (('what is the date' or 'what date is today') in voice_data) and not('tomorrow' or 'yesterday' in voice_data):
        engine.say(ctime()[0:11])
        engine.runAndWait()
    if 'search' in voice_data:
        search = record('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        engine.say('Here is what I found for ' + search)
        engine.runAndWait()
    if 'directions' in voice_data:
        start = record('Where do you want directions from?')
        start_search = start.replace(' ', '+')
        end = record('Where do you want directions to?')
        end_search = end.replace(' ', '+')
    
        url = 'https://www.google.com/maps/dir/' + start_search + '/' + end_search
        webbrowser.get().open(url)
        engine.say('Here are directions from ' + start + ' to ' + end)
        engine.runAndWait()
    if 'stop' in voice_data:
        exit()


time.sleep(1)
engine.say('Hi, how can I help?')
engine.runAndWait()
while 1:
    voice_data = record()
    respond(voice_data)