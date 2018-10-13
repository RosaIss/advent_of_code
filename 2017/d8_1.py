"""Day 8: I Heard You Like Registers"""

import sys

registers = {}

def add_registers(new_vars):
    for v in new_vars:
        if v.isdigit() or v in registers:
            continue
        registers[v] = 0


def evaluate_exp(line):
    tokens = line.split(" ")
    
    add_registers([tokens[0], tokens[4]])
    exp = "{} {} {}".format(registers[tokens[4]],
                            tokens[5], tokens[6])
    
    if eval(exp):
        if tokens[1] == "inc":
            registers[tokens[0]] += int(tokens[2])
        else:
            registers[tokens[0]] -= int(tokens[2])


def get_max_val_reg():
    max_v = None
    for _, reg_val in registers.iteritems():
        
        if not max_v or reg_val > max_v:
            max_v = reg_val        

    return max_v 

for line in sys.stdin:
    evaluate_exp(line)
print "Max register's value: {}".format(get_max_val_reg())
