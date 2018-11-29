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
    print opd
    if opd[0] == "-":
        return -int(opd[1:]) 
    elif opd.isdigit():
        return int(opd)
    elif opd in ltrs:
        return ltrs[opd]
    
    return 0


def execute_instructions(instructions):
    p_in_turn = Program(0)
    ins = None  
    opt = None
    opd1 = None
    opd2 = None
    executed_mul_ins = 0
    #print instructions
    
    while(True):
        #print p_in_turn.c
        ins = instructions[p_in_turn.c]
        opt = ins[0] 
        opd1 = ins[1]
        p_in_turn.c += 1
       
        print "" 
        print ins
        print p_in_turn.ltrs     
        opd2 = get_val_opd(ins[2], p_in_turn.ltrs) 

        if opt == "jnz":
            opd1 = get_val_opd(opd1, p_in_turn.ltrs)
            if opd1 != 0: 
                #print " "
                #print opd1
                #print p_in_turn.c
                p_in_turn.c += opd2 - 1 
                #print opd2 
                #print p_in_turn.c
            continue

        if opt == "set":
            p_in_turn.ltrs[opd1] = opd2 
            continue

        if opd1 not in p_in_turn.ltrs:
            p_in_turn.ltrs[opd1] = 0

        if opt == "sub":
            print opd2 
            exit()
            p_in_turn.ltrs[opd1] -= opd2
            continue

        if opt == "mul":
            p_in_turn.ltrs[opd1] *= opd2
            executed_mul_ins += 1
            continue

        return executed_mul_ins


def main():
    ins = []    

    for line in sys.stdin:
        ins.append(line[:-1].split(" "))
 

    print "Num of Mul operations: {}".format(execute_instructions(ins))   
    #p0 = Program(0)
    #p1 = Program(1)

    #while(True):
    #    exc_ins0 = execute_instructions(ins, p0, p1)
    #    exc_ins1 = execute_instructions(ins, p1, p0)

    #    if not exc_ins0 and not exc_ins1:
    #        break 

    #print "Times p1 sended a value: {}".format(p1.sended_val)


if __name__ == "__main__":
    main()
