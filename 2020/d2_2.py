"""--- Day 2: Password Philosophy - part 2---"""

import sys

def parse_input():
    args = [None]*4

    for line in sys.stdin:
        line = line.split(" ")
        args[0], args[1] = line[0].split("-")
        args[0] = int(args[0])
        args[1] = int(args[1])
        args[2] = line[1][0]    
        args[3] = line[2][0:-1]
        yield args


def isPassValid(pos1, pos2, val_char, password):
    pos1 -= 1
    pos2 -= 1

    if password[pos1] == password[pos2]:
        return False

    if password[pos1] == val_char:
        return True

    if password[pos2] == val_char:
        return True

    return False             


def main():
    policy_pass = parse_input()
    num_valid = 0

    for pp_args in policy_pass:
        if isPassValid(*pp_args):
            num_valid += 1
    
    print("Number of valid passwords: {}".format(num_valid))


if __name__ == "__main__":
    main()
