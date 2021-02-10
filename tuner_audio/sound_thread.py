from threading import Thread
import pyaudio
import wave
import time


class SoundThread(Thread):
    """ Simple threaded class that takes a path to an audio.wav file
        and the plays it when SoundThread.play_sound() is called. """

    def __init__(self, path_to_file):
        Thread.__init__(self)
        self.running = False
        self.data_chunk_size = 1024

        self.audio_file = wave.open(path_to_file, "rb")
        self.audio_file_data = []

        while True:  # load audio file
            data = self.audio_file.readframes(self.data_chunk_size)
            if data != b'':
                self.audio_file_data.append(data)
            else:
                break

        self.py_audio_object = pyaudio.PyAudio()

        audio_format = self.py_audio_object.get_format_from_width(self.audio_file.getsampwidth())
        self.audio_stream = self.py_audio_object.open(format=audio_format,
                                                      channels=self.audio_file.getnchannels(),
                                                      rate=self.audio_file.getframerate(),
                                                      input=False,
                                                      output=True)
        self.play_sound_now = False
        self.audio_file.close()

    def play_sound(self):
        self.play_sound_now = True

    def run(self):
        self.running = True
        while self.running:

            if self.play_sound_now is True:
                for audio_chunk in self.audio_file_data:
                    self.audio_stream.write(audio_chunk)

                self.play_sound_now = False
                time.sleep(1)
            else:
                time.sleep(0.1)

        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.py_audio_object.terminate()