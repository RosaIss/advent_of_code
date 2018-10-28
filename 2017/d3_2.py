"""--- Day 3: Spiral Memory part 2---"""

import math

# set the size to a number that, divided by 2,
# results in 2 symetrical partitions.
#   eg. size = 3, 2 arrays of 1 element
#       size = 5, 2 arrays of 2 elements

size = 900
mtx = [0] * (size * size)
Y = 0 
X = 1


def sum_cord_pos_val(pos, card_pos):
    if card_pos[Y] >= 0 and card_pos[Y] < size and \
       card_pos[X] >= 0 and card_pos[X] < size:
        tmp_pos = card_pos[Y] * size + card_pos[X]
        mtx[pos] += mtx[tmp_pos] 
       
def calculate_pos_val(current_pos, steps, movs, val):
    """
        Return a tuple of two elements.
            (Boolean) The first indicates
                if a greater element than val has been found.
            (Integer) The second is the position
                of the first greater element than val found, or, 
                the position of the last element in the matrix (if a greater 
                element than val couldn't be found)
    """
    for mov in movs:
        #print " "
        for i in xrange(0, steps):
            y = current_pos / size + mov[Y]
            x = current_pos % size + mov[X]
            current_pos = (y * size) + x            

            if current_pos >= len(mtx):
                return False, len(mtx) - 1  

            sum_cord_pos_val(current_pos, (y, x - 1))
            sum_cord_pos_val(current_pos, (y - 1, x - 1))
            sum_cord_pos_val(current_pos, (y + 1, x - 1))
            sum_cord_pos_val(current_pos, (y, x + 1))
            sum_cord_pos_val(current_pos, (y - 1, x + 1))
            sum_cord_pos_val(current_pos, (y + 1, x + 1))
            sum_cord_pos_val(current_pos, (y - 1, x))
            sum_cord_pos_val(current_pos, (y + 1, x))

            if mtx[current_pos] > val:
                return True, current_pos

    return False, current_pos
            
def get_first_greater_val(val):
    pos = (size / 2) * size + (size / 2)
    mtx[pos] = 1
    step = 1

    while(pos > 0):
        gtr_found, pos = calculate_pos_val(pos, step, [(0, 1), (-1, 0)], val)
        step += 1
        if gtr_found or pos == (len(mtx) - 1):
            return mtx[pos]
        gtr_found, pos = calculate_pos_val(pos, step, [(0, -1), (1, 0)], val)
        step += 1    
        if gtr_found or pos == (len(mtx) - 1):
            return mtx[pos]

    return mtx[pos]
    

val = raw_input()
greater_val = get_first_greater_val(int(val))
print "First greater value: {}".format(greater_val)
#print [ v for v in mtx if v != 0]
