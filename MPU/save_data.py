import FaBo9Axis_MPU9250
import time
import sys
import pandas as pd

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

df = pd.DataFrame(columns = ['ax' , 'ay' , 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz'])

try:
    for i in range(20):
        accel = mpu9250.readAccel()
        #print(" ax = " , ( accel['x'] ))
        #print( " ay = " , ( accel['y'] ))
        #print( " az = " , ( accel['z'] ))
        
        zgyro = mpu9250.readGyro()
        #print( " gx = " , ( gyro['x'] ))
        #print( " gy = " , ( gyro['y'] ))
        #print( " gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        #print( " mx = " , ( mag['x'] ))
        #print( " my = " , ( mag['y'] ))
        #print( " mz = " , ( mag['z'] ))
        
        df = df.append({'ax':accel['x'], 'ay':accel['y'], 'az':accel['z'], 'gx':gyro['x'], 'gy':gyro['y'], 'gz':gyro['z'], 'mx':mag['x'], 'my':mag['y'], 'mz':mag['z']})

        time.sleep(0.1)
        
    df.to_csv("0527-1.csv")

except KeyboardInterrupt:
    sys.exit()

