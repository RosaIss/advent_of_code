"""--- Day 11: Hex Ed ---"""

# Step equivalence
# ne-nw -> n
# se-n -> ne
# sw-n -> nw
# se-sw -> s 
# ne-s -> se
# nw-s -> sw
#
# Step combination | Step value
# 
# Class 1
# nw-se, | 0
# sw-ne, | 
# n-s    |
#
# Class 2 
# n, ne, se,  | 1
# nw, sw, s   |
#

step_type = {"n" : 0,
              "s" : 0,
              "nw": 0, 
              "sw": 0,
              "ne": 0,
              "se": 0 }

def apply_equivalence(mov1, mov2, new_mov):
    if step_type[mov1] == 0 or step_type[mov2] == 0:
        return

    if step_type[mov1] < step_type[mov2]:
        step_type[new_mov] += step_type[mov1]
        step_type[mov2] -= step_type[mov1] 
        step_type[mov1] = 0
    else:
        step_type[new_mov] += step_type[mov2]
        step_type[mov1] -= step_type[mov2] 
        step_type[mov2] = 0


def apply_class1(mov1, mov2):
    if step_type[mov1] == 0 or step_type[mov2] == 0:
        return 

    if step_type[mov1] > step_type[mov2]:
        step_type[mov1] -= step_type[mov2]
        step_type[mov2] = 0
    else:
        step_type[mov2] -= step_type[mov1]
        step_type[mov1] = 0


def apply_class2(mov1, mov2):
    if step_type[mov1] == 0 or step_type[mov2] == 0:
        return

    if step_type[mov1] > step_type[mov2]:
        step_type[mov2] = 0
    else:
        step_type[mov1] = 0


def get_total_steps(movs):
    total_steps = 0

    for m in movs:
        step_type[m] += 1

    apply_equivalence("ne", "nw", "n")
    apply_equivalence("se", "sw", "s")
    apply_class1("n", "s")

    apply_equivalence("se", "n", "ne")
    apply_class1("sw", "ne")
    apply_equivalence("sw", "n", "nw")
    apply_class1("nw", "se")

    apply_equivalence("ne", "s", "se")
    apply_class1("nw", "se")
    apply_equivalence("nw", "s", "sw")
    apply_class1("sw", "ne")

    # Count class 2
    for _, val in step_type.iteritems():
        total_steps += val
    
    return total_steps

steps = raw_input()
#steps = "ne,nw,s"
#steps = "ne,se,nw"
#steps = "nw,s,ne"
steps = [s for s in steps.split(",")]
total_steps = get_total_steps(steps)
print "Total steps: {}".format(total_steps)
