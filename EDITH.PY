from ast import main
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from AppOpener import run
import smtplib
from tkinter import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon!')

    else:
        speak('Good Evening!')

    speak('I am EDITH sir. Please tell me how may i help you')


def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        

        print('Say That Again Please.....')
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("arjunparvatha@gmail.com", "Mummy111")
    server.sendmail("arjunparvatha@gmail.com", to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
       query = takeCommand().lower()
      #logic for executing tasks based on query
       if 'wikipedia' in query:
          speak('Searching Wikipedia.....')
          query = query.replace('Wikipedia', '')
          results = wikipedia.summary(query, sentences = 1)
          speak("According to Wikipedia")
          print(results)
          speak(results)
        
       elif "open youtube" in query:
         webbrowser.open("youtube.com")

       elif "open google" in query:
         webbrowser.open("google.com")

       elif "open stackoverflow" in query:
         webbrowser.open("stackoverflow.com")


       elif "play music" in query:
         music_dir = "D:\\Non Critical\\songs\\Favourite Songs2"
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

       elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the Current Time is {strTime}")


       elif "open code" in query:
            codePath = "C:\\Users\\MAITHILI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


       elif "open netflix" in query:
            run("netflix")

        
       elif "open whatsapp" in query:
            run("whatsapp")


       elif "open instagram" in query:
            run("instagram")


       elif "email to arjun" in query:
           try:
              speak( "what should i say?")
              content = takeCommand()
              to = "arjunparvatha@gmail.com"
              sendEmail(to, content)
              speak("Email has been Sent!")
           except Exception as e:
                print(e)
                speak("Sorry the Email Could Not Get Sent!")


            

























        


         





          



