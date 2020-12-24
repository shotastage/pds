import os
import subprocess

from library.cmder import Commander

class MacTool():

    @staticmethod
    def install_pkg():
        install = Commander('installer', ['-pkg', '-target', '/'], sudo = True)
        install.run()
