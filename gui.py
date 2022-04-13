
# Creating simple GUI to demostrate SYNC capabilities.

import tkinter
import PIL
from tkinter import Label, Button, Tk
from PIL import ImageTk, Image
import webbrowser
import shutil
import os

class CAN_BUS_GUI:
    def __init__(self, master) -> None:

        self.pwd = os.getcwd()
        self.master = master
        master.title("CAN BUS")

        # Setting up Texts
        self.label = Label(master, text="CAN BUS")
        self.label.pack()

        self.analyst_label = Label(master, text = "Analyst_1")
        self.analyst_label.pack()
        self.analyst_label.place(x=150, y=130)

        self.analyst_label_2 = Label(master, text = "Analyst_2")
        self.analyst_label_2.pack()
        self.analyst_label_2.place(x=525, y=130)

        self.sync_button = Button(master, text="SYNC", command=self.SYNC)
        self.sync_button.pack()

        # Read Button file for Analyst 1
        self.File_button_A1 = Button(master, text="Analyst 1 File", command=self.read_file)
        self.File_button_A1.pack()
        self.File_button_A1.place(x=150, y=75)

        # Read Button file for Analyst 2
        self.File_button_A2 = Button(master, text="Analyst 2 File", command=self.read_file_2)
        self.File_button_A2.pack()
        self.File_button_A2.place(x=525, y=75)

        # Structoring Image car
        self.image = Image.open(self.pwd+"/Images/car.png")
        self.resize_image_car = self.image.resize((330, 255))
        self.resize_image_car = ImageTk.PhotoImage(self.resize_image_car)
        self.image_label = tkinter.Label(image=self.resize_image_car)
        self.image_label.place(x=25, y=150)

        # Structoring Image empty car
        self.image2 = Image.open(self.pwd+"/Images/emptycar.png")
        self.resize_image_emptycar = self.image2.resize((330, 255))
        self.resize_image_emptycar = ImageTk.PhotoImage(self.resize_image_emptycar)
        self.image_label2 = tkinter.Label(image=self.resize_image_emptycar)
        self.image_label2.place(x=400, y=150)

    # Command for button SYNC
    def SYNC(self):   
        image_label2 = tkinter.Label(image=self.resize_image_car)
        image_label2.place(x=400, y=150)

        # Copy over text file
        shutil.copyfile(self.pwd+"/Database/Analyst1/node_info.txt", 
        self.pwd+"/Database/Analyst2/node_info.txt")

        # Copy Json Obj
        shutil.copyfile(self.pwd+"/Database/Analyst1/Node_info.json", 
        self.pwd+"/Database/Analyst2/Node_info.json")

    # Command for button Analyst_1
    def read_file(self):
        webbrowser.open(self.pwd+"/Database/Analyst1/node_info.txt")

    # Command for button Analyst_2 
    def read_file_2(self):
        webbrowser.open(self.pwd+"/Database/Analyst2/node_info.txt")

root = Tk()
my_gui = CAN_BUS_GUI(root)
root.geometry("750x500")
root.mainloop()

# Clear Contents of Analyst 2 files for demo purposes
with open(os.getcwd()+"/Database/Analyst2/node_info.txt", 'r+') as f:
    f.truncate(0)

with open(os.getcwd()+"/Database/Analyst2/Node_info.json", 'r+') as f:
    f.truncate(0)











