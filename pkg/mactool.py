import platform

from library.cmder import Commander

class MacTool():

    def __init__(self) -> None:
        if platform.system() != 'Darwin':
            raise SystemError

    @staticmethod
    def install_pkg():
        install = Commander('installer', ['-pkg', '-target', '/'], sudo = True)
        install.run()

    @staticmethod
    def install_dmg():
        pass

    def _mount_dmg(self, file):
        cmd = Commander('dskutil', ['mount', file])
        cmd.run()

    def _unmount_dmg(self): pass
