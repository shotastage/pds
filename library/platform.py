import platform

from enum import Enum


class OS(Enum):
    macOS = 'macOS'
    Linux = 'Linux'
    Windows = 'NT'

    def judge(self) -> str:
        if platform.system() == 'Darwin':
            return self.macOS
