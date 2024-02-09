import pyttsx3
import command
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def translation():      
    
    n = 1
    speak("which language I translate Sir..")
    while n==1:
        query = command.take_command().lower()   
         
        if 'in spanish' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='es')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in bengali' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='bn')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in french' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='fr')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in malayalam' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ml')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in marathi' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='mr')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in punjabi' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='pn')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in tamil' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ta')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in telugu' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='te')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in urdu' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ur')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in russian' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ru')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in marathi' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='mr')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in nepali' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ne')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in latin' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='la')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in hindi' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='hi')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in german' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='de')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in gujarati' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='gu')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in italian' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='it')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in korean' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='ko')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in english' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='en')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in greek' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='el')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1

        elif 'in chinese' in query:
            speak("tell me a setence for translating")
            sentence = command.get_command_translator()
            translator = Translator()
            translated_sentence = translator.translate(sentence,src='en',dest='zh-cn')
            print(translated_sentence.text)
            speak(translated_sentence.text)
            n=1
        
        elif 'exit' in query:
            speak("ok sir. I am closing translator")
            n = 2
