# coding=utf-8
# Утилита для подсчёта количества строк в исходных кодах

import sys
from pathlib import Path

if len(sys.argv) != 4:
    print('Использование: python3 count_lines.py <Имя каталога> <список расширений через запятую> '
          '<список возможных кодировок через запятую>')
    exit(0)

exts = sys.argv[2].split(',')
encodings = sys.argv[3].split(',')
counts = dict()
total = 0


def recursive_pass(directory):
    for child in directory.iterdir():
        if child.is_dir():
            recursive_pass(child)
        else:
            suffix = child.suffix.lower()[1:]
            if suffix in exts and not count_lines(child):
                print("Не удалось подсчитать количество строк в файле: %s" % child)


def count_lines(file):
    for encoding in encodings:
        if count_lines_with_encoding(file, encoding):
            return True
    return False


def count_lines_with_encoding(file, encoding):
    global total
    f = None
    try:
        f = file.open(encoding=encoding)
        suffix = file.suffix.lower()[1:]
        line_count = sum(1 for _ in f)
        counts[suffix] = counts.get(suffix, 0) + line_count
        total = total + line_count
        return True
    except:
        return False
    finally:
        if f is not None:
            f.close()


root_path = Path(sys.argv[1])

recursive_pass(root_path)

for ext in counts.keys():
    print("%s: %d строк" % (ext, counts[ext]))

print("Итого: %d строк" % total)
