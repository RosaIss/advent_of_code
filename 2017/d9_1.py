"""--- Day 9: Stream Processing ---"""

def get_total_score(line):
    total_score = 0
    nested = 0
    ignore = False
    # Stack with one element so it's not necessary to check
    # if it's empty before accessing the top
    stack = ["0"] 

    for c in line:
        if ignore:
            ignore = False
            continue

        if c == '!':
            ignore = True
            continue       
     
        if stack[-1] == '<':
            if c == '>':
                stack.pop()
            continue
 
        if c == '<':
            stack.append(c)
            continue

        if c == '{':
            stack.append(c)
            nested += 1
            continue
    
        if c == '}':    
            stack.pop()
            total_score += nested
            nested -= 1

    return total_score


line = raw_input()
print "Total score: {}".format(get_total_score(line))
