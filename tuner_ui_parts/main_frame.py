import tkinter
from math import sin, radians

from tuner_ui_parts.custom_button_image import CustomButton
from tuner_ui_parts.custom_button_rounded import RoundedButton
from settings import Settings


class MainFrame(tkinter.Frame):
    def __init__(self, master, *args, **kwargs):
        tkinter.Frame.__init__(self, master, *args, **kwargs)

        self.app_pointer = master
        self.color_manager = master.color_manager
        self.image_manager = master.image_manager
        self.image_manager = master.image_manager

        self.configure(bg=self.color_manager.background_layer_1)

        self.under_canvas = tkinter.Canvas(master=self,
                                           bg=self.color_manager.background_layer_1,
                                           highlightthickness=0)

        self.under_canvas.place(anchor="center",
                                relx=0.5,
                                rely=0.5,
                                height=Settings.CANVAS_SIZE,
                                width=Settings.CANVAS_SIZE)

        self.display_outer_circle = self.under_canvas.create_oval(0,
                                                                  0,
                                                                  Settings.CANVAS_SIZE - 1,
                                                                  Settings.CANVAS_SIZE - 1,
                                                                  fill=self.color_manager.theme_main,
                                                                  width=0)

        self.display_background_line = self.under_canvas.create_line(Settings.CANVAS_SIZE * 0.5,
                                                                     Settings.CANVAS_SIZE * 0.5,
                                                                     Settings.CANVAS_SIZE * 0.5,
                                                                     -Settings.CANVAS_SIZE * 0.5,
                                                                     fill=self.color_manager.background_layer_1,
                                                                     width=Settings.CANVAS_SIZE * 0.06)

        self.needle_width = 9

        self.display_needle = self.under_canvas.create_line(Settings.CANVAS_SIZE * 0.5,
                                                            Settings.CANVAS_SIZE * 0.5,
                                                            Settings.CANVAS_SIZE * 0.5,
                                                            Settings.CANVAS_SIZE * 0.05,
                                                            fill=self.color_manager.needle,
                                                            width=self.needle_width)

        self.display_inner_circle_1 = self.under_canvas.create_oval(Settings.CANVAS_SIZE * 0.2,
                                                                    Settings.CANVAS_SIZE * 0.2,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    fill=self.color_manager.theme_dark,
                                                                    width=0)

        self.botton_frame = tkinter.Frame(master=self, bg=self.color_manager.background_layer_0)
        self.botton_frame.place(relx=0,
                                rely=0.5,
                                relheight=0.5,
                                relwidth=1)

        self.upper_canvas = tkinter.Canvas(master=self.botton_frame,
                                           bg=self.color_manager.background_layer_0,
                                           highlightthickness=0)
        self.upper_canvas.place(anchor="n",
                                relx=0.5,
                                rely=0,
                                height=Settings.CANVAS_SIZE / 2,
                                width=Settings.CANVAS_SIZE)

        self.display_inner_circle_2 = self.upper_canvas.create_oval(Settings.CANVAS_SIZE * 0.2,
                                                                    -Settings.CANVAS_SIZE * 0.3,
                                                                    Settings.CANVAS_SIZE * 0.8,
                                                                    Settings.CANVAS_SIZE * 0.3,
                                                                    fill=self.color_manager.theme_dark,
                                                                    width=0)

        self.note_label = tkinter.Label(master=self,
                                        text="A",
                                        bg=self.color_manager.theme_dark,
                                        fg=self.color_manager.text_2,
                                        font=("Avenir", 80))

        self.note_label.place(relx=0.5,
                              rely=0.5,
                              anchor="center")

        self.button_frequency = RoundedButton(master=self.botton_frame,
                                              bg_color=self.color_manager.background_layer_0,
                                              fg_color=self.color_manager.theme_main,
                                              hover_color=self.color_manager.theme_light,
                                              text_font=("Avenir", 18),
                                              text="440 Hz",
                                              text_color=self.color_manager.text_main,
                                              corner_radius=10,
                                              width=120,
                                              height=45,
                                              hover=False,
                                              function=None)

        self.button_frequency.place(anchor="sw",
                                    relx=0.05,
                                    rely=0.9)

        self.button_info = RoundedButton(master=self.botton_frame,
                                         bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_font=("Avenir", 18),
                                         text="Info",
                                         text_color=self.color_manager.text_main,
                                         corner_radius=10,
                                         width=120,
                                         height=45,
                                         function=self.master.draw_settings_frame)

        self.button_info.place(anchor="se",
                               relx=0.95,
                               rely=0.9)

        self.button_mute = CustomButton(master=self,
                                        bg_color=self.color_manager.background_layer_1,
                                        image_dict={"standard": self.image_manager.bell_image,
                                                    "clicked": self.image_manager.bell_muted_image,
                                                    "standard_hover": self.image_manager.bell_hovered_image,
                                                    "clicked_hover": self.image_manager.bell_muted_hovered_image})
        self.button_mute.place(anchor="ne",
                               relx=0.95,
                               rely=0.05,
                               height=self.image_manager.bell_image.height(),
                               width=self.image_manager.bell_image.width())

    def update_color(self):
        self.configure(bg=self.color_manager.background_layer_1)

        self.under_canvas.configure(bg=self.color_manager.background_layer_1)
        self.under_canvas.itemconfig(self.display_background_line, fill=self.color_manager.background_layer_1)
        self.under_canvas.itemconfig(self.display_outer_circle, fill=self.color_manager.theme_main)
        self.under_canvas.itemconfig(self.display_inner_circle_1, fill=self.color_manager.theme_dark)

        self.upper_canvas.configure(bg=self.color_manager.background_layer_0)
        self.upper_canvas.itemconfig(self.display_inner_circle_2, fill=self.color_manager.theme_dark)

        self.note_label.configure(bg=self.color_manager.theme_dark, fg=self.color_manager.text_2)
        self.button_mute.label.configure(bg=self.color_manager.background_layer_1)

        self.botton_frame.configure(bg=self.color_manager.background_layer_0)

        self.button_frequency.configure_color(bg_color=self.color_manager.background_layer_0,
                                              fg_color=self.color_manager.theme_main,
                                              hover_color=self.color_manager.theme_light,
                                              text_color=self.color_manager.text_main)

        self.button_info.configure_color(bg_color=self.color_manager.background_layer_0,
                                         fg_color=self.color_manager.theme_main,
                                         hover_color=self.color_manager.theme_light,
                                         text_color=self.color_manager.text_main)

    def set_needle_color(self, color):
        if color == "green":
            self.under_canvas.itemconfig(self.display_needle, fill=self.color_manager.needle_hit)
        elif color == "red":
            self.under_canvas.itemconfig(self.display_needle, fill=self.color_manager.needle)

    def set_needle_angle(self, deg):
        x = sin(radians(180 - deg))
        y = sin(radians(270 - deg))

        self.under_canvas.coords(self.display_needle,
                                 Settings.CANVAS_SIZE * 0.5,
                                 Settings.CANVAS_SIZE * 0.5,
                                 Settings.CANVAS_SIZE * 0.5 + (Settings.CANVAS_SIZE * 0.45 * x),
                                 Settings.CANVAS_SIZE * 0.5 + (Settings.CANVAS_SIZE * 0.45 * y))
        return x, y
