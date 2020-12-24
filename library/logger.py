import os

class Logger():
    
    logging = ''

    separator = '--------------------------------------------------------------------------------------'


    def __init__(self, separator, prev_logging):
        self.logging = prev_logging
        self.separator = separator

    def write(self): pass
