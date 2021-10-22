
class Settings:
    """ GuitarTuner global app configuration """

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = "3.1"
    AUTHOR = "Tom Schimansky"
    YEAR = "2021"

    GITHUB_API_URL = "https://api.github.com/repos/TomSchimansky/GuitarTuner"
    GITHUB_URL = "https://github.com/TomSchimansky/GuitarTuner"
    GITHUB_URL_README = "https://github.com/TomSchimansky/GuitarTuner#readme"

    STATISTICS_AGREEMENT = "GuitarTuner uses your IP-address to estimate your " + \
                           "region and collects data on how often the app is being opened.\n" + \
                           "No personal data gets sent and the data is only used to " + \
                           "determine how often the app is really used.\n\n" + \
                           "Do you agree?"

    USER_SETTINGS_PATH = "/assets/user_settings/user_settings.json"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 450  # window size when starting the app
    HEIGHT = 440

    MAX_WIDTH = 600  # max window size
    MAX_HEIGHT = 500

    FPS = 60  # canvas update rate
    CANVAS_SIZE = 300  # size of the audio-display

    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    NEEDLE_BUFFER_LENGTH = 12
    HITS_TILL_NOTE_NAME_UPDATE = 8
