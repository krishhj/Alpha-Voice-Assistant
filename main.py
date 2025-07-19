import speech_recognition as sr
import webbrowser
import musicLibrary  # Custom dictionary or module mapping song names to URLs
import requests
import os
from google import genai
from google.genai import types
import sys
import pygame
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv() 

# Save API in .env file to keep it secured
newsapi = os.getenv("NEWS_API_KEY")
os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY")

# Initialize recognizer
r = sr.Recognizer()

# Speak function using gTTS and Pygame
def speak(text):
    tts = gTTS(text, slow=False)
    tts.save('temp.mp3')  # Save TTS output to a temporary file

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Wait until the audio playback is finished
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")  # Clean up after playing

# AI processing using Gemini for general questions
def aiProcess(command):
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a smart Virtual Assistant. Your name is Alpha. Answer the question asked by the user in few sentences please"
        ),
        contents=f"{command} in one or two sentences"
    )
    return response.text

# Handle recognized voice commands
def processCommand(c):
    print(c)

    if "google" in c.lower():
        webbrowser.open_new_tab("https://www.google.com/")
        speak("Opening Google")

    elif "youtube" in c.lower():
        webbrowser.open_new_tab("https://www.youtube.com/")
        speak("Opening YouTube")

    elif "facebook" in c.lower():
        webbrowser.open_new_tab("https://www.facebook.com/")
        speak("Opening Facebook")

    elif "instagram" in c.lower():
        webbrowser.open_new_tab("https://www.instagram.com/")
        speak("Opening Instagram")

    elif "linkedin" in c.lower():
        webbrowser.open_new_tab("https://www.linkedin.com/")
        speak("Opening LinkedIn")

    elif "my github" in c.lower():
        webbrowser.open_new_tab("https://github.com/krishhj")
        speak("Opening GitHub")

    elif "college" in c.lower():
        webbrowser.open_new_tab("https://www.kjsieit.in/sims/student/home.php")
        speak("Opening your college's website")

    elif "chat gpt" in c.lower():
        webbrowser.open_new_tab("https://chatgpt.com/")
        speak("Opening ChatGPT")

    elif "play" in c.lower():
        # Assumes command is like "play despacito"
        song = c.lower().split(" ", 1)[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open_new_tab(link)
            speak(f"Playing {song}")
        else:
            speak("Sorry, I couldn't find that song.")

    elif "news" in c.lower():
        url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={newsapi}"
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok":
            for article in data["articles"][:3]:  # Limit to 3 headlines
                speak(article["title"])
        else:
            speak("Sorry, I failed to fetch the news.")

    elif "close" in c.lower() or "exit" in c.lower():
        speak("Yes, thank you. Have a great day!")
        sys.exit()

    else:
        # Let AI handle unrecognized queries
        output = aiProcess(c)
        speak(output)

# Main program execution
if __name__ == "__main__":
    speak("Initializing Alpha... Hello, how can I help you today?")

    while True:
        try:
            with sr.Microphone() as source:
                print("Say something...")
                audio = r.listen(source)

            print("Recognizing...")
            word = r.recognize_google(audio)
            print("You said:", word)

            # Graceful exit
            if "close" in word.lower() or "exit" in word.lower():
                speak("Yes, thank you. Have a great day!")
                break

            # Wake word
            if "alpha" in word.lower():
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = r.listen(source, phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print("Command recognized:", command)
                    processCommand(command)

                    if "close" in command.lower() or "exit" in command.lower():
                        speak("Yes, thank you!")
                        break

        except Exception as e:
            print(f"Alpha error: {e}")
