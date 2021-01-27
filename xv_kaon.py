import threading

class XVEntity(object):
    def __init__(self, params):
       self.params = params


    def get(self):
        return self.params

    def set(self, value):
        self.params = value