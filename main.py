#@mathew4STAR
#15-9-2021
#program that checks the attendence
#alter the configuration file
#--------------------

from tabnanny import check
import pyautogui as pg
from PIL import Image, ImageGrab
import time 
import tkinter as tk

def addclass(classs, div, data):
    f = open(("data//" + classs + div + ".txt"), "w+")
    f.write(data)
    f.close()

def check_attendance(configuration):
    time.sleep(int(configuration[0]))
    strength = int(configuration[1])
    floc = configuration[2].split()
    sloc = configuration[3].split()
    firstloc = (int(floc[0]), int(floc[1]))
    secondloc = (int(sloc[0]), int(sloc[1]))
    pg.click(firstloc)
    pg.moveTo(secondloc)
    absent = []
    participants = open("data//kids.txt")
    for i in participants:
        i = i.strip("\n")
        pg.write(i)
        image = ImageGrab.grab()
        color = image.getpixel(secondloc)
        if color == (255, 255, 255):
            absent.append(i)
        pg.hotkey('ctrl', 'shift', 'backspace')
        
    print("STRENCTH:", strength)
    print("PRESENT:", strength - len(absent))
    print("ABSENT:", len(absent))
    print("Absentees")
    print(absent)
    input('Press enter to close the application')

root = tk.Tk()
label = tk.Label(root, text="hello welcome to this program")
label.pack()
config = open("data//config.txt")
configuration = []
for i in config:
    configuration.append(i.strip("\n"))

button = tk.Button(root, text= "START PROCESS", command= lambda: check_attendance(configuration))
button.pack()

root.mainloop()