import sys


class FontManager(object):
    """ font sizes need to be different on operating systems
        because on windows the text is displayed much larger """

    def __init__(self):

        if sys.platform == "darwin":  # macOS
            self.button_font = ("Avenir", 18)
            self.note_display_font = ("Avenir", 74)
            self.info_text_font = ("Avenir", 16)
            self.settings_text_font = ("Avenir", 28)

        elif "win" in sys.platform:  # Windows
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)

        else:  # Linux or other
            self.button_font = ("Century Gothic", 14)
            self.note_display_font = ("Century Gothic", 62)
            self.info_text_font = ("Century Gothic", 12)
            self.settings_text_font = ("Century Gothic", 20)