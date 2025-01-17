#!/usr/bin/env python
"""mapper.py"""

import sys
import re
pattern = sys.argv[1]
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        # match the pattern we input by command.
        if re.search(pattern, word):
            print '%s\t%s' % (word, 1)
        else:
            print '%s\t%s' % (word, 0)
