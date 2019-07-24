#! /bin/bash

function print_help
{
    printf "Usage\n";
    printf "  install [options]\n"
    printf "Install LAAS python libraries for Nephelae project."
    printf "This script is using pip3 to install packages."
    printf "Installing directly using pip3 with the setup.py file is also possible,"
    printf "but it submodule code must previously be fetched using :"
    printf "      git submodule init && git submodule update\n"
    printf "Options"
    printf "  -o <pip-arguments>      = String of options to be passed to pip3.\n"
}

# parsing options
while getopts ":o:h" opt; do
    case ${opt} in
        h )
            print_help; exit 2;;
        o )
            PIPOPTIONS=$OPTARG ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2;
            print_help; exit 2;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2;
            print_help; exit 2;;
    esac
done

# getting directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

( cd $DIR ; git submodule init && git submodule update )

pip3 install $PIPOPTIONS $DIR



