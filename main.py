import bluetooth
import subprocess
from datetime import datetime

class BluetoothComm:
    def __init__(self):
        self.server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        self.server_socket.bind(("",port))
        self.server_socket.listen(1)
        self.client_socket,address = self.server_socket.accept()
        print("Accepted connection from ",address)
        
    def read_comm(self):
        res = self.client_socket.recv(1024)
        if len(res):
            return res
        else:
            return None
 
    def send_comm(self, text):
        self.client_socket.sendall(text)
        
def blue_value():
    f = open('value.txt', 'r')
        value = int(f.readline())
        f.close()
    blue_comm.send_comm(value)
    blue_comm.send_comm(get)
    
       
blue_comm = BluetoothComm()
get = blue_comm.read_comm()

check = 0
start_time = datetime.now()

while True:
    try:
        if (datetime.now() - start).seconds > 60:
            blue_value()
            start_time = datetime.now()
        
        f = open('recognition.txt', 'r')
        line = int(f.readline())
        f.close()
        total_sum = 0
        
        if line%100000 >= 11000:
            total_sum += 11000

        if line%1000 >= 100:
            total_sum += 100
            
        if line%100 >= 10:
            total_sum += 10

        if total_sum > 0:
            #print(line)
            blue_comm.send_comm(str(line))
            blue_comm.send_comm(get)
            line -= total_sum
            check = 1
            while check == 1:
                try:
                    f = open('recognition.txt', 'w')
                    f.write(str(line))
                    f.close()
                    check = 0
                except:
                    pass

    except:
        continue
