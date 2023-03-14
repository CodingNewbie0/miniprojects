# TTS(Google Text To Speech)
# https://pypi.org/ <- pip로 설치할때는 이 사이트에서 확인하고 설치
# pip install gTTS
# pip install playsound
from gtts import gTTS
from playsound import playsound

text = '안녕하세요, 박효창입니다.'

tts = gTTS(text=text, lang='ko', slow=False)
tts.save('./studyPython/output/hi.mp3')
print('생성완료!')
playsound('./studyPython/output/hi.mp3')
print('음성출력 완료!')