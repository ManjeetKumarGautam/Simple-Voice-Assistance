import os
import time
import command
import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def songs():
    # music_dir is hold a file location where musics is present. In the below you can see the file location " \\Music\\". 
    music_dir = "\\Music\\"
    song = os.listdir(music_dir)
    print(song)
    speak("Are you sure Sir")
    while True:                
        ms = command.take_command()
        if 'yes' in ms:
            speak("which song I play ,Sir")
            m = command.get_command_music().lower()
            speak("ok sir! i am playing"+ m +"music")
            os.startfile("\\Music\\"+m+".mp3")
            time.sleep(60)
            speak("Sir,Am I playing next song sir?")
        elif 'no' in ms:
            speak("ok sir..")
            break
