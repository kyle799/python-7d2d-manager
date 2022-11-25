#!/bin/python3
import tkinter as tk
import tkinter.font as tkFont

import time

global buttonForegroundColor
global buttonBackgroundColor
global ft

buttonForegroundColor ="#000000"
buttonBackgroundColor = "#f0f0f0"
#ft = tkFont.Font(family='Times',size=10)
class App:
    def __init__(self, root):
        root.title("7D2D Server Manager")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        ft = tkFont.Font(family='Times',size=10)

        pageMenu = tk.Frame(root)
        pageMenu.columnconfigure(0, weight=1)

        button1Main=tk.Button(pageMenu, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Main", command=self.button1Main_command)
        button1Main.grid(row=0, column=0, sticky='w', padx=5,)

        button2Config=tk.Button(pageMenu, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Config", command=self.button2Config_command)
        button2Config.grid(row=0, column=1, sticky='w', padx=5)

        button3PerkEditor=tk.Button(pageMenu, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Perk Editor", command=self.button3PerkEditor_command)
        button3PerkEditor.grid(row=0, column=2, sticky='w', padx=5)

        button4Button=tk.Button(pageMenu, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Button", command=self.button4Button_command)
        button4Button.grid(row=0, column=3, sticky='w', padx=5)

        button5ImportConfiguration=tk.Button(pageMenu, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Import Configuration", command=self.button5ImportConfiguration_command)
        button5ImportConfiguration.grid(row=0, column=4, sticky= 'e', padx=5)

        pageMenu.pack()



#add to mainpage 
        #input1=tk.Entry(root, font=ft, borderwidth="1px",foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="left")
        #input1.pack()

        #button6Button=tk.Button(root, font=ft, foreground=buttonForegroundColor, background=buttonBackgroundColor, justify="center", text="Button", command=self.button6Button_command)
        #button6Button.place(x=430,y=50,width=83,height=30)




    def button1Main_command(self):
        print(f"click main screen")


    def button2Config_command(self):
        print(f"click config")


    def button3PerkEditor_command(self):
        print(f"click perk edit")


    def button4Button_command(self):
        print(f"button 4")
    
    def button5ImportConfiguration_command(self):
        print(f"import config")

    def button6Button_command(self):
        print(f"Changed servername to {self.input1.get('1.0', tk.END)} ")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
