from pyaudio import PyAudio, paInt16
from threading import Thread
import numpy as np
import sys
import matplotlib.pyplot as plt

from settings import Settings


class AudioAnalyzer(Thread):
    def __init__(self, queue, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)

        self.queue = queue
        self.buffer = np.zeros(Settings.CHUNK_SIZE * Settings.BUFFER_TIMES)
        self.running = False

        try:
            self.audio_object = PyAudio()
            self.stream = self.audio_object.open(format=paInt16,
                                                 channels=1,
                                                 rate=Settings.SAMPLING_RATE,
                                                 input=True,
                                                 output=False,
                                                 frames_per_buffer=Settings.CHUNK_SIZE)
        except Exception as e:
            sys.stderr.write('Error: Line {} {} {}\n'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e))
            return

    @staticmethod
    def freq_to_number(f, a4_freq):
        if f == 0:
            sys.stderr.write("Error: No frequency data. Program has potentially no access to microphone\n")
            return 0
        return 12 * np.log2(f / a4_freq) + 69

    @staticmethod
    def number_to_freq(n, a4_freq):
        return a4_freq * 2.0**((n - 69) / 12.0)

    @staticmethod
    def note_name(n):
        return Settings.NOTE_NAMES[int(round(n) % 12)]


    def run(self):
        """Main command where the microphone buffer gets read and
           the fourier transformation gets applied"""

        self.running = True

        while self.running:
            try:
                data = self.stream.read(Settings.CHUNK_SIZE, exception_on_overflow=False)
                data = np.frombuffer(data, dtype=np.int16)

                self.buffer[:-Settings.CHUNK_SIZE] = self.buffer[Settings.CHUNK_SIZE:]
                self.buffer[-Settings.CHUNK_SIZE:] = data

                numpydata = abs(np.fft.fft(self.buffer))
                numpydata = numpydata[:int(len(numpydata) / 2)]

                frequencies = np.fft.fftfreq(len(numpydata), 1. / Settings.SAMPLING_RATE)
                print(len(frequencies), len(numpydata), frequencies[20000], numpydata[20000])

                self.queue.put(round(frequencies[np.argmax(numpydata)], 2))

            except Exception as e:
                sys.stderr.write('Error: Line {} {} {}\n'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, e))

        self.stream.stop_stream()
        self.stream.close()
        self.audio_object.terminate()
