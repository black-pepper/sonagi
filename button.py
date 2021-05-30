#-*- coding: utf-8 -*-   
  
import RPi.GPIO as GPIO  
import time

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%10 < 1:
                line = line + 1

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
  
GPIO.setmode( GPIO.BOARD )  
  
#12번핀은 출력모드로 설정  
GPIO.setup(12, GPIO.OUT)  
#11번핀은 입력모드로 설정  
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
while True:  
  
    input_state = GPIO.input(11)
    if input_state == False:  
        GPIO.output(12, GPIO.HIGH)
        Pass_Data()
    else:  
        GPIO.output(12, GPIO.LOW)
        #print(input_state)
  
    time.sleep(0.5)  