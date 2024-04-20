# This is a two steps process
# 1. Listen for audio inpyt that can be interpreted as speech
# 2. Output the speech to text in a file

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def record_text():
    while True:
        try:
            with sr.AudioFile("recording_output.wav") as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)

                return MyText
        except sr.RequestError as e:
            print("Could not request results: {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occured")


def output_text(text):
    
    f = open("audio_output.txt", "a") # "a" --> appending text at the end of the file
    f.write(text)
    f.write("\n")
    f.close()
    return

while True:
    text = record_text()
    output_text(text)

    print("Wrote text")
