
import sys
import time

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
            last_snd = lts[opd1]            
            continue            

        if opt == "rcv" and opd1 != 0:
            return last_snd

        opd2 = ins[2]
        if opd2[0] == "-":
            opd2 = 0 - int(opd2[1:]) 
        elif opd2.isdigit():
            opd2 = int(opd2)
        else:
            opd2 = int(lts[opd2])

        if opt == "jgz" and lts[opd1] > 0:
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
