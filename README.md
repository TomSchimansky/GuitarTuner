![GitHub release (latest by date)](https://img.shields.io/github/v/release/TomSchimansky/GuitarTuner)
![GitHub all releases](https://img.shields.io/github/downloads/TomSchimansky/GuitarTuner/total?color=green&label=macOS%20release%20downloads)
![GitHub Release Date](https://img.shields.io/github/release-date/TomSchimansky/GuitarTuner?color=green)

# GuitarTuner App

![](documentation/readme_images/Preview_Dark.png)

This is a simple **chromatic tuner** designed for guitar tuning, but it should also work with every other instrument.
The played note is automatically recognized through the microphone, and an acoustic signal is
heard when the tuning is correct. If you want you can also change the reference-tone to another
frequency. At the moment, a compiled version is only available for macOS, but you can use it on
Windows too if you run it in the command line.

* Automatic tone detection
* High accuracy: < 0.5 cents (around the A4 area)
* Working from 60 to 2000 Hz (C2 to C7)
* High stability of the pitch indicator
* Support for macOS light and dark-mode

###**➜️ Download macOS app:** [Download here](https://github.com/TomSchimansky/GuitarTuner/releases/tag/3.2)


###**➜️ Download macOS app:** <a href="https://github.com/TomSchimansky/GuitarTuner/releases/tag/3.2"><button type="button" class="btn" style="background-color:#589DF6;color:white;border:none;font-size: 16px;padding:10px 24px;border-radius: 8px;width: 140px;">Download</button></a>

![](documentation/readme_images/Icon_Banner.png)

### Functionality

The app is written in Python with Tkinter, PyAudio and numpy. It uses PyAudio to get access to the raw audio-stream coming from the microphone.
Then a **fast-fourier-transformation** (```numpy.fft```) is applied on the audio-data, which is buffered for about 1.5 seconds.
Then a HPS (Harmonic Product Spectrum) operation is applied to filter the harmonic frequencies.
From the HPS output, you can get the loudest frequency and convert it to a musical note by applying the following
formula: ```12 * numpy.log2(f / a4_frequency) + 69```.

### Run GuitarTuner with python
First you need to install all necessary libraries:
```
pip3 install -r requirements.txt
```
Then you can do:
```
python3 main.py
```
Note that macOS dark-mode **only** works with **anaconda** python version or python.org version 3.10 or later.

So the preferred way to run the program would be with anaconda-python (you have to install miniconda):

```
conda activate base
pip install -r requirements.txt
python main.py
   ...
conda deactivate
```

Install miniconda python version: https://docs.conda.io/en/latest/miniconda.html

### Create standalone application
You can also create a standalone application for macOS or Windows by yourself. For macOS you can use py2app:
```
python3.8 setup.py py2app
```
For windows, you would need to use py2exe instead and modify the setup.py file.

To keep application size as small as possible, make sure you create a virtual environment where you install
only the necessary libraries. The macOS dark-mode currently **only** works with the **anaconda python** Version.
If you compile the app with a python.org version, you have to disable the dark-mode by deleting
the ```'NSRequiresAquaSystemAppearance': False```entry in setup.py, which causes the application window to go
into dark-mode.

![](documentation/readme_images/Preview_Light.png)
