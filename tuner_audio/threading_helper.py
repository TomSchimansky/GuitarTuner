from threading import Lock


class ProtectedList(object):
    """ Simple queue to share data between Threads with lock protection """

    def __init__(self):
        self.elements = []
        self.lock = self.lock = Lock()

    def put(self, element):
        self.lock.acquire()
        self.elements.append(element)
        self.lock.release()

    def get(self):
        self.lock.acquire()
        if len(self.elements) > 0:
            element = self.elements[0]
            del self.elements[0]
        else:
            element = None
        self.lock.release()
        return element

    def __repr__(self):
        self.lock.acquire()
        string = str(self.elements)
        self.lock.release()
        return string

