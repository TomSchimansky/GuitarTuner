import tkinter

from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from settings import Settings


class SettingsFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.app_pointer = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager

        self.configure(bg=self.color_manager.background_layer_1)

        self.bottom_frame = tkinter.Frame(master=self,
                                          bg=self.color_manager.background_layer_0)
        self.bottom_frame.place(relx=0,
                                rely=0.8,
                                relheight=0.2,
                                relwidth=1)

        self.button_back = RoundedButton(master=self.bottom_frame,
                                         bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Back",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_main_frame)

        self.button_back.place(anchor="se",
                               relx=0.95,
                               rely=0.75,
                               height=45,
                               width=120)

        self.label_info_text = tkinter.Label(master=self,
                                             bg=self.color_manager.background_layer_1,
                                             fg=self.color_manager.text_2,
                                             font=("Avenir", 16),
                                             text=Settings.ABOUT_TEXT)

        self.label_info_text.place(anchor="center",
                                   relx=0.5,
                                   rely=0.12,
                                   relheight=0.2,
                                   relwidth=0.8)

        self.label_note_text = tkinter.Label(master=self,
                                             bg=self.color_manager.background_layer_1,
                                             fg=self.color_manager.text_2,
                                             font=("Avenir", 28),
                                             text="A4 =")

        self.label_note_text.place(anchor="center",
                                   relx=0.2,
                                   rely=0.45,
                                   relheight=0.1,
                                   relwidth=0.2)

        self.label_frequency = RoundedButton(master=self,
                                             bg_color=self.color_manager.background_layer_1,
                                             fg_color=self.color_manager.theme_main,
                                             hover_color=self.color_manager.theme_main,
                                             text_font=("Avenir", 28),
                                             text="440 Hz",
                                             text_color=self.color_manager.text_main,
                                             corner_radius=10,
                                             width=170,
                                             height=65,
                                             hover=False)

        self.label_frequency.place(anchor="center",
                                   relx=0.5,
                                   rely=0.45)

        self.button_frequency_up = CustomButton(master=self,
                                                bg_color=self.color_manager.background_layer_1,
                                                image_dict={"standard": self.image_manager.arrowUp_image,
                                                     "clicked": self.image_manager.arrowUp_image,
                                                     "standard_hover": self.image_manager.arrowUp_image_hovered,
                                                     "clicked_hover": self.image_manager.arrowUp_image_hovered},
                                                function=self.frequency_button_up)

        self.button_frequency_up.place(anchor="center",
                                       relx=0.5,
                                       rely=0.3,
                                       height=50,
                                       width=150)

        self.button_frequency_down = CustomButton(master=self,
                                                  bg_color=self.color_manager.background_layer_1,
                                                  image_dict={"standard": self.image_manager.arrowDown_image,
                                                       "clicked": self.image_manager.arrowDown_image,
                                                       "standard_hover": self.image_manager.arrowDown_image_hovered,
                                                       "clicked_hover": self.image_manager.arrowDown_image_hovered},
                                                  function=self.frequency_button_down)

        self.button_frequency_down.place(anchor="center",
                                         relx=0.5,
                                         rely=0.6,
                                         height=50,
                                         width=150)

    def update_color(self):
        self.configure(bg=self.color_manager.background_layer_1)
        self.bottom_frame.configure(bg=self.color_manager.background_layer_0)

        self.button_back.configure_color(bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_color=self.color_manager.text_main)

        self.label_info_text.configure(bg=self.color_manager.background_layer_1, fg=self.color_manager.text_2)
        self.label_note_text.configure(bg=self.color_manager.background_layer_1, fg=self.color_manager.text_2)

        self.label_frequency.configure_color(bg_color=self.color_manager.background_layer_1,
                                             fg_color=self.color_manager.theme_main,
                                             hover_color=self.color_manager.theme_light,
                                             text_color=self.color_manager.text_main)

        self.button_frequency_up.label.configure(bg=self.color_manager.background_layer_1)
        self.button_frequency_down.label.configure(bg=self.color_manager.background_layer_1)

    def frequency_button_up(self):
        self.master.a4_frequency += 1
        self.label_frequency.set_text(str(self.master.a4_frequency) + " Hz")

    def frequency_button_down(self):
        self.master.a4_frequency -= 1
        self.label_frequency.set_text(str(self.master.a4_frequency) + " Hz")
