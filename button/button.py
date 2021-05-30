#-*- coding: utf-8 -*-   
  
import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode( GPIO.BOARD )  
  
#12번핀은 출력모드로 설정  
GPIO.setup(12, GPIO.OUT)  
#11번핀은 입력모드로 설정  
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
while True:  
  
    input_state = GPIO.input(11)
    if input_state == False:  
        GPIO.output(12, GPIO.HIGH)
        print(input_state)
    else:  
        GPIO.output(12, GPIO.LOW)
        #print(input_state)
  
    time.sleep(0.5)  