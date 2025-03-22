import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import pyttsx3
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key)

# Initialize text-to-speech engine
engine = pyttsx3.init()


def say(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


say("Hello! Zen AI is now active.")

chatStr = ""


def chat(query):
    """Handle chatting using Google Gemini AI."""
    global chatStr
    chatStr += f"User: {query}\nZen: "

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(query)
        response_text = response.text.strip()
        chatStr += f"{response_text}\n"
        print("AI:", response_text)
        say(response_text)  # Speak response
        return response_text
    except Exception as e:
        print("AI Error:", e)
        return "Sorry, I couldn't process that."


def takeCommand():
    """Listen to user's voice and return as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 4000  # Adjust for background noise
        try:
            audio = r.listen(source, timeout=5)  # Timeout for responsiveness
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand.")
            return "None"
        except sr.RequestError:
            print("Could not connect to the internet.")
            return "None"


if __name__ == '__main__':
    print('Welcome to Zen AI')
    say("Zen AI is ready.")

import os
import webbrowser
import datetime
import subprocess

while True:
    query = takeCommand().lower()
    if query == "none":
        continue  # Skip if no input detected

    # Open common websites
    sites = {
        "website": "https://zendalona.com/",
        "wikipedia": "https://www.wikipedia.com",
        "google": "https://www.google.com"
    }
    for site in sites:
        if f"open {site}" in query:
            say(f"Opening {site}")
            webbrowser.open(sites[site])
            continue

    # Play Music (Update path for Windows)
    if "open music" in query:
        musicPath = r"C:\Users\drart\Downloads\l_theme_death_note.mp3"  # Windows me path change karein
        os.startfile(musicPath)  # Windows me `os.startfile()` use hota hai

    # Time Check
    elif "the time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        say(f"Sir, the time is {hour} bajke {minute} minutes.")

    # Open Camera (Windows Version)
    elif "open camera" in query:
        subprocess.run("start microsoft.windows.camera:", shell=True)  # Windows Camera command

    # Open Password Manager (Windows me "Passky" ka exact path dalna padega)
    elif "open pass" in query:
        passky_path = r"C:\Path\to\Passky.exe"  # Yahan correct path likhna hoga
        os.startfile(passky_path)

    # AI Chat (Gemini model use hoga)
    elif "using artificial intelligence" in query:
        chat(query)

    # Quit Command
    elif "jarvis quit" in query:
        say("Goodbye, Rey!")
        exit()

    # Reset Chat History
    elif "reset chat" in query:
        chatStr = ""

    else:
        chat(query)  # Default AI model is Gemini
