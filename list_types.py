# coding=utf-8
# Utility for recursively counting files with breakdown by extension

import sys
from pathlib import Path

if len(sys.argv) != 2:
    print('Usage: python3 list_types.py <root directory name>')
    exit(0)

root_dir = sys.argv[1]

exts = dict()


def recursive_pass(directory):
    for child in directory.iterdir():
        if child.is_dir():
            recursive_pass(child)
        else:
            if len(child.suffix) > 0:
                suffix = child.suffix.lower()[1:]
                exts[suffix] = exts.get(suffix, 0) + 1


recursive_pass(Path(root_dir))

for ext in exts.keys():
    print("%s: %d files" % (ext, exts[ext]))
