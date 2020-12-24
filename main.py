#!/usr/bin/env python

import localenv
from localenv import OnLocalEnv
from library.cmder import Commander

if __name__ == '__main__':
    print('Courier universal package manager v0.0.0')
    
    env = localenv.LocalEnv()
    env.initialize()


    with OnLocalEnv() as e:
        f = open('./on.txt', 'w')
        f.close()

