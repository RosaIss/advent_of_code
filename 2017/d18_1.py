"""--- Day 18: Duet ---"""

import sys
import time

class Program():

    def __init__(self):
        self.ltrs = {}
        self.rcv_queue = deque()
        self.sended_val = 0
        self.c = 0

def get_val_opd(opd, ltrs):
    if opd[0] == "-":
        return -int(opd[1:]) 
    elif opd.isdigit():
        return int(opd)
    elif opd in ltrs:
        return ltrs[opd]
    
    return 0


def execute_instructions(instructions):
    ins = None 
    opt = None
    opd1 = None
    opd2 = None
    last_snd = None
    lts = {}
    c = 0
    
    while(True):
        ins = instructions[c]
        opt = ins[0] 
        opd1 = ins[1]
        c += 1

        if opt == "snd":
            opd1 = get_val_opd(ins[1], lts)
            last_snd = opd1            
            continue            

        if opt == "rcv" and opd1 != 0:
            if get_val_opd(ins[1], lts) != 0:
                return last_snd
            continue

        opd2 = get_val_opd(ins[2], lts)

        if opt == "jgz":
            opd1 = get_val_opd(ins[1], lts)
            if opd1 > 0:
                c += opd2 - 1
            continue

        if opt == "set":
            lts[opd1] = opd2 
            continue

        if opd1 not in lts:
            lts[opd1] = 0

        if opt == "add":
            lts[opd1] += opd2
            continue

        if opt == "mul":
            lts[opd1] *= opd2
            continue

        if opt == "mod":
            lts[opd1] %= opd2


def main():
    ins = []    

    for line in sys.stdin:
        ins.append(line[:-1].split(" "))

    last_snd = execute_instructions(ins)

    print "Last recovered frequency: {}".format(last_snd)


if __name__ == "__main__":
    main()
