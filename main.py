import pip
import os
# from time import sleep
def import_or_install(package):  #function to check if module is installed or not installs module if not installed
    try:
        if package=="SpeechRecognition":
            import speech_recognition
            return
        if package=="gTTS":
            import gtts
            return
        if package == "pygame":
            os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        __import__(package)
    except:
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        __import__(package)
# import_or_install("pyttsx3")        #
import_or_install("pygame")         #
import_or_install("io")             #  use of above function
import_or_install("SpeechRecognition")  #
# import_or_install("pyaudio")            #
import_or_install("gTTS")
import pyttsx3              #reimport pyttsx3 for text to speech
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  #for hiding pygame welcome text
import pygame       #importing pygame for audio playback
from io import BytesIO  #importing bytesIO for creating object like files
import speech_recognition as sr #google speech recognition api
from gtts import gTTS
responses = {                                                   #dictionary for voice feedback
    "hello": "Hi there! I am Byte",
    "hi": "Hi there! I am Byte",
    "how are you": "I'm doing well, thank you.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! ",
    "exit": "Exiting... thank you for using byte",
    "nice":"thank you",
    "what can you do":"i am a basic bot just made for this demo you can ask me recommend an accessory for metaverse"
}
 
r=sr.Recognizer()
def res(user_i):
        if user_i in responses:
            return responses[user_i]
        else:
            return user_i
def speak(tospeak):
        if type(tospeak)==BytesIO :
            tospeak.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(tospeak)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
def generate(text):
        print("Bot : "+text)
        # engine =pyttsx3.init()
        # engine.setProperty('rate',180)
        # engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM')
        # engine.say(text)
        # engine.runAndWait()
        aout = BytesIO()
        tts = gTTS(res(text),lang='ta',tld='co.in')
        
        tts.write_to_fp(aout)
        speak(aout)

aout = BytesIO()
generate("Hi this is Byte")
# speak(aout)
while True:
    aout = BytesIO()
    # print(type(aout))
    with sr.Microphone() as source:
        print("You : ",end="")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio).strip()
        print(text)
        generate(res(text))
        if text=="exit" or text=="bye":
            # sleep(2)
            break
        
    except sr.UnknownValueError:
        
        # print("\nBot:sorry couldn't understand you")
        generate("sorry couldn't understand you")
    except sr.RequestError as e:
        print(f"Error: {e}")

