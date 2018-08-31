""" Day 3: Spiral Memory part 1 """

import math

def manhattan_dist(dest_port):
    if dest_port == 1:
        return 0

    frac, intg = math.modf(math.sqrt(dest_port))

    if frac == 0 and intg % 2 != 0:
        return intg - 1

    if intg % 2 == 0:
        intg -= 1    

    init_port = pow(intg, 2) 
    dist = (intg + 1) / 2

    return dist + steps_from_init_port(init_port,
                                       dest_port,
                                       intg + 1)

def steps_from_init_port(init_port, dest_port, square_steps):
    
    def calculate_steps(current_port):
        return abs(square_steps / 2 - (current_port - dest_port))

    tmp = init_port + square_steps
    if tmp >= dest_port:
        return calculate_steps(tmp) 
    
    tmp += square_steps
    if tmp >= dest_port:
        return calculate_steps(tmp) 
       
    tmp += square_steps
    if tmp >= dest_port:
        return calculate_steps(tmp) 

    tmp += square_steps
    if tmp >= dest_port:
        return calculate_steps(tmp) 

#I think this is a better implementation of above function
#def steps_from_init_port(init_port, dest_port, square_steps):
#    frac, intg = math.modf((init_port - dest_port) / square_steps)
#
#    if frac != 0:
#        intg += 1
#    current_port = init_port + intg * square_steps 
#    return abs(square_steps / 2 - (current_port - dest_port))
    
dest_port = raw_input()
print manhattan_dist(int(dest_port))
    


        
    
    
    
