from subprocess import call

with open('../Data/List_of_characters.txt') as f:
    lines = f.readlines()
for l in lines:
    l = l.replace(" ", "_").replace("'","").strip().rstrip().lstrip()
    call(["qsub", "-j","y", "-o","/dev/null", "/mnt/home/gyachdav/Development/awoiaf/scr/awoiaf_miner.sh",l])


