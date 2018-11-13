"""--- Day 16: Permutation Promenade part 2---"""

def get_final_array(arr, ops):
    off = 0
    a = ord('a')
    
    for op in ops:
        if op[0] == 'p':
            c1, c2 = map(ord, op[1:].split("/"))
            
            p1, p2 = [p for p, c in enumerate(arr) if c1 == c or c2 == c]
            arr[p1], arr[p2] = arr[p2], arr[p1]

            continue

        if op[0] == 'x':
            p1, p2 = map(int, op[1:].split("/"))
            
            p1 += off
            if p1 >= len(arr):
                p1 -= len(arr)

            p2 += off
            if p2 >= len(arr):            
                p2 -= len(arr)

            arr[p1], arr[p2] = arr[p2], arr[p1]

            continue
        
        if int(op[1:]) > 0:    
            last_p = off + len(arr)
            if last_p > len(arr):
                last_p -= len(arr)

            off = last_p - int(op[1:])
            if off < 0:
                off += len(arr)

    arr = arr[off:] + arr[:off]

    return arr


def iter_until_orig_array(orig_arr, arr, ops):
    it = 1
    new_arr = get_final_array(arr, ops)
    while(True):
        if orig_arr != new_arr:
            new_arr = get_final_array(new_arr, ops)
            it += 1
        else:
            break

    return it
        

def main():
    ops = raw_input()

    orig_arr = range(ord('a'), ord('p') + 1)
    arr = range(ord('a'), ord('p') + 1)
    ops = ops.split(",")

    print "Order: {}".format("".join(map(chr,arr)))

    it = iter_until_orig_array(orig_arr, arr, ops)
    it_left = 1000000000 % it
    
    new_arr = get_final_array(orig_arr, ops)
    for i in xrange(1, it_left):
        new_arr = get_final_array(new_arr, ops)
        
    print "New order: {}".format("".join(map(chr, new_arr)))


if __name__ == "__main__":
    main()
