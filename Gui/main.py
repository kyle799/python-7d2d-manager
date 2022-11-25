#!/bin/python3
import tkinter as tk
import tkinter.font as tkFont

import time


class App:
    def __init__(self, root):
        root.title("7D2D Server Manager")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Times',size=10)


        button1=tk.Button(root)
        button1["bg"] = "#f0f0f0"
        button1["font"] = ft
        button1["fg"] = "#000000"
        button1["justify"] = "center"
        button1["text"] = "Main"
        button1.place(x=0,y=0,width=70,height=25)
        button1["command"] = self.button1_command

        button2=tk.Button(root)
        button2["bg"] = "#f0f0f0"
        button2["font"] = ft
        button2["fg"] = "#000000"
        button2["justify"] = "center"
        button2["text"] = "Config"
        button2.place(x=70,y=0,width=70,height=25)
        button2["command"] = self.button2_command

        button3=tk.Button(root)
        button3["bg"] = "#f0f0f0"
        button3["font"] = ft
        button3["fg"] = "#000000"
        button3["justify"] = "center"
        button3["text"] = "Perk Editor"
        button3.place(x=140,y=0,width=70,height=25)
        button3["command"] = self.button3_command

        button4=tk.Button(root)
        button4["bg"] = "#f0f0f0"
        button4["font"] = ft
        button4["fg"] = "#000000"
        button4["justify"] = "center"
        button4["text"] = "Button"
        button4.place(x=210,y=0,width=70,height=25)
        button4["command"] = self.button4_command

        button5=tk.Button(root)
        button5["bg"] = "#f0f0f0"
        button5["font"] = ft
        button5["fg"] = "#000000"
        button5["justify"] = "center"
        button5["text"] = "Import configuration"
        button5.place(x=430,y=0,width=170,height=25)
        button5["command"] = self.button5_command

        input1=tk.Entry(root)
        input1["borderwidth"] = "1px"
        input1["font"] = ft
        input1["fg"] = "#333333"
        input1["justify"] = "left"
        input1["text"] = "Entry"
        input1["show"] = "servername"
        input1.place(x=0,y=50,width=424,height=37)

        button6=tk.Button(root)
        button6["bg"] = "#f0f0f0"
        button6["fg"] = "#000000"
        button6["justify"] = "center"
        button6["text"] = "Button"
        button6.place(x=430,y=50,width=83,height=30)
        button6["command"] = self.button6_command

    def button1_command(self):
        print(f"click main screen")


    def button2_command(self):
        print(f"click config")


    def button3_command(self):
        print(f"click perk edit")


    def button4_command(self):
        print(f"button 4")
    
    def button5_command(self):
        print(f"import config")

    def button6_command(self):
        print(f"Changed servername to ")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
