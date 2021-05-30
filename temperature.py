import sys
import time
from collections import deque
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

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

def init():
    temper = deque()
    while len(temper)<60:
        temperature = mpu.readTemperatureMaster()
        temper.append(int(temperature))
        total_sum += int(temperature)

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

mpu.configure()

init()
while True:
    temperature = mpu.readTemperatureMaster()
    temper.append(int(temperature))
    total_sum += int(temperature)
    total_sum -= temper.popleft()
    if total_sum/60 > 35:
        Pass_Data()
        init()
    time.sleep(1)
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        #print('temperature: ' + str(temperature))
        #print('humidity: ' + str(humidity))
        
    #else:
        #print('Failed to get reading. Try again!')
        #sys.exit(1)
