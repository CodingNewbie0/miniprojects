# pip install pyttsx3
import pyttsx3

tts = pyttsx3.init()
tts.say('안녕하세요 박효창입니다.')
tts.runAndWait()