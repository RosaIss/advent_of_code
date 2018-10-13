"""Day 8: I Heard You Like Registers part 2"""

import sys

max_val = None
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
    return registers[tokens[0]]

def set_max_val_reg(line):
    global max_val
    reg_val = evaluate_exp(line)

    if not max_val or reg_val > max_val: 
        max_val = reg_val


for line in sys.stdin:
    set_max_val_reg(line)
print "Max register's value: {}".format(max_val)
