import kaon
import threading
from xv import xv_main

class XVEntity(object):
    def __init__(self, params):
       self.params = params
       self.xv_thread = None
       self.stopping_backreference = lambda: False
       self.reconfigure()

    def get(self):
        return self.params

    def set(self, value):
        self.params = value
        self.reconfigure()

    def reconfigure(self):
        if self.xv_thread != None:
            self.stopping_backreference = lambda: True
            self.xv_thread.join()
        self.stopping_backreference = lambda: False
        self.xv_thread = threading.Thread(
            target= xv_main,
            args= (self.params, self.stopping_backreference)
        )
