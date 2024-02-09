import pyttsx3
import command
import datetime
import wikipedia
import music
import os
import subprocess
import translator
import pyautogui
import time
import shutil
import wolframalpha
import ctypes
import pyjokes
import winshell
import webbrowser

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    columns = shutil.get_terminal_size().columns
    print("\n")
    print("..........  WELCOME  ..........".center(columns))
    print("\n")

# wish me
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12 :
        speak("Good morning")

    elif hour>=12 and hour<=16 :
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am JARVIS sir. Please tell me how may I help you")

if __name__ == "__main__":

    welcome()
    wishMe()
    while True:

        query = command.take_command().lower()

        if 'wikipedia' in query:
            speak("Searching wikipidea...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            print(results)
            speak(results)
         
        # CHATS 
        elif 'hello jarvis' in query:
            speak("hello sir!")

        elif 'your name' in query:
            speak("My name is jarvis")

        elif 'who are you' in query:
            speak("I am a fictional artificial intelligence")

        elif 'how are you' in query:
            speak("I'm fine and how are you")
            hs = command.take_command()
            if 'fine' in hs or 'good' in hs:
                speak("Good sir")

        elif 'jarvis you are so intelligent' in query:
            speak("thank you sir..")

        elif 'are you married' in query:
            speak("I'm happily single")

        elif 'you listen me' in query:
            speak("Yes Sir, I am listening you")

        elif 'who made you' in query:
            speak("Manjeet sir has made me")
        
        elif 'bye' in query:
            speak("bye sir")
            exit()

        elif 'good night' in query:
            speak("Good Night Sir")
            os.system("taskkill /im Code.exe")

        # TIME
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        # YOUTUBE
        
        elif "open youtube" in query:
            speak("ok sir! i am opening youtube... Please wait")
            webbrowser.open("youtube.com")
            speak("Opened")

        elif "close youtube" in query:
            os.system("taskkill /im iexplore.exe /f")
        
        # GOOGLE
        
        elif "open google" in query:
            speak("ok sir! i am opening google... Please wait")
            webbrowser.open("google.com")

        elif "close google" in query:
            os.system("taskkill /im iexplore.exe /f")

        # STACKOVERFLOW
        
        elif "open stackoverflow" in query:
            speak("ok sir! i am opening stackoverflow... Please wait")
            webbrowser.open("stackoverflow.com")

        elif "close stackoverflow" in query:
            os.system("taskkill /im iexplore.exe /f")

        # GAMETOP
        
        elif 'open gametop' in query:
            speak("ok sir! i am opening gametop... Please wait")
            webbrowser.open("gametop.com")

        elif "close gametop" in query:
            os.system("taskkill /im iexplore.exe /f")
        
        # System Command and various other command
        
        elif 'lock window' in query:
            speak("locking the device") 
            ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
            speak("Hold On a Sec ! Your system is on its way to shut down") 
            subprocess.call('shutdown / p /f') 
                  
        elif 'clean recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Cleaned , Sir") 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 

        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = 20
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("User asked to Locate") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
        
        # Search in laptop       
        
        elif 'find in laptop' in query:
            speak("what is find and open , Sir")
            f = command.take_command().lower()
            pyautogui.press('win',interval=0.2)
            pyautogui.typewrite(f,interval=0.4)
            pyautogui.press('enter',interval=0.4)

        # Search in google           
        
        elif 'search' in query : 
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)
        
        # VS CODE
        
        elif 'open code' in query:
            speak("ok sir! i am opening V S code")
            code_path = "C:\\Users\\Ranjeet kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'close code' in query:
            os.system("taskkill /im Code.exe")

        # NOTEPAD
        
        elif 'open notepad' in query:
            speak("ok sir! i am opening notepad")
            notepad_path = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(notepad_path)
            speak("do you want to write Sir ")
            n = 1
            while n==1:
                text = command.take_command()
                if 'yes' in text:
                    speak("What do I write sir")
                    w = command.get_command_writing()
                    pyautogui.typewrite(w)
                    speak("I've write of that")
                    speak("Anything you want to write again, Sir")
                else:
                    speak("ok Sir")
                    n = 2

        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = command.get_command_writing()
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = command.take_command() 
            if 'yes' in snfm or 'sure' in snfm:  
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif 'show note' in query:
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(30))
            s1=2

        elif 'close notepad' in query:
            os.system("taskkill /im notepad.exe")

        
        # MS OFFICE EXCEL
        
        elif 'open excel' in query:
            speak("ok sir! i am opening excel")
            excel_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\EXCEL.exe"
            os.startfile(excel_path)
            
        elif 'close excel' in query:
            os.system("taskkill /im EXCEL.exe")

        # MS OFFICE WORD
        
        elif 'open word' in query:
            speak("ok sir! i am opening M S word")
            word_path = "C:\\Program Files\\Microsoft Office\\Office12\\WINWORD.exe"
            os.startfile(word_path)
            speak("do you want to write Sir ")
            y = 1
            while y==1:
                text = command.take_command()
                if 'yes' in text:
                    speak("What do I write sir")
                    a = command.get_command_writing()
                    pyautogui.typewrite(a)
                    speak("I've write of that")
                    speak("Anything you want to write again, Sir")
                else:
                    speak("ok Sir")
                    y = 2

        elif 'close word' in query:
            os.system("taskkill /im WINWORD.exe")

        # MS PAINT
        
        elif 'open paint' in query:
            speak("ok sir! i am opening paint")
            paint_path = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(paint_path)

        elif 'close paint' in query:
            os.system("taskkill /im mspaint.exe")

        # MS OFFICE POWERPOINT
        
        elif 'open powerpoint' in query:
            speak("ok sir! i am opening power point")
            ppt_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\POWERPNT.exe"
            os.startfile(ppt_path)

        elif 'close powerpoint' in query:
            os.system("taskkill /im POWERPNT.exe")
        
        # MUSIC

        elif 'play music' in query:
            music.songs()
        
        # SEARCHING
        
        elif "what is" in query or "who is" in query: 
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("JW6Y7Q-GKWVR76AJG") 
            res = client.query(query) 
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 

        # TRANSLATOR

        elif 'open translator' in query:
            translator.translation()