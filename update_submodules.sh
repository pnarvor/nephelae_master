#! /bin/bash

# getting directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $DIR/nephelae_base
git pull
cd $DIR

cd $DIR/nephelae_mapping
git pull
cd $DIR

cd $DIR/nephelae_paparazzi
git pull
cd $DIR

cd $DIR/nephelae_simulation
git pull
cd $DIR


