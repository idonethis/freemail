import mmap
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


class FreemailFile(object):

    def __init__(self, filename):
        self.filename = filename

    def __contains__(self, item):
        with open(os.path.join(DATA_DIR, self.filename)) as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            return s.find(item) != -1
        return True


class Freemail(object):

    disposable = FreemailFile("disposable.txt")
    free = FreemailFile("free.txt")

    class __metaclass__(type):
        def __contains__(self, item):
            return any(map(lambda txt: item in txt, [self.disposable, self.free]))
