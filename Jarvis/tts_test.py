import speech_recognition as sr
import pyttsx3
import time

# Text to Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

# Speech Recognition
r = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio).lower()
    except:
        return ""

speak("Initializing Jarvis")
speak("Say Jarvis to activate me")

while True:
    command = listen()
    if "jarvis" in command:
        speak("Yes, I am listening")
    time.sleep(0.4)
