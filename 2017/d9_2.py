"""--- Day 9: Stream Processing part 2---"""

def get_garbage_counter(line):
    ignore = False
    garbage_counter = 0
    garbage_char_found = False

    for c in line:
        if ignore:
            ignore = False
            continue

        if c == '!':
            ignore = True
            continue

        if garbage_char_found:
            if c == '>':
                garbage_char_found = False
            else:
                garbage_counter += 1
            continue
 
        if c == '<':
            garbage_char_found = True
            continue

    return garbage_counter 


line = raw_input()
print "Total garbage: {}".format(get_garbage_counter(line))
