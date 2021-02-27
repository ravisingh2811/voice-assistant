
from math import exp
from sys import api_version
import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
import time
from twilio.rest import Client
import wolframalpha
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium import webdriver
from time import sleep, strftime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Dimpal sir. Please tell me how can I help you")    
def takeCommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio ,  language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say this  again please")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("kinetic2811@gmail.com" , "kumar2811")
    server.sendmail("rk250020@gmail.com" , to , content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "who" in query:
            speak("Searching Wikipedia...")
            query = query.replace("who" , "")
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open google maps" in query:
            webbrowser.open("https://www.google.com/maps")  
        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif"desltop" in query:
            winshell.desktop()
            speak("opening desktop")
        
        elif "play music" in query or "play song" in query:
                speak("Here you go with music")
                music_dir = 'F:\\songs'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                print(random)
                playsound.playsound(random)
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strTime}")   


        elif "open" in query.lower():
    
                if "chrome" in query.lower():
                    path =  r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)
                    speak(f"Opening Google Chrome")
                elif"visual studio code" in query.lower():
                    path =  r"C:\\Program Files (x86)\\Microsoft Visual Studio\\Installer\\vs_installer.exe"
                    os.startfile(path)
                    speak(f"Opening Visual studio code")
                elif"dev" in query.lower():
                    path =  r"C:\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
                    os.startfile(path)
                    speak(f"Opening Dev C++")        
                elif" telegram" in query.lower():
                    path =  r"C:\\Users\\hp\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                    os.startfile(path)
                    speak(f"Opening telegram")
                    
                elif"chat box" in query.lower():
                    path =  r"C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    os.startfile(path)
                    speak(f"Opening whatsApp")


        elif"send mail" in query:
            try:
               speak("what should I say?")
               content = takeCommand()
               to = ("rk250020@gmail.com")
               sendEmail(to , content)
               speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry i can't send this email")
        elif "joke" in query:
            joke = pyjokes.get_jokes()
            speak(f"here you go{joke}")
            print(speak)
        elif "exit" in query or "stop" in query or "quit" in query:
            exit()
