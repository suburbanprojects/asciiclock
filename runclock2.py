from pyfiglet import Figlet
import datetime
import time
import os

f = Figlet(font='doom')

def termwin():
    os.system("mode con cols=50 lines=10")

def clock():
    while True:
        print (f.renderText(datetime.datetime.now().strftime("%H:%M:%S")),end="\r")
        time.sleep(1)

termwin()
clock()
