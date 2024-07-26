#voice assistant using python

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
#import pyaudio
import os
import time

def sptext():
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not Understanding.....")

def speechtext(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "hello sam" in sptext().lower():
        while True:
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is Kiran Parmar"
                speechtext(name)

            elif "old are you" in data1:
                age = "i am twenty nine years old"
                speechtext(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtext(time)

            elif 'youtube' in data1:
                webbrowser.open("https://youtube.com/")

            elif "joke" in data1:
                joke_1  = pyjokes.get_joke(language="en",category="all")
                print(joke_1)
                speechtext(joke_1)

            elif "play song" in data1:
                add = "D:\sd card mom\MUSI"
                listsong = os.listdir(add)
                print(listsong)
                index = int(input("Enter number of song to play: "))
                os.startfile(os.path.join(add,listsong[index]))

            elif "exit" in data1:
                speechtext("thank you")
                break

            time.sleep(10)
    else:
        print("Thanks")