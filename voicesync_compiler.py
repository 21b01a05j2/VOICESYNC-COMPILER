import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyttsx3

# Function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

# Function to perform actions on the online Python compiler
def perform_compiler_actions():
    url = "https://www.programiz.com/python-programming/online-compiler/"
    driver = webdriver.Chrome()  # Make sure you have Chromedriver installed
    driver.get(url)
    speak("Opening the online Python compiler.")
    time.sleep(5)  # Allow time for the compiler to fully load, you can adjust this time

    if driver is not None:
        try:
            # Find the code editor element and send keys to input the desired code
            code_editor = driver.find_element("class name", "ace_text-input")
            code_editor.send_keys("print(\"Hello, world!\")")
            time.sleep(1)  # Wait for a moment
            code_editor.send_keys(Keys.CONTROL, Keys.RETURN)  # Use CONTROL + Enter to run the code
            speak("Code printed: print(\"Hello, world!\")")
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred while executing the code.")
        finally:
            driver.quit()  # Close the browser window
    else:
        speak("The online Python compiler is not open.")

# Function to process user commands
def process_command(command):
    if "perform compiler actions" in command:
        perform_compiler_actions()
    else:
        speak("Command not recognized.")

# Main function to initiate the voice assistant
def main():
    speak("Hello! How can I assist you today?")

    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
