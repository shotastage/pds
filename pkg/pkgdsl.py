import yaml

class PackagerDSL():

    def __init__(self, file: str) -> None:
        super().__init__()
        self._file = file
