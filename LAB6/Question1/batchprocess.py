import subprocess
import sys
BINARY = './subprocess'
if len(sys.argv) != 2:
    print('Usage: Programname Inputfile')
    sys.exit(-1)
    
try:
    with open(sys.argv[1]) as file:
        inputstr = file.read()
        foo = inputstr.split()
        for x in foo:
            cmd = BINARY+' '+x.strip()
            #print(cmd)
            subprocess.run(cmd.split())
except FileNotFoundError as fnf_error:
    print(fnf_error)
    