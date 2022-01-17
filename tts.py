import pyttsx3
from tts_setting import *
import os
import time
import sys

print("for exit press 'Alt+F4' or type ':e'")
print("Initializing...")
engine = pyttsx3.init()
engine.setProperty("rate", voice_speed)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[voice_gender].id)
print("Done")

while True:
    text = input("Please Enter The Text: ")
    if text == ":e":
        sys.exit()
    print('Speaking...')
    engine.say(text)
    engine.runAndWait()
    print("Done")
    time.sleep(1)
    os.system("cls")
