import sys
import re

program_dict = {}

def insert_in_program_dict(line):
    programs = re.split("[, ]+", line)
    if programs[0] not in program_dict:
        program_dict[programs[0]] = 0
    else:
        program_dict[programs[0]] = 1

    for p in programs[3:]:
        if p not in program_dict:
            program_dict[p] = 0
        else:
            program_dict[p] = 1
            
def get_root_program():
    for p, repeated in program_dict.iteritems():
        if not repeated:
            return p 

for line in sys.stdin:
    insert_in_program_dict(line[:-1])
root_program = get_root_program()
print root_program
