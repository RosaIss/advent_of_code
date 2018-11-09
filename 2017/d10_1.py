"""--- Day 10: Knot Hash ---"""

def get_hash(num, seq):
    current_p = 0
    skip = 0
    length = len(num)

    for i in seq:
        if i > (length - current_p):
            rev_num = num[current_p:] + \
                  num[:i - (length - current_p)]
            rev_num = rev_num[::-1]

            num[current_p:] = rev_num[:length - current_p]
            num[:i - (length - current_p)] = rev_num[length - current_p:]
        else:
            if current_p == 0:
                num[:i] = num[i-1::-1]
            else:
                num[current_p:current_p + i] = num[current_p + i - 1: \
                                                   current_p - 1:-1]
        
        current_p += i + skip
        if current_p >= length:
            current_p = (current_p - length) % length 
        skip += 1

    return num


seq = raw_input()
seq = [int(n) for n in seq.split(",")]
hash_seq = get_hash(range(0, 256), seq)
print "Hash: {}".format(hash_seq)
print "Multiplication result: {}".format(hash_seq[0] * hash_seq[1])
