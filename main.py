import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pyautogui import click
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am mini Sir!,Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('asakshin2@gmail.com', 'Sakshin@0208')
    server.sendmail('asakshin2@gmail.com', to, content)
    server.close()

def onlineClass():

        link = "https://meet.google.com/fvx-xbgr-zgr"
        webbrowser.open(link)
        sleep(10)
        click(x=614, y=810)
        sleep(2)
        click(x=718, y=807)
        sleep(1)
        click(x=1358, y=604)
        sleep(5)

def mute():
    click(x=783, y=1019)

def video():
    click(x=848, y=1021)

def endCall():
    click(x=1118, y=1019)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
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
            webbrowser.open("https://www.google.co.in/")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/")


        elif 'play music' in query:
            music_dir = 'D:\Hindi hits\Aashaqui 2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to team' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "venkyshettyydg@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")


        elif 'online' in query:
            onlineClass()

        elif 'mute' in query:
            mute()

        elif 'unmute' in query:
            mute()

        elif 'video' in query:
            video()

        elif 'off video' in query:
            video()

        elif 'disconnect' in query:
            endCall()

        elif 'bye' in query:
            speak("Have a good time sir, always at your service!")
            break