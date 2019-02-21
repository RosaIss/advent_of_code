""" --- Day 2: Inventory Management System part 1---"""


import sys


def calculate_checksum(ids):
    two_char = 0
    three_char = 0
    size_alpha = 26
    alpha = [0] * size_alpha

    for i in ids:
        alpha = [0] * size_alpha
        for c in i:
            alpha[ord(c) - ord('a')] += 1
        two_char += 1 if 2 in alpha else 0 
        three_char += 1 if 3 in alpha else 0

    return two_char * three_char
 

def main():
    line = None
    checksum = None
    ids = []    

    for line in sys.stdin:
        line = line[:-1]
        ids.append(line)

    checksum = calculate_checksum(ids)

    print "Checksum: {}".format(checksum)


if __name__ == "__main__":
    main()
