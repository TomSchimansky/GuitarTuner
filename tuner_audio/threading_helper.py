from threading import Lock


class ProtectedList(object):
    """ Simple queue to share data between Threads with lock protection.
        Standard buffer length is only 8! """

    def __init__(self, buffer_size=8):
        self.elements = []
        self.buffer_size = buffer_size
        self.lock = Lock()

    def put(self, element):
        self.lock.acquire()

        # append new element at the end of the list
        self.elements.append(element)

        # delete oldest element if list is too long
        if len(self.elements) > self.buffer_size:
            self.elements.pop(0)

        self.lock.release()

    def get(self):
        self.lock.acquire()

        # check if something is in the list
        if len(self.elements) > 0:
            element = self.elements[0]
            del self.elements[0]

        # if list is empty return None
        else:
            element = None

        self.lock.release()
        return element

    def __repr__(self):
        self.lock.acquire()

        string = str(self.elements)

        self.lock.release()
        return string
