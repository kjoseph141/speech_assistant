import speech_recognition as sr
import time
from time import ctime
import webbrowser
import pyttsx3 as tts 


# Initialize speech_recognition recognizer
rec = sr.Recognizer()
engine = tts.init()
voice_selection = engine.getProperty('voices')[7]
engine.setProperty('voice', voice_selection.id)


def record(ask=False):
    """
    Records voice using default microphone and returns voice as text

    Args:
        ask (bool, optional): [Additional question to prompt user]. Defaults to False.

    Returns:
        [string]: [text from recording voice]
    """

    with sr.Microphone() as source:
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=1)

        if ask:
            engine.say(ask)
            engine.runAndWait()
            
        audio = rec.listen(source,)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print('No valid command detected. Waiting for command...')
            
        except sr.RequestError:
            engine.say('Sorry, I\'m not working right now')
            engine.runAndWait()
            

    return voice_data


def respond(voice_data):
    """
    Detemines the command and responds with specific actions and replies

    Args:
        voice_data ([text]): [text from recording of user's voice]
    """

    if ('OK Mac' in voice_data) or ('hey Mac' in voice_data):
        engine.say('Hi, how can I help?')
        engine.runAndWait()

    if 'what is your name' in voice_data:
        engine.say('My name is Mac. What\'s your name?')
        engine.runAndWait()
        name = record()
        engine.say('Hi ' + name + '. How can I help you?')
        engine.runAndWait()

    if 'how are you' in voice_data:
        engine.say('I\'m well, thank you. How are you?')
        engine.runAndWait()
        response = record()
        if ('well' in response) or ('good' in response):
            engine.say('I\'m glad to hear that. How can I help you?')
            engine.runAndWait()
        elif ('bad' in response) or ('not' in response):
            engine.say('Sorry to hear that. How can I help you today?')
            engine.runAndWait()
        else:
            engine.say('Ok. How can I help you?')
            engine.runAndWait()

    if 'what can you' in voice_data:
        engine.say('I can do a few basic things like tell you the time and date, search on Google or YouTube, open new tabs, or find directions.')
        engine.runAndWait()
        
    if 'what time' in voice_data:
        engine.say(ctime()[11:-4])
        engine.runAndWait()
        
    if 'what is the date' in voice_data and (not ('tomorrow' in voice_data)):
        engine.say(ctime()[0:11])
        engine.runAndWait()
        
    if 'search' in voice_data and (not ('YouTube' in voice_data)):
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

    if 'YouTube' in voice_data:
        search = record('What do you want to search on YouTube?')
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
        engine.say('Here is what I found for ' + search)
        engine.runAndWait()

    if 'open tab' in voice_data:
        webbrowser.open_new_tab('https://google.com/')
        
    if 'stop' in voice_data:
        engine.say('Switching off')
        engine.runAndWait()
        exit()


time.sleep(1)
engine.say('Hi, how can I help?')
engine.runAndWait()

# Runs indefinitely on loop
while 1:
    voice_data = record()
    respond(voice_data)