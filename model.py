from selenium import webdriver
import time

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%100000 < 10000:
                line = line + 10000

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

            if line%100000 >= 10000:
                line = line - 10000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
 
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("file:///home/pi/Desktop/capstone/model/model.html")

while True:
    try:
        label = driver.find_element_by_id('label-container')
        label = label.text.split()
        if float(label[4]) > 0.15:
            print(label[1], label[2])
            print(label[3], label[4])
            Pass_Data()
            time.sleep(3)
            #Reset_Data()
    except:
        pass
