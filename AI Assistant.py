import pyttsx3 
import speech_recognition as sr          
import datetime
import wikipedia 
import webbrowser 
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Savitha, Ma'am!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Savitha, Ma'am!")   

    else:
        speak("Good Evening Savitha, Ma'am!")  

    speak("i am Lisa, Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language="en-US")
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query


wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com/")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com/") 


    elif 'open dsu' in query:
        webbrowser.open("https://www.dsu.edu.in/")

    elif 'open gmail' in query:
        webbrowser.open("https://mail.google.com/")


    elif 'play music' in query:
        webbrowser.open('https://www.spotify.com/')

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"thanu, Sir, the time is {strTime}")
    elif 'google classroom' in query:
        webbrowser.open('https://classroom.google.com')