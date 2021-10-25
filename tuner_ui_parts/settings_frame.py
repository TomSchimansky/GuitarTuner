import tkinter
import webbrowser

from tuner_ui_parts.tkinter_custom_button_imageset import TkinterCustomButtonImageset
from tuner_ui_parts.tkinter_custom_button import TkinterCustomButton
from settings import Settings


class SettingsFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.app_pointer = master
        self.color_manager = self.app_pointer.color_manager
        self.font_manager = self.app_pointer.font_manager
        self.image_manager = self.app_pointer.image_manager

        self.configure(bg=self.color_manager.background_layer_1)

        self.bottom_frame = tkinter.Frame(master=self,
                                          bg=self.color_manager.background_layer_0)
        self.bottom_frame.place(anchor=tkinter.S, relx=0.5, rely=1, relheight=0.2, relwidth=1)

        self.button_back = TkinterCustomButton(master=self.bottom_frame,
                                               bg_color=self.color_manager.background_layer_0,
                                               fg_color=self.color_manager.theme_main,
                                               hover_color=self.color_manager.theme_light,
                                               text_font=self.font_manager.button_font,
                                               text="Back",
                                               text_color=self.color_manager.text_main,
                                               corner_radius=10,
                                               width=110,
                                               height=40,
                                               command=self.master.draw_main_frame)
        self.button_back.place(anchor=tkinter.SE, relx=0.95, rely=0.75)

        self.button_website = TkinterCustomButton(master=self.bottom_frame,
                                                  bg_color=self.color_manager.background_layer_0,
                                                  fg_color=self.color_manager.theme_main,
                                                  hover_color=self.color_manager.theme_light,
                                                  text_font=self.font_manager.button_font,
                                                  text="Website",
                                                  text_color=self.color_manager.text_main,
                                                  corner_radius=10,
                                                  width=110,
                                                  height=40,
                                                  command=self.website_button)
        self.button_website.place(anchor=tkinter.SW, relx=0.05, rely=0.75)

        self.label_info_text = tkinter.Label(master=self,
                                             bg=self.color_manager.background_layer_1,
                                             fg=self.color_manager.text_2,
                                             font=self.font_manager.info_text_font,
                                             text=Settings.ABOUT_TEXT)
        self.label_info_text.place(anchor=tkinter.CENTER, relx=0.5, rely=0.12, relheight=0.2, relwidth=0.8)

        self.label_note_text = tkinter.Label(master=self,
                                             bg=self.color_manager.background_layer_1,
                                             fg=self.color_manager.text_2,
                                             font=self.font_manager.settings_text_font,
                                             text="A4 =")
        self.label_note_text.place(relx=0.2, rely=0.45, relheight=0.1, relwidth=0.2, anchor=tkinter.CENTER)

        self.label_frequency = TkinterCustomButton(master=self,
                                                   bg_color=self.color_manager.background_layer_1,
                                                   fg_color=self.color_manager.theme_main,
                                                   hover_color=self.color_manager.theme_main,
                                                   text_font=self.font_manager.settings_text_font,
                                                   text="440 Hz",
                                                   text_color=self.color_manager.text_main,
                                                   corner_radius=10,
                                                   width=170,
                                                   height=65,
                                                   hover=False)
        self.label_frequency.place(anchor=tkinter.CENTER, relx=0.5, rely=0.45)

        self.button_frequency_up = TkinterCustomButtonImageset(master=self,
                                                               height=50,
                                                               width=150,
                                                               bg_color=self.color_manager.background_layer_1,
                                                               image_dict={"standard": self.image_manager.arrowUp_image,
                                                                           "clicked": self.image_manager.arrowUp_image,
                                                                           "standard_hover": self.image_manager.arrowUp_image_hovered,
                                                                           "clicked_hover": self.image_manager.arrowUp_image_hovered},
                                                               command=self.frequency_button_up)
        self.button_frequency_up.place(anchor=tkinter.CENTER, relx=0.5, rely=0.3)

        self.button_frequency_down = TkinterCustomButtonImageset(master=self,
                                                                 height=50,
                                                                 width=150,
                                                                 bg_color=self.color_manager.background_layer_1,
                                                                 image_dict={"standard": self.image_manager.arrowDown_image,
                                                                             "clicked": self.image_manager.arrowDown_image,
                                                                             "standard_hover": self.image_manager.arrowDown_image_hovered,
                                                                             "clicked_hover": self.image_manager.arrowDown_image_hovered},
                                                                 command=self.frequency_button_down)
        self.button_frequency_down.place(anchor=tkinter.CENTER, relx=0.5, rely=0.6)

    def update_color(self):
        self.configure(bg=self.color_manager.background_layer_1)
        self.bottom_frame.configure(bg=self.color_manager.background_layer_0)

        self.button_back.configure_color(bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_color=self.color_manager.text_main)

        self.button_website.configure_color(bg_color=self.color_manager.background_layer_0,
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
        if self.master.a4_frequency > 1:
            self.master.a4_frequency -= 1
            self.label_frequency.set_text(str(self.master.a4_frequency) + " Hz")

    def website_button(self):
        webbrowser.open(Settings.GITHUB_URL_README)
