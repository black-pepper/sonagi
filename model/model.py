from selenium import webdriver
import time
 
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("file:///home/pi/Desktop/capstone/model/model.html")

while True:
    try:
        label = driver.find_element_by_id('label-container')
        label = label.text.split()
        if float(label[4]) > 0.15:
            print(label[1], label[2])
            print(label[3], label[4])
        time.sleep(3)
    except:
        pass
