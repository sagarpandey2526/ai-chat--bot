import speech_recognition as sr  
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommend(c):
    if "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
  
if __name__ == "__main__":
    speak("Initializing jarvis...")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...") 
                audio = r.listen(source,timeout=5,phrase_time_limit=5) 
            word = r.recognize_google(audio)
            print("You Said: ",word)
            if(word.lower()=="jarvis"):
                
                speak("Ya")
            
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source)
                r.adjust_for_ambient_noise(source, duration=1)
                command = r.recognize_google(audio)

                processCommend(command)

        except Exception as e:
            print("Error;{0}".format(e))                
