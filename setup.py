""" this setup.py file is build for compilation on macOS with py2app"""

import os
import getpass
from setuptools import setup
from settings import Settings

REMOVE_OLD_BUILD = True  # delete /build and /dist

APP = ['main.py']
USER_NAME = getpass.getuser()

SOUND_FILES = ["assets/sounds/drop.wav"]

IMAGE_FILES = ["assets/images/arrowDown_hovered.png",
               "assets/images/arrowDown.png",
               "assets/images/arrowUp_hovered.png",
               "assets/images/arrowUp.png",
               "assets/images/bell_hovered.png",
               "assets/images/bell.png",
               "assets/images/mutedBell_hovered.png",
               "assets/images/mutedBell.png"]

OPTIONS = {'argv_emulation': False,
           'includes': 'numpy, tkinter, PIL, pyaudio, darkdetect',
           'excludes': '',
           'frameworks': '/Users/{}/miniconda3/lib/libffi.6.dylib,'.format(USER_NAME) +
                         '/Users/{}/miniconda3/lib/libtk8.6.dylib,'.format(USER_NAME) +
                         '/Users/{}/miniconda3/lib/libtcl8.6.dylib'.format(USER_NAME),
           # For whatever reason, py2app didn't include these 3 frameworks automatically. (path can be different)
           'iconfile': 'assets/images/GuitarTuner_Icon.icns',
           'plist': {
               'CFBundleName': Settings.APP_NAME,
               'CFBundleDisplayName': Settings.APP_NAME,
               'CFBundleExecutable': Settings.APP_NAME,
               'CFBundleGetInfoString': "Tune your instrument with {}".format(Settings.APP_NAME),
               'CFBundleIdentifier': Settings.CF_BUNDLE_IDENTIFIER,
               'CFBundleVersion': Settings.VERSION,
               'CFBundleShortVersionString': Settings.VERSION,
               'NSRequiresAquaSystemAppearance': False,
               'NSHumanReadableCopyright': u"Copyright © {}, {}, All Rights Reserved".format(Settings.YEAR, Settings.AUTHOR)
           }}


if REMOVE_OLD_BUILD is True:
    os.system("rm -r build")
    os.system("rm -r dist")

setup(name=Settings.APP_NAME,
      app=APP,
      author=Settings.AUTHOR,
      data_files=[("assets/images", IMAGE_FILES), ("assets/sounds", SOUND_FILES)],
      options={'py2app': OPTIONS},
      setup_requires=['py2app'])
