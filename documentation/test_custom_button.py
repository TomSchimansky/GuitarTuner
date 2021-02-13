""" This is a small program to demonstrate the use
    of the TkinterCustomButton class, which is used
    in this project """

import tkinter
import tkinter.messagebox
import os
import sys
from distutils.version import StrictVersion as Version

from tkinter_custom_button import TkinterCustomButton

MAIN_PATH = os.path.dirname(__file__)

APP_NAME = "Rounded Tkinter custom button test"
ABOUT_TEXT = "Simple Test-App"
WIDTH = 600
HEIGHT = 400


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        if sys.platform == "darwin":  # macOS
            if Version(tkinter.Tcl().call("info", "patchlevel")) >= Version("8.6.9"):  # Tcl/Tk >= 8.6.9
                os.system("defaults write -g NSRequiresAquaSystemAppearance -bool No")  # turn on dark mode for all apps
                # Currently this works only with anaconda python version (python.org Tcl/Tk version is only 8.6.8).

        tkinter.Tk.__init__(self, *args, **kwargs)

        self.minsize(WIDTH, HEIGHT)
        self.resizable(True, True)
        self.title(APP_NAME)
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)

        if sys.platform == "darwin":  # macOS
            self.menubar = tkinter.Menu(master=self)
            self.app_menu = tkinter.Menu(self.menubar, name='apple')
            self.menubar.add_cascade(menu=self.app_menu)

            self.app_menu.add_command(label='About ' + APP_NAME, command=self.about_dialog)
            self.app_menu.add_separator()

            self.config(menu=self.menubar)
            self.createcommand('tk::mac::Quit', self.on_closing)

        # ========== slightly rounded corners =============

        self.button_1 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#2874A6",
                                            hover_color="#5499C7",
                                            text_font=None,
                                            text="Test Button 1",
                                            text_color="white",
                                            corner_radius=10,
                                            width=120,
                                            height=45,
                                            hover=True,
                                            command=self.test_function)
        self.button_1.place(relx=0.33, rely=0.2, anchor=tkinter.CENTER)

        self.button_2 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#922B21",
                                            border_color="white",
                                            hover_color="#CD6155",
                                            text_font=None,
                                            text="Test Button 2",
                                            text_color="white",
                                            corner_radius=10,
                                            border_width=2,
                                            width=150,
                                            height=45,
                                            hover=True,
                                            command=self.test_function)
        self.button_2.place(relx=0.66, rely=0.2, anchor=tkinter.CENTER)

        # ========== fully rounded corners =============

        self.button_3 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#1E8449",
                                            hover_color="#2ECC71",
                                            text_font=None,
                                            text="Test Button 3",
                                            text_color="white",
                                            corner_radius=20,
                                            width=120,
                                            height=40,
                                            hover=True,
                                            command=self.test_function)
        self.button_3.place(relx=0.33, rely=0.4, anchor=tkinter.CENTER)

        self.button_4 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            border_color="#BB8FCE",
                                            fg_color="#6C3483",
                                            hover_color="#A569BD",
                                            text_font=None,
                                            text="Test Button 4",
                                            text_color="white",
                                            corner_radius=20,
                                            border_width=2,
                                            width=150,
                                            height=40,
                                            hover=True,
                                            command=self.test_function)
        self.button_4.place(relx=0.66, rely=0.4, anchor=tkinter.CENTER)

        # ========== no rounded corners =============

        self.button_5 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#A93226",
                                            hover_color="#CD6155",
                                            text_font=None,
                                            text="Test Button 5",
                                            text_color="black",
                                            corner_radius=0,
                                            width=120,
                                            height=40,
                                            hover=True,
                                            command=self.test_function)
        self.button_5.place(relx=0.33, rely=0.6, anchor=tkinter.CENTER)

        self.button_6 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color=self.cget("bg"),
                                            border_color="#ABB2B9",
                                            hover_color="#566573",
                                            text_font=None,
                                            text="Test Button 6",
                                            text_color="#ABB2B9",
                                            corner_radius=0,
                                            border_width=2,
                                            width=120,
                                            height=40,
                                            hover=True,
                                            command=self.test_function)
        self.button_6.place(relx=0.66, rely=0.6, anchor=tkinter.CENTER)

        # ========== other shapes =============

        self.button_7 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#58636F",
                                            border_color=None,
                                            hover_color="#808B96",
                                            text_font=None,
                                            text="B 7",
                                            text_color="white",
                                            corner_radius=10,
                                            border_width=0,
                                            width=45,
                                            height=45,
                                            hover=True,
                                            command=self.test_function)
        self.button_7.place(relx=0.33, rely=0.8, anchor=tkinter.CENTER)

        self.button_8 = TkinterCustomButton(master=self,
                                            bg_color=None,
                                            fg_color="#212F3D",
                                            border_color="#117A65",
                                            hover_color="#34495E",
                                            text_font=None,
                                            text="Button 8",
                                            text_color="white",
                                            corner_radius=12,
                                            border_width=4,
                                            width=100,
                                            height=60,
                                            hover=True,
                                            command=self.test_function)
        self.button_8.place(relx=0.66, rely=0.8, anchor=tkinter.CENTER)

        self.running = False

    def test_function(self):
        tkinter.messagebox.showwarning(title="Button Test",
                                       message="Button pressed")

    def about_dialog(self):
        tkinter.messagebox.showinfo(title=APP_NAME,
                                    message=ABOUT_TEXT)

    def on_closing(self, event=0):
        if sys.platform == "darwin":  # macOS
            if Version(tkinter.Tcl().call("info", "patchlevel")) >= Version("8.6.9"):  # Tcl/Tk >= 8.6.9
                os.system("defaults delete -g NSRequiresAquaSystemAppearance")  # turn off dark mode for all apps

        self.destroy()
        self.running = False
        exit()

    def start(self):
        self.running = True
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
