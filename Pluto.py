from gtts import gTTS
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
from pygame import mixer
import smtplib
import os
import time


def speak(audio):
    print(audio)
    text_to_speech = gTTS(text=audio, lang='en-uk')
    text_to_speech.save('audio.mp3')
    mixer.init()
    mixer.music.load("audio.mp3")
    mixer.music.play()
    time.sleep(len(audio)//10)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am PLUTO. Please tell me how may I help you?")       


def takeCommand(): 
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
        time.sleep(2)

    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = takeCommand()

    return command


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:

        command = takeCommand().lower()


        if 'hello' in command:
            speak('Hello! I am PLUTO. How can I help you?')

        elif "what can you do" in command:
            speak("I can search things, play music, open websites, send email, search for your query, and many more....")

        elif 'who are you' in command:
            speak('I am your Virtual Assistant...')

        elif 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open wikipedia' in command:
            webbrowser.open("wikipedia.com")

        elif 'open youtube' in command:
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com") 
        
        elif 'play music' in command:
            music_dir = '/home/reeha/Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.path.join(music_dir, songs[0])

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'email to' in command:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = command.replace("email to ","")
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("error while sending email...")
        
        elif 'bye' in command or 'quit' in command:
            speak("I hope you like my assistance... Have a nice day!")
            break

        elif "repeat" in command or "speak" in command:
            speak(command)


