#!/usr/bin/env bash

before_check()
{
    echo 'Checking environment...'
    if [ -e ~/.pds ]; then
        echo 'pds is already installed!'
        exit 1
    fi
}



# Main
echo
echo '############################################################'
echo '## PDS Installer v0.0.1 Experimental                      ##'
echo '############################################################'
echo

before_check
