"""--- Day 2: Password Philosophy ---"""

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


def isPassValid(min_char, max_char, val_char, password):
    counter_char = 0

    for c in password:
        if val_char == c:
            counter_char += 1
    
    if counter_char >= min_char and counter_char <= max_char:
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
