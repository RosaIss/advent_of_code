"""--- Day 1: Chronal Calibration part 2 ---"""

import sys

def main():
    ch_freq = []
    freqs = {0: ''}
    curr_freq = -1
    new_freq = 0    

    for line in sys.stdin:
        line = line[:-1]
        ch_freq.append(int(line))


    while curr_freq != new_freq:
        for chf in ch_freq:
            curr_freq = new_freq     
            new_freq = curr_freq + chf
            if new_freq in freqs:
                curr_freq = new_freq
                break

            freqs[new_freq] = ''

    print "Duplicated frequency: {}".format(new_freq) 

if __name__ == "__main__":
    main()
