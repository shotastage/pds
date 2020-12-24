import os
from locations import MAIN_STORE


def initialize_settings():
    with open(os.path.join(MAIN_STORE, 'settings.py'), 'w') as f:
        f.write('# SETTINGS')

class Settings():pass
    load_file = os.path.join(MAIN_STORE, 'settings.py')
