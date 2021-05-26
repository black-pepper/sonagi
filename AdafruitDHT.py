#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

import sys
import Adafruit_DHT
from collections import deque

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%100 < 10:
                line = line + 10

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

def init():
    temper = deque()
    while len(temper)<60:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            temper.append(int(temperature))
            total_sum += int(temperature)

sensor = 11
pin = 2
temper = deque()
total_sum = 0

init()
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        temper.append(int(temperature))
        total_sum += int(temperature)
        total_sum -= temper.popleft()
        if total_sum/60 > 35:
            Pass_Data()
            init()
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        #print('temperature: ' + str(temperature))
        #print('humidity: ' + str(humidity))
        
    #else:
        #print('Failed to get reading. Try again!')
        #sys.exit(1)
