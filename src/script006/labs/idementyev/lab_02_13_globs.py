#!/usr/bin/env python3

"""
Print all files in a directory matching a mask.
Mask is a passed argument.
"""

import argparse
import glob
import os

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-11'

p = argparse.ArgumentParser()
p.add_argument('-m', '--mask', default="*.py", help='Glob mask')
p.add_argument('-d', '--directory', default=".", help='Directory to search in')
args = p.parse_args()

file_mask = args.mask
directory = os.path.abspath(os.path.normpath(args.directory))

for file in glob.glob(os.path.join(directory, "*{}".format(file_mask))):
    print(file)
