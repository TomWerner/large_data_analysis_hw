#!/usr/bin/env python

import sys;
import re;

l = 3;
for line in sys.stdin:
        (i, k, v, side) = re.split("[ \t]+", line.strip());
        for j in range(1, l + 1):
            if side == 'L':
                print "%s %s %s\t%s L" % (i, j, k, v)
            if side == 'R':
                print '%s %s %s\t%s R' % (j, k, i, v)
