import platform

class DebToool():

    def __init__(self) -> None:
        if platform.system() != 'Linux':
            raise SystemError
