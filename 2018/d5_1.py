""" --- Day 5: Alchemical Reduction part 1---"""

import sys

def get_new_polymer(polymer):
    pol_stack = [polymer[0]]

    for u in polymer[1:]:
        if not pol_stack:
            pol_stack.append(u)
            continue

        if pol_stack[-1] != u and pol_stack[-1].upper() == u.upper():
            pol_stack.pop()
        else:
            pol_stack.append(u)
            
    return "".join(pol_stack)
    

def main():
    
    polymer = raw_input()

    new_polymer = get_new_polymer(polymer)
    print "Polymer: {} ".format(new_polymer)
    print "Number of units: {} ".format(len(new_polymer))


if __name__ == "__main__":
    main()
