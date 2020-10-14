# Simple Spotify search program with automated mouse clicks to play song from "Top Result"
# NOTE: Must be already logged into Spotify on web browser
# NOTE: Speech Input MUST match Top Result

import speech_recognition as sr  # Include speech recognition library
import pynput  # Include pynput library for mouse automation
from pynput import mouse  # Include mouse class from pynput
import webbrowser as web  # Include webbrowser library for web search
import time  # Include time library for delay functions
from pynput.mouse import Button  # Include Button class for automating clicks
from pynput.mouse import Controller  # Include Controller class for mouse movement automation


def main():
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"  # Set path to location of Chrome.exe
    r = sr.Recognizer()  # Define speech recognizer function
    m = sr.Microphone()  # Define Microphone function
    mouse = Controller()  # Define mouse as controller function from pynput library

    with m as source:  # Set microphone as a source for speech recognition
        r.adjust_for_ambient_noise(source)  # Adjustment for ambient noise to improve word recognition

        print("Request a song ")  # Prompt user to request a song

        audio = r.listen(source)  # Listen for a word and store into audio
        dest = r.recognize_google(audio)  # Translate audio into text using google speech api
        if dest != 0:  # Check for dest to be filled with text
            print("Searching now for: " + dest)  # Print search with title from speech input
            time.sleep(3)  # Sleep 3 seconds (To display audio search result)

        try:
            web.open(
                "https://open.spotify.com/search/" + dest)  # Open spotify and search for song results matching speech input
            time.sleep(20)  # Sleep for 20 seconds to allow search
            mouse.position = (454, 285)  # Position mouse to Top Result box
            mouse.click(Button.left, 2)  # Click Top Result box, song will begin playing

        except Exception as e:  # Exception for try:
            print("Error : " + str(e))


if __name__ == "__main__":  # Read source file
    main()
