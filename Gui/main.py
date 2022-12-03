import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image
import re
import xml.etree.ElementTree as elemettree

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("7 Days to Die Manager")
        screenwidth = str(round(self.winfo_screenwidth()/2))
        screenheight = str(round(self.winfo_screenheight()/2))
        self.geometry(f"{screenwidth}x{screenheight}")

        serverConfigRoot="c:\\users\\kyle\\\desktop\\7D2D"
        defaultServerConfig=serverConfigRoot+"\\serverconfig.xml"


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.mainConfigButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Server Config", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.mainConfigButtonEvent)
        self.mainConfigButton.grid(row=1, column=0, sticky="ew")

        self.perkEditorButton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Perk Editor", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.perkEditorButtonEvent)
        self.perkEditorButton.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.frame_3_ButtonEvent)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)




        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #programatticly create textboxes and names from xml file
        configTree=elemettree.parse(defaultServerConfig)
        configRoot=configTree.getroot()
        textboxidx=0
        for attribute in configRoot.iter('property'):
            textboxidx=textboxidx+1
            self.label = customtkinter.CTkLabel(self.home_frame, text=attribute.attrib['name'], anchor="w")
            self.label.grid(row=textboxidx, column=0, padx=1, pady=1)
            mainConfigTextbox="mainConfigTextbox"+"{textboxidx}"
            self.mainConfigTextbox = customtkinter.CTkTextbox(self.home_frame, height=1)
            self.mainConfigTextbox.grid(row=textboxidx, column=1, padx=0, pady=1)
            self.mainConfigTextbox.insert("0.0", attribute.attrib['value'])

        # select default frame

        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.mainConfigButton.configure(fg_color=("red", "red") if name == "home" else "transparent")
        self.perkEditorButton.configure(fg_color=("red", "red") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("red", "red") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def mainConfigButtonEvent(self):
        self.select_frame_by_name("home")

    def perkEditorButtonEvent(self):
        self.select_frame_by_name("frame_2")

    def frame_3_ButtonEvent(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()