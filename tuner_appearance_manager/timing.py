import time
import sys


class Timer(object):
    """ Timer makes current thread sleep until time
        of set FPS is over. If time is already over
        the Timer does nothing or prints a warning
        if specified """
    
    def __init__(self, fps, warnings=False):
        self.fps = fps
        self.wait_time = 1/self.fps
        self.last_time = time.time()
        self.warnings = warnings

    def wait(self):
        spend_time = time.time() - self.last_time
        sleep_time = self.wait_time - spend_time

        if sleep_time < 0:
            if self.warnings:
                sys.stderr.write("Warning: Timer delay of {} secs\n".format(round(-sleep_time, 4)))
        else:
            time.sleep(sleep_time)

        self.last_time = time.time()
