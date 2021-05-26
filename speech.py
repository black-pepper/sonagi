#-*- coding:utf-8 -*-
import speech_recognition as sr
import os, time

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%1000 < 100:
                line = line + 100

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue

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

    if "인식 테스트" in text:
        Pass_Data()
        pass

    elif "종료" in text:
        break



