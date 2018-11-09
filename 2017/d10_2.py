"""--- Day 10: Knot Hash part 2 ---"""

def get_hash(num, seq, current_p=0, skip=0):
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
    
    return num, current_p, skip

def get_sparse_hash(num, seq, current_p, skip, it):
    for i in xrange(0, it):
        num, current_p, skip = get_hash(num, seq, current_p, skip)
    return num
        
def get_knot_hash(num):
    block = 16
    hashed_num = []
    
    for i in xrange(0, 256, block):
        tmp = hex(reduce((lambda x, y: x ^ y), num[i:i + block]))
        hashed_num.append("{:0>2}".format(tmp[2:]))
    
    return "".join(hashed_num)


str_in = raw_input()
suffix_values = [17, 31, 73, 47, 23]
seq = map(ord, str_in) + suffix_values

hashed_num, pos, skip = get_hash(range(0,256), seq) 
hashed_num = get_sparse_hash(hashed_num, seq, pos, skip, 63) 
knot_hash = get_knot_hash(hashed_num)
print "Knot hash: {}".format(knot_hash)
