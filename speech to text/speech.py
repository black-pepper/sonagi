#-*- coding:utf-8 -*-
import speech_recognition as sr
import os, time

def Voice_Recogition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = " "
        try:
            said = r.recognize_google(audio, language='ko-KR')
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

while True:
    text = Voice_Recogition()

    if "도와주세요" in text:
        #어플리케이션 전송코드
        pass

    elif "종료" in text:
        break



