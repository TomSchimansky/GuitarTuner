
class Settings:
    """ GuitarTuner global app configuration """

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = "3.0"
    AUTHOR = "Tom Schimansky"
    YEAR = "2021"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 450  # window size when starting the app
    HEIGHT = 440

    MAX_WIDTH = 600  # max window size
    MAX_HEIGHT = 500

    FPS = 60  # canvas update rate
    CANVAS_SIZE = 300  # size of the audio-display

    """ audio settings """
    CHUNK_SIZE = 1024
    BUFFER_TIMES = 64
    SAMPLING_RATE = 44100

    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
