"""
For Compilation MacOS you can do:

pip3 install -r requirements.txt
python3 setup.py py2app

"""

import os
from setuptools import setup
from settings import Settings

APP = ['main.py']

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
           'iconfile': 'assets/images/GuitarTunerDesign.icns',
           'plist': {
               'CFBundleName': Settings.APP_NAME,
               'CFBundleDisplayName': Settings.APP_NAME,
               'CFBundleExecutable': Settings.APP_NAME,
               'CFBundleGetInfoString': "Tune your guitar the most simplest way.",
               'CFBundleIdentifier': Settings.CF_BUNDLE_IDENTIFIER,
               'CFBundleVersion': Settings.VERSION,
               'CFBundleShortVersionString': Settings.VERSION,
               'NSRequiresAquaSystemAppearance': False,
               'NSHumanReadableCopyright': u"Copyright © {}, {}, All Rights Reserved".format(Settings.YEAR, Settings.AUTHOR)
           }}

REMOVE_OLD_BUILD = True

if REMOVE_OLD_BUILD is True:
    os.system("rm -r build")
    os.system("rm -r dist")

setup(name=Settings.APP_NAME,
      app=APP,
      author=Settings.AUTHOR,
      data_files=[("assets/images", IMAGE_FILES), ("assets/sounds", SOUND_FILES)],
      options={'py2app': OPTIONS},
      setup_requires=['py2app'])
