import subprocess
import threading
import time
import webbrowser
import pyttsx3
import requests
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=a0b47318cc1ab8d39d4c4958d493b1c3&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        speak(f"The weather in {city} is {weather_desc}. The temperature is {temp} degrees Celsius.")
    else:
        speak("Sorry, I couldn't fetch the weather information for that city.")

def open_spotify():
    try:
        subprocess.Popen(["spotify"])
    except FileNotFoundError:
        speak("Spotify is not installed on this system.")

def open_notepad():
    try:
        subprocess.Popen(["notepad"])
    except FileNotFoundError:
        speak("Notepad is not installed on this system.")

def set_reminder(reminder_text, seconds):
    def reminder_thread():
        time.sleep(seconds)
        speak("Reminder: " + reminder_text)

    threading.Thread(target=reminder_thread).start()
    speak(f"I will remind you to {reminder_text} in {seconds} seconds.")

def chat(query):
    responses = {
        "what's your name": "My name is Robo, your virtual assistant.",
        "who created you": "I was created by Sujal Lothe.",
        "what can you do": "I can tell you the weather, open YouTube, Spotify, and Notepad. You can also chat with me!",
        "bye": "Goodbye! Take care.",
        "hello robo": "Hello! How can I assist you today?",
        "you are amazing":"thank you, You also"
    }
    response = responses.get(query.lower(), "I'm sorry, I didn't understand that.")
    speak(response)

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                query = recognizer.recognize_google(audio).lower()
                print("You said:", query)

                if "weather" in query:
                    speak("Sure, which city?")
                    audio = recognizer.listen(source)
                    city = recognizer.recognize_google(audio).lower()
                    get_weather(city)
                elif "youtube" in query:
                    speak("Opening YouTube.")
                    webbrowser.open("https://www.youtube.com")
                elif "spotify" in query:
                    speak("Opening Spotify.")
                    open_spotify()
                elif "notepad" in query:
                    speak("Opening Notepad.")
                    open_notepad()
                elif "set reminder" in query:
                    speak("What would you like me to remind you?")
                    audio = recognizer.listen(source)
                    reminder_text = recognizer.recognize_google(audio)
                    speak("In how many seconds should I remind you?")
                    audio = recognizer.listen(source)
                    seconds = int(recognizer.recognize_google(audio))
                    set_reminder(reminder_text, seconds)
                elif "bye" in query and "robo" in query:
                    speak("Goodbye!")
                    return  # Exiting the function to terminate the program
                else:
                    chat(query)

            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand what you said.")
            except sr.RequestError:
                speak("Sorry, I'm having trouble accessing speech recognition service.")

if __name__ == "__main__":
    main()





