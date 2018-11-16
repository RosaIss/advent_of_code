"""--- Day 18: Duet part 2 ---"""

from collections import deque
import sys
import time

class Program():

    def __init__(self, p_id):
        self.ltrs = {'p': p_id}
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


def execute_instructions(instructions, p_in_turn, p):
    ins = None  
    opt = None
    opd1 = None
    opd2 = None
    executed_ins = 0
    
    while(True):
        ins = instructions[p_in_turn.c]
        opt = ins[0] 
        opd1 = ins[1]
        p_in_turn.c += 1
        executed_ins += 1

        if opt == "snd":
            opd1 = get_val_opd(opd1, p_in_turn.ltrs) 
            p.rcv_queue.append(opd1)
            p_in_turn.sended_val += 1           
            continue            

        if opt == "rcv":
            try:
                p_in_turn.ltrs[opd1] = p_in_turn.rcv_queue.popleft()
            except IndexError:
                p_in_turn.c -= 1
                return executed_ins - 1

            continue    

        
        opd2 = get_val_opd(ins[2], p_in_turn.ltrs) 

        if opt == "jgz":
            opd1 = get_val_opd(opd1, p_in_turn.ltrs)
            if opd1 > 0: 
                p_in_turn.c += opd2 - 1
            continue

        if opt == "set":
            p_in_turn.ltrs[opd1] = opd2 
            continue

        if opd1 not in p_in_turn.ltrs:
            p_in_turn.ltrs[opd1] = 0

        if opt == "add":
            p_in_turn.ltrs[opd1] += opd2
            continue

        if opt == "mul":
            p_in_turn.ltrs[opd1] *= opd2
            continue

        if opt == "mod":
            p_in_turn.ltrs[opd1] %= opd2


def main():
    ins = []    

    for line in sys.stdin:
        ins.append(line[:-1].split(" "))
    
    p0 = Program(0)
    p1 = Program(1)

    while(True):
        exc_ins0 = execute_instructions(ins, p0, p1)
        exc_ins1 = execute_instructions(ins, p1, p0)

        if not exc_ins0 and not exc_ins1:
            break 

    print "Times p1 sended a value: {}".format(p1.sended_val)


if __name__ == "__main__":
    main()
