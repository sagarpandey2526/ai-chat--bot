import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse

# Initialize
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

speak("Hello, I am Jarvis. What should I play on YouTube?")

while True:
    command = listen()

    if "play i guess" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        query = urllib.parse.quote(song)
        webbrowser.open(f"https://youtu.be/Qg9LxRHLbAk?list=RDQg9LxRHLbAk={query}")

    elif"play rap" in command:
        speak("playing song on youtube")
        webbrowser.open("https://youtu.be/qVcHlaFZf6A?list=RDqVcHlaFZf6A")

    elif"play no cap"in command:
        speak("playi ng song on youtube")
        webbrowser.open("https://youtu.be/PejQbGZraqg?list=RDqVcHlaFZf6A")

    elif"news" in command:
        webbrowser.open("https://youtu.be/e1FIApIafWE")

    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        break
