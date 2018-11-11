"""--- Day 14: Disk Defragmentation part 2 ---"""

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


def add_row_to_mtx(mtx, knot_hash):
    row = []
    for h in knot_hash:
        str_bin = "{:0>4}".format(bin(int(h, 16))[2:])
        # Now, a square set to 0 means it's used and
        # square set to -1 means it's free
        row.extend([int(x) - 1 for x in str_bin])
    mtx.append(row)
    return 
                

def mark_group(mtx, region, r, c):
    if r < 0 or r > 127 or c < 0 or c > 127:   
        return 
    
    if mtx[r][c] == -1 or mtx[r][c] == region:
        return

    mtx[r][c] = region
    
    mark_group(mtx, region, r - 1, c)
    mark_group(mtx, region, r + 1, c)
    mark_group(mtx, region, r, c - 1)
    mark_group(mtx, region, r, c + 1)


def get_regions(mtx):
    region = 0

    for r, row in enumerate(mtx):
        for c, val in enumerate(row):
            if val == 0:
                region += 1
                mark_group(mtx, region, r, c)        
    return region 


def main():
    str_in = raw_input()
    suffix_values = [17, 31, 73, 47, 23]
    mtx = []

    for i in range(0, 128):
        seq = map(ord, str_in + "-" + str(i))
        seq += suffix_values
        hashed_num, pos, skip = get_hash(range(0,256), seq) 
        hashed_num = get_sparse_hash(hashed_num, seq, pos, skip, 63)
        knot = get_knot_hash(hashed_num)
        add_row_to_mtx(mtx, knot)
    
    print "Regions: {}".format(get_regions(mtx))


if __name__ == "__main__":
    main()
