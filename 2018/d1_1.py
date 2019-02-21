"""--- Day 1: Chronal Calibration part 1 ---"""

import sys


def main():
    ch_freq = []

    for line in sys.stdin:
        line = line[:-1]
        ch_freq.append(int(line))

    freq = sum(ch_freq)
    print "Resulting frequency: {}".format(freq) 

if __name__ == "__main__":
    main()
