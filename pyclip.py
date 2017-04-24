import sys

# Clipboard storage
tmp = '/tmp/pyclip.tmp'

if(sys.stdin.isatty()): # Writes tmp to stdout
    with open(tmp, 'r') as clipboard:
        sys.stdout.write(clipboard.read())
elif(sys.stdout.isatty()): # Save stdin to tmp
    with open(tmp, 'w') as clipboard:
        clipboard.write(sys.stdin.read())
 
