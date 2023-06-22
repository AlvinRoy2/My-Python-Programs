import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia  
import pyjokes
listner=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'Jarvis' in command:
                command=command.replace('Jarvis','')
                #print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing....'+song)
        print('Song.')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strptime("%I:%M %p")
        talk("Current Time is"+time)
    elif 'who is' in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person)
        talk(info) 
    elif 'joke'  in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please tell the command again")
        
while True:
    run_alexa()