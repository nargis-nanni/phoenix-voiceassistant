import subprocess
# import wolframalpha
import pyttsx3
# import tkinter 
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
# from twilio.rest import Client
# from clint.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning nargis !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon nargis !")   
  
    else:
        speak("Good Evening nargis !")  
  
    assname =("Verona 1 point o")
    speak("I am your Assistant")
    speak(assname)

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query


if __name__ == '__main__':
    clear = lambda: os.system('cls')    


    clear()
    wishMe()
    takeCommand() 

    while True:
       
        query = takeCommand().lower()



        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   



        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\91971\\OneDrive\\Desktop\\your dad"
            songs = os.listdir(music_dir)
            print(songs)    
            random = os.startfile(os.path.join(music_dir, songs[0]))    


        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                     
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "hey verona" in query:
             
            wishMe()
            # speak("Jarvis 1 point o in your service Mister")
            speak("yes sir")
            # speak(assname)
     
        elif "aaj ka weather" in query:
                 
            # Google Open weather website
            # to get API of Open weather 
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")


        elif "i love you" in query:
            speak("It's hard to understand")        

        elif 'open python 3.9.0' in query:
            speak("Here you go to python 3.9.0\n")
            Desktop.open("IDLE (Python 3.9 64-bit)")
     