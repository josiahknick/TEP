import tkinter
from tkinter import ttk

from tkinter import *
from tkinter.ttk import *

root = Tk()

welcm = Label(root, text="Welcome to the Terrific Encryption Program!").grid(row=1, column=2)
intro = Label(root, text="Choose what you would like to do below.").grid(row=2, column=2)

FE_Button = Button(root, text="File Encryption").grid(row=3, column=1)
TE_Button = Button(root, text="Traffic Encryption").grid(row=3, column=2)
Settings_Button = Button(root, text="Settings").grid(row=3, column=3)

TOS = Label(root, text="By using this application you agree to our TOS. \n You can find a copy of the TOS ").grid(row=5, column=2)

def OpenTOSFile(): 
    TOS = open("tos.txt", "r")
    print(TOS.read())

TOS_Button = Button(root, text="this text is stupid", command=OpenTOSFile).grid(row=5, column=3)

root.wm_title("TEP Encryption")

root.mainloop()
