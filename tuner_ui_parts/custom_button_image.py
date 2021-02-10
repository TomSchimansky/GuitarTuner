import tkinter
import sys


class CustomButton(tkinter.Frame):
    """ tkinter custom button with image, takes a
        image_dict with images like the following:

        image_dict = {"standard": ImageTk.PhotoImage,
                      "clicked": ImageTk.PhotoImage,
                      "standard_hover": ImageTk.PhotoImage,
                      "clicked_hover": ImageTk.PhotoImage} """

    def __init__(self, image_dict=None, hover=True, bg_color="black", function=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image_dict = image_dict
        self.pressed = False
        self.bg_color = bg_color
        self.function = function

        self.configure(bg=self.bg_color)

        self.label = tkinter.Label(master=self,
                                   image=image_dict["standard"],
                                   bg=self.bg_color)

        self.label.place(relx=0.5,
                         rely=0.5,
                         anchor=tkinter.CENTER)

        if sys.platform == "darwin" and self.function is not None:
            self.configure(cursor="pointinghand")

        if hover is True:
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        self.bind("<Button-1>", self.clicked)
        self.label.bind("<Button-1>", self.clicked)

    def configure_color(self, bg_color=None):
        if bg_color is not None:
            self.bg_color = bg_color
            self.label.configure(bg=self.bg_color)

    def on_enter(self, event):
        if self.pressed is False:
            self.label.configure(image=self.image_dict["standard_hover"])
        if self.pressed:
            self.label.configure(image=self.image_dict["clicked_hover"])

    def on_leave(self, enter):
        if self.pressed is False:
            self.label.configure(image=self.image_dict["standard"])
        if self.pressed:
            self.label.configure(image=self.image_dict["clicked"])

    def clicked(self, event):
        if self.function:
            self.function()

        if self.pressed is False:
            self.pressed = True
            self.label.configure(image=self.image_dict["clicked"])
        else:
            self.pressed = False
            self.label.configure(image=self.image_dict["standard"])
