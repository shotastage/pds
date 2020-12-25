import subprocess

from typing import NoReturn

class Commander():

    sudo: bool = True
    cmd: str = 'ls'
    args: list[str] = ['-a', '-l']

    def __init__(self, cmd, args, sudo = False):
        self.sudo = sudo
        self.cmd = cmd
        self.args = args

    def run(self) -> NoReturn:
        res = 'pds Commander Error\nNo SHELL response found.'

        if self.sudo:
            args = ['sudo', self.cmd]
            res = subprocess.run(args + self.args, stdout=subprocess.PIPE)
        else:
            args = [self.cmd]
            res = subprocess.run(args + self.args, stdout=subprocess.PIPE)
