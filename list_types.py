# coding=utf-8
# Утилита для подсчёта файлов в структуре каталогов с разбивкой по расширениям

import sys
from pathlib import Path

if len(sys.argv) != 2:
    print('Использование: python3 list_types.py <Имя каталога>')
    exit(0)

exts = dict()


def recursive_pass(directory):
    for child in directory.iterdir():
        if child.is_dir():
            recursive_pass(child)
        else:
            if len(child.suffix) > 0:
                suffix = child.suffix.lower()[1:]
                exts[suffix] = exts.get(suffix, 0) + 1


recursive_pass(Path(sys.argv[1]))

for ext in exts.keys():
    print("%s: %d" % (ext, exts[ext]))
