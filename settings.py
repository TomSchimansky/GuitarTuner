
class Settings:
    """ GuitarTuner global app configuration """

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = "3.0"
    AUTHOR = "Tom Schimansky"
    YEAR = "2021"

    GITHUB_API_URL = "https://api.github.com/repos/TomSchimansky/GuitarTuner"
    GITHUB_URL = "https://github.com/TomSchimansky/GuitarTuner"

    USER_SETTINGS_PATH = "/assets/user_settings/user_settings.json"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 450  # window size when starting the app
    HEIGHT = 440

    MAX_WIDTH = 600  # max window size
    MAX_HEIGHT = 500

    FPS = 60  # canvas update rate
    CANVAS_SIZE = 300  # size of the audio-display

    """ audio settings """
    CHUNK_SIZE = 1024  # samples
    BUFFER_TIMES = 48  # buffer length = CHUNK_SIZE * BUFFER_TIMES
    ZERO_PADDING = 3  # times the buffer length
    SAMPLING_RATE = 44100

    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    NEEDLE_BUFFER_LENGTH = 12
    HITS_TILL_NOTE_NAME_UPDATE = 6
