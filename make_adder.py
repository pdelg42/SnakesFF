#!/usr/bin/python3

import os
from pathlib import Path

def print_everithing(main_dir = '.', layer = 0):
    with os.scandir(main_dir) as entries:
        for entry in entries:
            name = str(entry.name)
            if os.path.isdir(os.path.join(main_dir, entry.name)):
                # print("\033[1;32m" + name + "\033[1;37m")
                print_everithing(os.path.join(main_dir, entry.name), layer + 1)
            else:
                name = name + '\t\\\n'
                name = os.path.join(main_dir, name)
                name = '\t\t' + name
                # print(name)
                if ".c" in name:
                    f.write(name)

lines_before = []
lines_after = []
with open('Makefile', 'r') as f:
    line = f.readline()
    while line and not "FILES" in line:
        lines_before.append(str(line))
        line = f.readline()
    lines_before.append(str(line))
    while line:
        line = f.readline()
        lines_after.append(str(line))

with open('Makefile', 'w') as f:
    for lineb in lines_before:
        f.write(lineb)
    print_everithing()
    for linea in lines_after:
        f.write(linea)
