""" Day 2: Corruption Checksum part 1 """

import re
import sys

def difference_btw_max_min(line):
    cs = 0
    line = re.split("[ ,/\t]+", line)
    line = sorted([int(j) for j in line])
    cs = line[-1] - line[0]
    return cs

cs = 0
for line in sys.stdin:
    cs += difference_btw_max_min(line)

print cs
