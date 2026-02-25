import speech_recognition as sr
import pyttsx3
import time

#r = sr.Recognizer()
#engine = pyttsx3.init()

#def speak(text):
 #   print("Jarvis:", text)
  #  engine.say(text)
   # engine.runAndWait()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice
engine.setProperty('rate', 170)


def listen():
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

#speak("Initializing Jarvis")
#speak("Say Jarvis")
def speak(text):
    print("Jarvis:", text)
    engine.stop()           # important
    engine.say(text)
    engine.runAndWait()

while True:
    word = listen()
    if "jarvis" in word:
        speak("Yes, I am listening")
    time.sleep(0.5)

