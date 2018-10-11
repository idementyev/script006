#!/usr/bin/env python3

"""
Ping localhost with saving output to file
"""

import os
import subprocess

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-11'

hostname = "localhost"
command = "ping"
args = {'win': ['-w', '1000', '-n', '10'],
        'nix': ['-W', '1', '-c', '10'],}

outfile = '02_14_out.txt'

# use the correct args
# type change: now args is a list
if os.name == 'nt':
    args = args['win']
else:
    args = args['nix']

with open(outfile, 'wb') as of:
    print((command, *args, hostname))
    p = subprocess.Popen((command, *args, hostname), stdout=subprocess.PIPE)
    result = p.communicate()[0]
    print(result.decode('utf-8'))
    of.write(result)