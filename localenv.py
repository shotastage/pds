import os

import locations

class LocalEnv():

    def initialize(self):

        # Prepare courier store directory
        if not os.path.isdir(locations.MAIN_STORE):
            os.makedirs(locations.MAIN_STORE)

class OnLocalEnv(object):

    will_enter_wd = None

    def __enter__(self):
        self.will_enter_wd = os.getcwd()
        os.chdir(os.path.join(locations.MAIN_STORE))

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.will_enter_wd)
