#!/bin/bash

CURRENT_DIR=`pwd`
PIP=`which pip`
EASY=`which easy_install`

if [ ! -z $PIP ] || [ ! -z $EASY ]; then

    echo "1. Installing dependencies, you might be requested to provide your root password"
    
    if [ ! -z $PIP ]; then
        echo "   Installing via pip"
        `which sudo` pip install nltk beautifulsoup4
    else 
        echo "   Installing via easy_install"
        `which sudo` easy_install install nltk beautifulsoup4
    fi
    
    echo "2. Re-exporting PYTHONPATH"
    export PYTHONPATH="${PYTHONPATH}:${CURRENT_DIR}/scr/lib"
    echo "   PYTHONPATH is $PYTHONPATH"

    echo "3. Creating $CURRENT_DIR/etc/awoiafrc.default"

    echo "[Folders]" > $CURRENT_DIR/etc/awoiafrc.default
    echo "dir=$CURRENT_DIR" >> $CURRENT_DIR/etc/awoiafrc.default
    echo "rootdir: %(dir)s" >> $CURRENT_DIR/etc/awoiafrc.default
    echo "datadir: %(dir)s/Data" >> $CURRENT_DIR/etc/awoiafrc.default
    echo "visdir: %(dir)s/vis" >> $CURRENT_DIR/etc/awoiafrc.default
    
    echo "   Content of awoiafrc.default:"
    echo "######################"
    cat $CURRENT_DIR/etc/awoiafrc.default
    echo "######################"
    
    echo "   FINISHED."
else
    echo "##################################"
    echo "Please install pip or easy_install"
    echo "##################################"
fi