import tkinter
import tkinter.messagebox
import os
import sys
import json
import requests
import webbrowser
import time
import numpy as np
import random
from distutils.version import StrictVersion as Version

from tuner_audio.audio_analyzer import AudioAnalyzer
from tuner_audio.threading_helper import ProtectedList
from tuner_audio.sound_thread import SoundThread

from tuner_appearance_manager.color_manager import ColorManager
from tuner_appearance_manager.image_manager import ImageManager
from tuner_appearance_manager.font_manager import FontManager
from tuner_appearance_manager.timing import Timer

from tuner_ui_parts.main_frame import MainFrame
from tuner_ui_parts.settings_frame import SettingsFrame

try:
    from usage_monitoring import usage_monitor
except ImportError:
    """ Usage monitoring not possible, because the module is missing
     (Github Version is missing the module because of private API key) """
    usage_monitor = None

from settings import Settings


class App(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        if sys.platform == "darwin":  # macOS
            if Version(tkinter.Tcl().call("info", "patchlevel")) >= Version("8.6.9"):  # Tcl/Tk >= 8.6.9
                os.system("defaults write -g NSRequiresAquaSystemAppearance -bool No")  # Only for dark-mode testing!
                # WARNING: This command applies macOS dark-mode on all programs. This can cause bugs on some programs.
                # Currently this works only with anaconda python version (python.org Tcl/Tk version is only 8.6.8).
                pass

        tkinter.Tk.__init__(self, *args, **kwargs)

        self.main_path = os.path.dirname(os.path.abspath(__file__))

        self.color_manager = ColorManager()
        self.font_manager = FontManager()
        self.image_manager = ImageManager(self.main_path)
        self.frequency_queue = ProtectedList()

        self.main_frame = MainFrame(self)
        self.settings_frame = SettingsFrame(self)

        self.audio_analyzer = AudioAnalyzer(self.frequency_queue)
        self.audio_analyzer.start()

        self.play_sound_thread = SoundThread(self.main_path + "/assets/sounds/drop.wav")
        self.play_sound_thread.start()

        self.timer = Timer(Settings.FPS)

        self.needle_buffer_array = np.zeros(Settings.NEEDLE_BUFFER_LENGTH)
        self.tone_hit_counter = 0
        self.note_name_counter = 0
        self.last_note_name = ""
        self.a4_frequency = 440

        self.dark_mode_active = False

        self.title(Settings.APP_NAME)
        self.geometry(str(Settings.WIDTH) + "x" + str(Settings.HEIGHT))
        self.resizable(True, True)
        self.minsize(Settings.WIDTH, Settings.HEIGHT)
        self.maxsize(Settings.MAX_WIDTH, Settings.MAX_HEIGHT)
        self.configure(background=self.color_manager.background_layer_1)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        if sys.platform == "darwin":  # macOS
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)

            menu_bar = tkinter.Menu(master=self)
            app_menu = tkinter.Menu(menu_bar, name='apple')
            menu_bar.add_cascade(menu=app_menu)

            app_menu.add_command(label='About ' + Settings.APP_NAME, command=self.about_dialog)
            app_menu.add_separator()

            self.config(menu=menu_bar)

        elif "win" in sys.platform:  # Windows
            self.bind("<Alt-Key-F4>", self.on_closing)

        self.draw_main_frame()

        if self.read_user_setting("bell_muted") is True:
            self.main_frame.button_mute.set_pressed(True)

        self.open_app_time = time.time()

    @staticmethod
    def about_dialog():
        tkinter.messagebox.showinfo(title=Settings.APP_NAME,
                                    message=Settings.ABOUT_TEXT)

    def draw_settings_frame(self, event=0):
        self.main_frame.place_forget()
        self.settings_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def draw_main_frame(self, event=0):
        self.settings_frame.place_forget()
        self.main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    def manage_usage_stats(self, option, open_times, id):

        # check usage_monitor module could be loaded
        if usage_monitor is not None:

            # check if user agreed on usage statistics
            if self.read_user_setting("agreed_on_usage_stats") is True:

                # send log message with option and open_times data
                 usage_monitor.UsageMonitor.new_log_msg(option, open_times, id)
            else:
                # open dialog to ask for usage statistics permission
                answer = tkinter.messagebox.askyesno(title=Settings.APP_NAME,
                                                     message=Settings.STATISTICS_AGREEMENT)
                if answer is True:
                    # save user permission
                    self.write_user_setting("agreed_on_usage_stats", True)

                    # send log message with option and open_times data
                    usage_monitor.UsageMonitor.new_log_msg(option, open_times, id)
                else:
                    # close program if user doesnt agree
                    self.on_closing()

    def check_for_updates(self):
        if self.read_user_setting("check_for_updates") is True:
            try:
                response = requests.get(Settings.GITHUB_API_URL + "/releases/latest")
                latest_version = response.json()["tag_name"]
            except Exception as err:
                sys.stderr.write(str(err) + "/n")
                return

            if Version(latest_version) > Version(Settings.VERSION):
                answer = tkinter.messagebox.askyesno(title=Settings.APP_NAME,
                                                     message="A new version of this app is available. \n\n" +
                                                             "Do you want to download it?")
                if answer is True:
                    webbrowser.open(Settings.GITHUB_URL + "/releases/latest")
                else:
                    answer = tkinter.messagebox.askyesno(title=Settings.APP_NAME,
                                                         message="Ask again next time? \n\n")
                    if answer is False:
                        self.write_user_setting("check_for_updates", False)

    def write_user_setting(self, setting, value):
        with open(self.main_path + Settings.USER_SETTINGS_PATH, "r") as file:
            user_settings = json.load(file)

        user_settings[setting] = value

        with open(self.main_path + Settings.USER_SETTINGS_PATH, "w") as file:
            json.dump(user_settings, file)

    def read_user_setting(self, setting):
        with open(self.main_path + Settings.USER_SETTINGS_PATH) as file:
            user_settings = json.load(file)

        return user_settings[setting]

    def on_closing(self, event=0):
        self.write_user_setting("bell_muted", self.main_frame.button_mute.is_pressed())
        self.check_for_updates()

        if sys.platform == "darwin":  # macOS
            if Version(tkinter.Tcl().call("info", "patchlevel")) >= Version("8.6.9"):  # Tcl/Tk >= 8.6.9
                os.system("defaults delete -g NSRequiresAquaSystemAppearance")  # Only for dark-mode testing!
                # This command reverts the dark-mode setting for all programs.
                pass

        self.audio_analyzer.running = False
        self.play_sound_thread.running = False
        self.destroy()

    def update_color(self):
        self.main_frame.update_color()
        self.settings_frame.update_color()

    def handle_appearance_mode_change(self):
        dark_mode_state = self.color_manager.detect_os_dark_mode()

        if dark_mode_state is not self.dark_mode_active:
            if dark_mode_state is True:
                self.color_manager.set_mode("Dark")
            else:
                self.color_manager.set_mode("Light")

            self.dark_mode_active = dark_mode_state
            self.update_color()

    def start(self):
        self.handle_appearance_mode_change()

        # handle new usage statistics when program is started
        if self.read_user_setting("id") is None: self.write_user_setting("id", random.randint(10**20, (10**21)-1))
        self.write_user_setting("open_times", self.read_user_setting("open_times")+1)
        self.manage_usage_stats("start", self.read_user_setting("open_times"), self.read_user_setting("id"))

        while self.audio_analyzer.running:

            try:
                # handle the change from dark to light mode, light to dark mode
                self.handle_appearance_mode_change()

                # get the current frequency from the queue
                freq = self.frequency_queue.get()
                if freq is not None:

                    # convert frequency to note number
                    number = self.audio_analyzer.frequency_to_number(freq, self.a4_frequency)

                    # calculate nearest note number, name and frequency
                    nearest_note_number = round(number)
                    nearest_note_name = self.audio_analyzer.number_to_note_name(nearest_note_number)
                    nearest_note_freq = self.audio_analyzer.number_to_frequency(nearest_note_number, self.a4_frequency)

                    # calculate frequency difference from freq to nearest note
                    freq_difference = nearest_note_freq - freq

                    # calculate the frequency difference to the next note (-1)
                    semitone_step = nearest_note_freq - self.audio_analyzer.number_to_frequency(round(number-1),
                                                                                                self.a4_frequency)

                    # calculate the angle of the display needle
                    needle_angle = -90 * ((freq_difference / semitone_step) * 2)

                    # buffer the note name change
                    if nearest_note_name != self.last_note_name:
                        self.note_name_counter += 1

                        if self.note_name_counter >= Settings.HITS_TILL_NOTE_NAME_UPDATE:
                            self.last_note_name = nearest_note_name
                            self.note_name_counter = 0
                        else:
                            nearest_note_name = self.last_note_name
                    else:
                        self.note_name_counter = 0

                    # if needle in range +-5 degrees then make it green, otherwise red
                    if abs(freq_difference) < 0.25:
                        self.main_frame.set_needle_color("green")
                        self.tone_hit_counter += 1
                    else:
                        self.main_frame.set_needle_color("red")
                        self.tone_hit_counter = 0

                    # after 7 hits of the right note in a row play the sound
                    if self.tone_hit_counter > 7:
                        self.tone_hit_counter = 0

                        if self.main_frame.button_mute.is_pressed() is not True:
                            self.play_sound_thread.play_sound()

                    # update needle buffer array
                    self.needle_buffer_array[:-1] = self.needle_buffer_array[1:]
                    self.needle_buffer_array[-1:] = needle_angle

                    # update ui elements
                    self.main_frame.set_needle_angle(np.average(self.needle_buffer_array))
                    self.main_frame.set_note_name(note_name=nearest_note_name)

                    # calculate difference in cents
                    if semitone_step == 0:
                        diff_cents = 0
                    else:
                        diff_cents = (freq_difference / semitone_step) * 100
                    freq_label_text = f"+{round(-diff_cents, 1)} cents" if -diff_cents > 0 else f"{round(-diff_cents, 1)} cents"
                    self.main_frame.set_frequency_difference(freq_label_text)

                    # set current frequency
                    if freq is not None: self.main_frame.set_frequency(freq)

                self.update()
                self.timer.wait()

            except IOError as err:
                sys.stderr.write('Error: Line {} {} {}\n'.format(sys.exc_info()[-1].tb_lineno, type(err).__name__, err))
                self.update()
                self.timer.wait()


if __name__ == "__main__":
    app = App()
    app.start()
