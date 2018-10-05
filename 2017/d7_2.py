"""Day 7: Recursive Circus part 2"""
import sys
import re

program_dict = {}

def insert_in_program_dict(line):
    program_att = re.split("[, ]+", line)

    if program_att[0] not in program_dict:
        program_dict[program_att[0]]={}
        program_dict[program_att[0]]["repeated"]=0
    else:
        program_dict[program_att[0]]["repeated"]=1

    if len(program_att) > 2:
        program_dict[program_att[0]]["deps"] = program_att[3:]
    else:
        program_dict[program_att[0]]["deps"] = []

    program_dict[program_att[0]]["weight"] = int(program_att[1][1:-1])


    for p in program_att[3:]:
        if p not in program_dict:
            program_dict[p]={}
            program_dict[p]["repeated"] = 0
        else:
            program_dict[p]["repeated"] = 1

def get_root_program():
    for p, att in program_dict.iteritems():
        if not att["repeated"]:
            return p

def find_weight_correction(program):
    """
    Return
        -total_weight or
        -[total_weight, [two potentially erroneous weights]]
        The latter situation happens when there are two deps in the stack
        and the values are different to each other. Hence
        it is not posible to infere which is the right value
        until one of the siblings of the disk in the bottom of the stack
        is proccessed
        eg.
            - ugml + (gyxo + ebii) = 68 + (1 + 2) = 71
            - padx = 70
                ans = 1
    """

    if not program_dict[program]["deps"]:
        return program_dict[program]["weight"]

    dep_num = 0
    weights = {}
    for p in program_dict[program]["deps"]:
        dep_num += 1
        weight_result = find_weight_correction(p)
        if isinstance(weight_result, list):
            if len(weights) == 1:
                if len(program_dict[program]["deps"]) > 1:
                    next_p = program_dict[program]["deps"][2]
                    next_w = find_weight_correction(next_p)
                else:
                    print "Couln't find the error in the program {}".\
                          format(str(weight_result))
                    sys.exit(1)

            ans = weight_result[1][0]
            if (weight_result[0] - weight_result[1][0] +\
                weight_result[1][1]) == next_w:
                ans = weight_result[1][1]
            print "Correct weight: {}".format(str(ans))
            sys.exit(0)

        if weight_result in weights:
            weights[weight_result].append(p)
        else:
            weights[weight_result] = [p]

        keys = weights.keys()
        if len(keys) > 1 and dep_num > 2:
            w1, w2 = None, None
            if len(weights[keys[1]]) == 1:
                w1 = keys[1]
                w2 = keys[0]
            else:
                w1 = keys[0]
                w2 = keys[1]
            ans = program_dict[weights[w1][0]]["weight"] + (w2 - w1)
            print "Correct weight: {}".format(str(ans))
            sys.exit(0)

    keys = weights.keys()
    total_weight = keys[0] * len(weights[keys[0]]) + program_dict[program]["weight"]
    if len(weights.keys()) == 1:
        return total_weight
    return [total_weight, weights.keys()]

for line in sys.stdin:
    insert_in_program_dict(line[:-1])
root_program = get_root_program()
find_weight_correction(root_program)
