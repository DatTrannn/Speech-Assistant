import speech_recognition as sr
from datetime import date, datetime
import pyttsx3 #text to speech
import webbrowser

robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""


def understand():
    while(True):
        with sr.Microphone() as mic:           # Tương tự như mic = sr.Microphone() nhưng với with khi chạy xong mic sẽ tự tắt
            print("Robot: I'm listening")
            audio = robot_ear.listen(mic)
        print("Robot: ... ")
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You: " + you)
        if you == "":
            robot_brain = "Sorry, I can't hear you, try again"
        elif there_exists(["hey", "hi", "hello"], you):
            robot_brain = "Hello"
        elif there_exists(["date","day"],you):
            today = date.today()
            robot_brain = today.strftime("%d/%m/%Y")
        elif there_exists(["time"],you):
            now = datetime.now()
            robot_brain = now.strftime("%H:%M:%S")
        elif there_exists(["search for"], you) and "youtube" not in you:
            search_term = you.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            robot_brain = f"Here is what I found for {search_term} on google"
        elif there_exists(["youtube"], you):
            search_term = you.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            robot_brain = f'Here is what I found for {search_term} on youtube'
        elif there_exists(["stop", "bye"], you):
            robot_brain = "Bye!"
            print("Robot: " + robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
        else: 
            robot_brain = "I'm fine thank you and you"

        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

def there_exists(terms, you):
    for term in terms:
        if term in you:
            return True

understand()