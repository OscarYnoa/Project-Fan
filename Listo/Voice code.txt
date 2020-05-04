import os

import speech_recognition as sr

r = sr.Recognizer()

def voice_audio():
    with sr.Microphone() as source:

        audio = r.listen(source)
        voice_text = ''
        try:
            voice_text = r.recognize_google(audio)
            print(voice_text)
        except:
            print('Sorry could not recognize your voice')

        return voice_text

def abanico (voice_text):
    if 'off'in voice_text:
        print(abanico_off())
    if '1' in voice_text or 'one' in voice_text:
        print(abanico_1())
    if '2' in voice_text or 'two' in voice_text:
        print(abanico_2())
    if '3' in voice_text or 'three'in voice_text:
        print(abanico_3())

def abanico_off():
    x = os.system("start C:/Users/oscar/Desktop/Listo/Off_Fan.gif")
    return x

def abanico_1():
    x = os.system("start C:/Users/oscar/Desktop/Listo/Slow_Fan.mp4")
    return x

def abanico_2():
    x = os.system("start C:/Users/oscar/Desktop/Listo/Med_Fan.mp4")
    return x

def abanico_3():
    x = os.system("start C:/Users/oscar/Desktop/Listo/High_Fan.mp4")
    return x



while True:
    voice_text = voice_audio()
    abanico(voice_text)