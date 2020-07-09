from tkinter import *

root = Tk()

###Introduction and instructions
welcm = Label(root, text="Welcome to the Terrific Encryption Program!").grid(row=1, column=2)
intro = Label(root, text="Choose what you would like to do below.").grid(row=2, column=2)

###TOOLS###

###File Encryption
FE_Button = Button(root, text="File Encryption").grid(row=3, column=1)

###Traffic Encryption
TE_Button = Button(root, text="Traffic Encryption").grid(row=3, column=2)

###Settings
Settings_Button = Button(root, text="Settings").grid(row=3, column=3

###TOS 
TOS = Label(root, text="By using this application you agree to our TOS. \n You can find a copy of the TOS ").grid(row=5, column=2)
def OpenTOSFile():
    TOS = open("TEP Terms of Service", "r")
    print(TOS.read())
TOS_Button = Button(root, text="here.", command=OpenTOSFile, font=("Calibri", 8)).grid(row=5, column=3)

###Window Settings
#root.geometry("500x500")
root.wm_title("TEP Encryption")

root.mainloop()