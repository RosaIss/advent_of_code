"""--- Day 12: Digital Plumber ---"""

import sys

# the index of the list corresponds to the
# program's id. Each index contains:
# [Does the current program have a way to program 0?,
#  [programs linked to the current program]]
programs = []


def get_progs_of_group(prog_id):
    stack = []
    num_progs = 1

    programs[prog_id][0] = True
    for p_id in programs[prog_id][1]:
        stack.append(p_id)

    while(len(stack) != 0):
        p_id = stack.pop()
        if not programs[p_id][0]:
            num_progs += 1
            programs[p_id][0] = True
            stack.extend(programs[p_id][1])

    return num_progs

for i in sys.stdin:
    program = i[:-1]
    program = program.split(" ", 2)
    programs.append([False, [int(p) for p in program[2].split(", ")]])

print "Number of programs: {}".format(get_progs_of_group(0))

