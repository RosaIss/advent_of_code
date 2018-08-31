""" Day 2: Corruption Checksum part 2 """
import re
import sys

def difference_btw_max_min(line):
    cs = 0
    line = re.split("[ ,/\t]+", line)
    line = sorted([int(j) for j in line])
    
    count = 0
    for i in line:
        count += 1 
        for j in line[count:]:
            if j % i == 0:
                return j / i
    return 0 

cs = 0
for line in sys.stdin:
    cs += difference_btw_max_min(line)

print cs
