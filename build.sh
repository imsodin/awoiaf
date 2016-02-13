#!/bin/bash

CURRENT_DIR=`pwd`
PIP=`which pip`
EASY=`which easy_install`

if [ ! -z $PIP ] || [ ! -z $EASY ]; then

    echo "1. Installing dependencies, you might be requested to provide your root password"

    if [ ! -z $PIP ]; then
        echo "   Installing via pip"
        `which sudo` pip install nltk beautifulsoup4 requests
    else
        echo "   Installing via easy_install"
        `which sudo` easy_install install nltk beautifulsoup4 requests
    fi

    echo "2. Re-exporting PYTHONPATH"
    export PYTHONPATH="${PYTHONPATH}:${CURRENT_DIR}/scr/lib"
    echo "   PYTHONPATH is $PYTHONPATH"

    echo "   FINISHED."
else
    echo "##################################"
    echo "Please install pip or easy_install"
    echo "##################################"
fi
