#!/usr/bin/env python

import localenv
from localenv import OnLocalEnv
from library.cmder import Commander


from config.settings import initialize_settings
if __name__ == '__main__':
    print('Package Deliver System universal package manager v0.0.0')
    
    env = localenv.LocalEnv()
    env.initialize()

    initialize_settings()
    with OnLocalEnv() as e:
        f = open('./on.txt', 'w')
        f.close()

