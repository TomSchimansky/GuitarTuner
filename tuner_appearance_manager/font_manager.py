import sys


class FontManager(object):
    """ font sizes need to be different on operating systems
        because on windows the text is displayed much larger """

    def __init__(self):

        if sys.platform == "darwin":  # macOS
            self.button_font = ("Avenir", 16)
            self.note_display_font = ("Avenir", 72)  # main note Text
            self.note_display_font_medium = ("Avenir", 26)  # text on left and right site
            self.frequency_text_font = ("Avenir", 15)
            self.info_text_font = ("Avenir", 14)
            self.settings_text_font = ("Avenir", 24)

        elif "win" in sys.platform:  # Windows
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.note_display_font_medium = ("Century Gothic", 24)  # text on left and right site
            self.frequency_text_font = ("Century Gothic", 13)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)

        else:  # Linux or other
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.note_display_font_medium = ("Century Gothic", 24)  # text on left and right site
            self.frequency_text_font = ("Century Gothic", 13)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)