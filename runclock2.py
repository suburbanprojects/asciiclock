from pyfiglet import Figlet
import datetime
import time

f = Figlet(font='doom')

def clock():
    while True:
        print (f.renderText(datetime.datetime.now().strftime("%H:%M:%S")),end="\r")
        time.sleep(1)

clock()
