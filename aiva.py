import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f" You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def respond(command):
    if "hello" in command:
        speak("Hello Ashwinee! How can I help you today?")
    elif "your name" in command:
        speak("I'm your Python voice assistant.")
    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that. Can you try again?")

# Main loop
while True:
    command = listen()
    respond(command)