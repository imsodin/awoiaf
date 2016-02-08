set -x

AWOIAF_ROOT=/mnt/home/gyachdav/Development/awoiaf

PYTHONPATH="${PYTHONPATH}:/mnt/home/gyachdav/local/lib/python2.7/site-packages:${AWOIAF_ROOT}/scr/lib"
export PYTHONPATH

/usr/bin/python ${AWOIAF_ROOT}/scr/mineCharDetails.py  -c $1
