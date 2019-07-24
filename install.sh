#! /bin/bash

# getting directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


( cd $DIR ; git submodule init && git submodule update )
pip3 install $DIR



