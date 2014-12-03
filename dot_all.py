#!/usr/bin/env python
import os
import subprocess
import sys

for dirname, _, filenames in os.walk(sys.argv[1]):
    for fn in filenames:
        base, ext = os.path.splitext(fn)
        if ext == '.dot':
            subprocess.check_call(['dot', '-Tsvg', os.path.join(dirname, fn), '-o', os.path.join(dirname, base + '.svg')])
