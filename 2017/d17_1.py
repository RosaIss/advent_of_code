"""--- Day 17: Spinlock ---"""

def fill_arr(arr, total_numbers, steps):
    last_num = 0
    last_pos = 0 
    pos = 0

    while(last_num < total_numbers):
        last_num += 1
        pos_left = last_pos - pos

        if len(arr) < steps:
            rem = (steps - pos_left) % len(arr)
            if rem == 0:
                pos = last_pos + 1
            else:
                pos = rem
        elif pos_left > steps:
            pos += steps + 1
        else:
            pos = steps - pos_left
 
        arr.insert(pos, last_num)
        last_pos += 1
    
    return pos


def main():
    total_numbers = 2017
    arr = [0]
    steps = raw_input()    
    steps = int(steps)  

    pos_last_num = fill_arr(arr, total_numbers, steps)
    
    pos_after_last_num = pos_last_num + 1
    if pos_last_num == total_numbers:
        pos_after_last_num = 0
    
    print "Number after '{}': {}".format(total_numbers,
                                         arr[pos_after_last_num])

if __name__ == "__main__":
    main()




