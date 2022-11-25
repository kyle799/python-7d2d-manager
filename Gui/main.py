#!/bin/python3
import tkinter as tk
import tkinter.font as tkFont

import time

global buttonForegroundColor
global buttonBackgroundColor

buttonForegroundColor ="#000000"
buttonBackgroundColor = "#f0f0f0"

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

        button1=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Main", command=self.button1_command)
        button1.place(x=0,y=0,width=70,height=25)

        button2=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Config", command=self.button2_command)
        button2.place(x=70,y=0,width=70,height=25)

        button3=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center",text="Perk Editor", command=self.button3_command)
        button3.place(x=140,y=0,width=70,height=25)

        button4=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Button", command=self.button4_command)
        button4.place(x=210,y=0,width=70,height=25)

        button5=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center",text="Import Configuration",command=self.button5_command)
        button5.place(x=430,y=0,width=170,height=25)

        input1=tk.Entry(root, font=ft, borderwidth="1px",foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="left",)
        #input1["text"] = "Entry"
        #input1["show"] = "servername"
        input1.place(x=0,y=50,width=424,height=37)

        button6=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Button", command=self.button6_command)
        button6.place(x=430,y=50,width=83,height=30)

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
        print(f"Changed servername to {self.input1.get('1.0', tk.END)} ")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
