import pip
import os
from sklearn.tree import DecisionTreeClassifier

data = [    
    [34, 8000],
    [25, 8500],
    [48, 9000],
    [61, 9500],
    [76, 10000],
    [43, 10500],
    [19, 11000],
    [52, 11500],
    [27, 12000],                      #
    [69, 12500],
    [32, 13000],
    [44, 14500],
    [59, 13500],
    [12, 12000],
    [39, 15000],
    [70, 16000],
    [23, 17500],
    [80, 14000],
    [36, 11200],
    [50, 14000]
]
dict ={0:"google cardboard",1:"samsung vr",2:"htc vr",3:"P S V R",4:"Oculus Quest"}
y_train =[0, 0, 0, 1, 1, 1, 2, 2, 2, 3,3, 3, 4, 4,3,2,1,2,4,1]
clf = DecisionTreeClassifier()
clf.fit(data, y_train)

# Make predictions on new data
# X_test = []
# t=int(input())
# l1=[0,0]
# l1[0]=int(input())
# l1[1]=int(input())
# # l1[2]=int(input())
# X_test.append(l1)
    
# y_pred = clf.predict(X_test)
# print(dict[y_pred[0]])
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
import_or_install("word2number")
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
    "what can you do":"i am a basic bot just made for this demo ,you can ask me to recommend an accessory for metaverse"
}
 
r=sr.Recognizer()
global age
global income    
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
        tts = gTTS(text,lang='ta',tld='co.in')
        
        tts.write_to_fp(aout)
        speak(aout)
def recommend(a,b):
    X_test = []
    # t=int(input())
    l1=[0,0]
    l1[0]=a
    l1[1]=b
    # l1[2]=int(input())
    X_test.append(l1)
    y_pred = clf.predict(X_test)
    return (dict[y_pred[0]])
    from time import sleep
aout = BytesIO()
generate("Hi this is Byte")
flag = 0
# speak(aout)
while True:
    # aout = BytesIO()
    if flag == 1:
        generate("whats your age ?")
    # print(type(aout))
    if flag == 2:
        generate("what's your income?")
    with sr.Microphone() as source:
        print("You : ",end="")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio).strip()
        print(text)
        if flag==1:
            global age 
            age = text
            flag=2;
            continue
        if flag==2:
            global income
            income=text
            generate(recommend(age, income))
            flag=0
            continue
            
        if "product" in text or "recommend" in text or "metaverse" in text:
            generate("ok")
            flag = 1;
            continue
        if flag==0:    
            generate(res(text))
        if text=="exit" or text=="bye":
            # sleep(2)
            break
        
    except sr.UnknownValueError:
        
        # print("\nBot:sorry couldn't understand you")
        generate("sorry couldn't understand you")
    except sr.RequestError as e:
        print(f"Error: {e}")

