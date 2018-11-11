"""--- Day 15: Dueling Generators ---"""

import sys

def get_num_matching_gen(gen_a, gen_b, it):
    fact_a = 16807
    fact_b = 48271
    num_match = 0

    div = 2147483647    

    for _ in xrange(0, it):
        gen_a *= fact_a 
        gen_b *= fact_b
        
        gen_a %= div
        gen_b %= div

        bin_a = "{:0>16}".format(bin(gen_a)[2:][-16:]) 
        bin_b = "{:0>16}".format(bin(gen_b)[2:][-16:])

        num_match += 1 if bin_a == bin_b else 0
        
    return num_match
        


def main():
    iterations = 40000000
    
    lines = iter(sys.stdin)
    gen_a = lines.next().split(" ")[4]
    gen_b = lines.next().split(" ")[4]

    gen_a = gen_a[:-1]
    gen_b = gen_b[:-1]

    #print "{} {}".format(gen_a, gen_b)

    print "Matching generators: {}".format(get_num_matching_gen(int(gen_a),
                                                                int(gen_b),
                                                                iterations))

if __name__ == "__main__":
    main()
