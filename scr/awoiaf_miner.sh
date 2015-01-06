set -x

PYTHONPATH="${PYTHONPATH}:/mnt/home/gyachdav/local/lib/python2.7/site-packages:/mnt/home/gyachdav/Development/awoiaf/scr/lib"
export PYTHONPATH

/usr/bin/python /mnt/home/gyachdav/Development/awoiaf/scr/mineCharDetails.py  -c $1
