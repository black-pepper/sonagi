import FaBo9Axis_MPU9250
import time
import sys
from datetime import datetime
from collections import deque

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%10000 < 1000:
                line = line + 1000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
        
def Reset_data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%10000 >= 1000:
                line = line - 1000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
        
def init():
    curr_time = datetime.now()
    while (datetime.now() - start).seconds < 60 :
        try:
        curr_time = detetime.datetime.now()
        accel = mpu9250.readAccel()
        gyro = mpu9250.readGyro()
        mag = mpu9250.readMagnet()
        
        queue.append(accel['x'])
        
        if abs(accel['x']) > 1 and abs(accel['y']) > 1 and abs(accel['z']) > 1:
            Pass_Data()
            time.sleep(2)
            Reset_Data()

        time.sleep(0.1)
        
def save_sensor_value():
    avg = sum(queue)/len(queue)
    while check == 0:
        try:
            f = open('value.txt', 'w')
            f.write(str(avg))
            f.close()

            check = 1
        except:
            continue

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
queue = deque()
init()
size = len(queue)

start_time = datetime.now()

while True:
    try:
        if (datetime.now() - start).seconds > 60:
            save_sensor_value()
            start_time = datetime.now()
        
        
        accel = mpu9250.readAccel()
        #print(" ax = " , ( accel['x'] ))
        #print( " ay = " , ( accel['y'] ))
        #print( " az = " , ( accel['z'] ))

        gyro = mpu9250.readGyro()
        #print( " gx = " , ( gyro['x'] ))
        #print( " gy = " , ( gyro['y'] ))
        #print( " gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        #print( " mx = " , ( mag['x'] ))
        #print( " my = " , ( mag['y'] ))
        #print( " mz = " , ( mag['z'] ))
        #print()
        
        if abs(accel['x']) > 1 and abs(accel['y']) > 1 and abs(accel['z']) > 1:
            Pass_Data()
            time.sleep(2)
            Reset_Data()
            
        queue.popleft()
        queue.append(accel['x'])

        time.sleep(0.1)

    except KeyboardInterrupt:
        pass

