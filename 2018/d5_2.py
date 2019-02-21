""" --- Day 5: Alchemical Reduction part 2---"""

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
    alph = [chr(ord('A') + i) for i in xrange(0,26)]
    min_polymer = polymer
    new_polymer = None

    for a in alph:
        new_polymer = filter(lambda c: c.upper() != a, polymer)
        new_polymer = get_new_polymer(new_polymer)

        if len(min_polymer) > len(new_polymer):
            min_polymer = new_polymer

    #print "Polymer: {} ".format(new_polymer)
    print "Number of units: {} ".format(len(min_polymer))


if __name__ == "__main__":
    main()
