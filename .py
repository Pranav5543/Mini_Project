import random
import smtplib
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyjokes
import os

# Initialize the voice engine once
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("The command is:", query)
    except Exception as e:
        print(e)
        print("Say that again, please.")
        return "None"

    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your-email@gmail.com', 'your-password')
        server.sendmail('your-email@gmail.com', to, content)
        server.close()
        speak("Email has been sent successfully.")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send the email.")

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    day_of_the_week = Day_dict.get(day, "Unknown day")
    print(day_of_the_week)
    speak("The day is " + day_of_the_week)

def tellTime():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

def Hello():
    speak("Hello sir, I am your desktop assistant. Tell me how may I help you.")

def Take_query():
    Hello()

    while True:
        query = takeCommand().lower()

        if "open chrome" in query:
            speak("Opening Chrome")
            webbrowser.open("www.google.com")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
        elif "which day is it" in query:
            tellDay()
        elif "tell me the time" in query:
            tellTime()
        elif "bye" in query:
            speak("Bye! Hope you had a good time.")
            break
        elif "from wikipedia" in query:
            speak("Checking Wikipedia")
            query = query.replace("from wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            speak(result)
        elif "tell me your name" in query:
            speak("I am Banti, your desktop Assistant.")
        elif "tell a joke" in query:
            speak(pyjokes.get_joke())
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")
        elif "open command prompt" in query:
            speak("Opening Command Prompt")
            os.system("start cmd")

if __name__ == "__main__":
    Take_query()
