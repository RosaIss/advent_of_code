"""--- Day 12: Digital Plumber part 2 ---"""

import sys

# the index of the list corresponds to the
# program's id. Each index contains:
# [Does the current program have a way to program 0?,
#  [programs linked to the current program]]
programs = []


def mark_group(prog_id):
    stack = []

    programs[prog_id][0] = True
    for p_id in programs[prog_id][1]:
        stack.append(p_id)

    while(len(stack) != 0):
        p_id = stack.pop()
        if not programs[p_id][0]:
            programs[p_id][0] = True
            stack.extend(programs[p_id][1])


total_groups = 0
for i in sys.stdin:
    program = i[:-1]
    program = program.split(" ", 2)
    programs.append([False, [int(p) for p in program[2].split(", ")]])

for p_id in xrange(0, len(programs)):
    if not programs[p_id][0]:
        total_groups += 1
        mark_group(p_id)

print "Total groups: {}".format(total_groups)

