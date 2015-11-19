# Some useful utils for gathering source code statistics

I needed to gather some LOC statistics for files in a project, so I wrote these small utils.
All utilities are written in Python 3.

- `list_types.py` — recursively counts files in project with breakdown by extension.
- `count_lines.py` — recursively gathers LOC statistics with breakdown by extension. Accepts a list of extensions 
and a list of encodings to try to parse the files against.