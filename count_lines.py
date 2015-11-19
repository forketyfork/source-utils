# coding=utf-8
# Utility for recursively calculating total line count in files with breakdown by extension

import sys
from pathlib import Path

if len(sys.argv) != 4:
    print('Usage: python3 count_lines.py <root directory name> <comma-separated extensions list> '
          '<comma-separated encodings list>')
    exit(0)

root_dir = sys.argv[1]
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
                print("Failed to count lines in file: %s" % child)


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
    except UnicodeDecodeError:
        return False
    finally:
        if f is not None:
            f.close()


root_path = Path(root_dir)

recursive_pass(root_path)

for ext in counts.keys():
    print("%s: %d lines" % (ext, counts[ext]))

print("Total: %d lines" % total)
