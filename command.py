import speech_recognition as sr

def take_command():
    #it take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio =  r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

# listening for written
def get_command_writing():
    h = sr.Recognizer()
    with sr.Microphone() as d:
        print("Listen For written.....")
        h.pause_threshold = 1
        audio =  h.listen(d)
    try:
        print("Recognizing what you say...")
        query = h.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def get_command_music():
    h = sr.Recognizer()
    with sr.Microphone() as d:
        print("Listening for music name... ")
        h.pause_threshold = 1
        audio =  h.listen(d)
    try:
        print("Recognizing...")
        query = h.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def get_command_translator():
    h = sr.Recognizer()
    with sr.Microphone() as d:
        print("Listening sentence for translate..... ")
        h.pause_threshold = 1
        audio =  h.listen(d)
    try:
        print("Recognizing...")
        query = h.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query
