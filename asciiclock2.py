from pyfiglet import Figlet
import datetime
import time


def clock():
    while True:
        print (f.renderText(datetime.datetime.now().strftime("%H:%M:%S")),end="\r")
        time.sleep(1)

print("---Ascii Clock 1.0.1------")
print("|The fonts available :   |")
print("|1. Doom                 |")
print("|2. Digital              |")
print("|3. Slant                |")
print("|4. Future               |")
print("|5. Basic                |")
print("---Press Ctrl+C to quit---\n")

while True:
    select = input("Enter your selection: ")

    if select == '1':
        f = Figlet(font='doom')
        clock()

    elif select == '2':
        f = Figlet(font='digital')
        clock()

    elif select == '3':
        f = Figlet(font='slant')
        clock()

    elif select == '4':
        f = Figlet(font='future_6')
        clock()

    elif select == '5':
        f = Figlet(font='basic')
        clock()




