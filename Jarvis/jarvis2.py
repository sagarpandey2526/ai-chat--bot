import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

# Initialize recognizer and speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Internet problem")
        return ""

# Main program
if __name__ == "__main__":
    speak(" jervis at your service") 
    speak("Say Jarvis to activate me")


    while True:
        wake_word = listen()

        if "jarvis" in wake_word:
            speak("Yes, I am listening")

            command = listen()

            if "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")

            elif "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
  
            elif "time" in command:
                time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {time}")

            elif "date" in command:
                date = datetime.datetime.now().strftime("%d %B %Y")
                speak(f"Today's date is {date}")

            elif "exit" in command or "stop" in command:
                speak("Goodbye")
                break

            elif "open chat GPT" in command.lower():
                speak("opening chatgpt")
                webbrowser.open("https://www.chatgpt.com/")

            else:
                speak("Sorry, I did not understand that")