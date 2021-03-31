import subprocess
import wolframalpha
import pyttsx3
# import tkinter 
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as kit
import os
import cv2
import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import shutil
import requests
import pyautogui
from  requests import get
# from twilio.rest import Client
# from clint.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# email={'nargis':'nannikhan72@gmail.com','khushi':'kshabiya397@gmail.com','siddhart':'dna8377850@gmail.com','hanish':'hanish.arora8@gmail.com','pooja':'poojadayal434@gmail.com','poojadi':'poojanagar76@gmail.com','angy':'theinnovative@gmail.com','dinesh':'dkumar42358@gmail.com','roshidi':'loveayaan32@gmail.com','vishal':'vishalkumarkm3@gmail.com','abhishek':'abhi3phadi@gmail.com'
    
# def checker(key):
#     if key in email:
#         return email[key]
#     else:
#         return "please forgive me"

app = wolframalpha.Client("WG9854-5GT394LE6P")


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()
 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")   
  
    else:
        speak("Good Evening  !")  
  
    assname ='pheonix from karmmarg'
    speak("I am your  wonderful friend")
    speak(assname)


def usrname():
    speak("What should i call you ")        
    uname = takeCommand()
    speak("Welcome nargis ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome !" , uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you,")


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


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('nannikhan72@gmail.com','')
    server.sendmail('nannikhan72@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname() 
    
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be 
        # stored here in 'query' and will be
        # converted to lower case for easily 
        # recognition of command
   


        # elif 'send email' in qurey:
        #     try:
        #         speak("whom should i send email to")
        #         to = checker(takecommand().lower())
        #         speak("what should i say?")
        #         content=takecommand()
        #         speak("email has been send!")
        #         print("email has been send!")
        #         except Expecption as e:
        #         print(e)
        #         speak('i am not able to send this email sorry')

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #   login bulding for tasks


        if "open notepad" in query:
            npath = "C:\\windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        # elif 'open google' in query:
        #     speak("Here you go to Google\n")
        #     webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\HP\\OneDrive\\Desktop\\karm\\song"
            songs = os.listdir(music_dir)
            print(songs)    
            random = os.startfile(os.path.join(music_dir, songs[0]))
 
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")   
            speak(f" the time is {strTime}")
            print("the time is "+strTime)

        elif 'whats the temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)

        elif 'Calculater' in query:
            speak("what should i calculatre?")
            gh = takecommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)

        elif "open camera" in query:
            nar = cv2.Videocapture(0)
            while True:
                  cv2.inshow('camera,img')
                  k = cv2.waitkey(58)
                  if k==27:
                      break;
            nar.release()
            cv2.destroyAllwindows()      


        elif "ip address" in query:
            ip = get("https://api.ipify.org").text   
            speak(f"your IP address is {ip}") 
            print(f"your IP address is {ip} ")  


                  

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(1.3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i have done sir, the screenshot is saved in our main folder. Now i ready for next command")  

        # elif "open camera" in query:
        #     cap =cv2.videoCaptu(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow("webcam", img)
        #         k = cv2.waitkey(50)
        #         if k==27:
        #             break;
        #             cap.release()
        #             cv2.destroyALLWindows()

 
        # elif 'open opera' in query:
        #     codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        #     os.startfile(codePath)

        elif "volume down" in query:
            pyautogui.press("volume down")

        elif "volume mute" in query:
            pyautogui.press("volume mute")

        elif "volume up" in query:
            pyautogui.press("volume up")   


    

 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
 
        elif 'fine mine friend' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak('assname')
            print("My friends call me")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by nargis my friend.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'thank you mere doost' in query:
            speak ("it's my pleasure,mere doost")


     
        # elif "calculate" in query:   
        #     app_id = "Wolframalpha api id"
        #     client = wolframalpha.Client(app_id)
        #     indx = query.lower().split().index('calculate') 
            # query = query.split()[indx + 1:] 
            # res = client.query(' '.join(query)) 
            # answer = next(res.results).text
            # print("The answer is " + answer) 
            # speak("The answer is " + answer) 
 
        # elif 'search' in query or 'play' in query:
             
        #     query = query.replace("search", "") 
        #     query = query.replace("play", "")          
        #     webbrowser.open(query) 
 
        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to nargis. further It's a secret")

        elif "open google" in query:
            speak ("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "open youtube" in query:
            speak ("what should i search on youtube")
            na = takecommand().lower()
            webbrowser.open(f"{na}")    
 
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by my dear friend nargis")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by my dear friend nargis")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed succesfully")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
            try: 
                jsonObj = urlopen('''
 "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=dd99e5301ef942e0a2748194efc4ad40"
/ articles?source = the-times-of-india&sortBy = top&apiKey =: e85dd1afb43a49af92f061e607df6779''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /p")
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a=int(takeCommand())
            time.sleep(a)
            print(a)
 
        # elif "where is" in query:
        #     query = query.replace("where is", "")
        #     location = query
        #     speak("User asked to Locate")
        #     speak(location)
        #     webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak(" Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "pagal hai tu" in query:
            speak("show")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
            with open("Voice.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:
             
            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            speak('assname')
 
    
    
                
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "song on youtube" in query:
            kit.playonyt("see you again")    
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm oustanding!")
 
        elif "i love you" in query:
            speak("It's hard to understand")
 
        elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client()
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

# def sesver():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#       print("Bir sey de!")
#       audio = r.listen(source)
#     data = ""
#     try:
#       data = r.recognize_google(audio, language='tr-tr')
#       data = data.lower()
#       return data 
#        except ValueError:

