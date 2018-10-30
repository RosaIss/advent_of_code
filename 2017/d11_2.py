"""--- Day 11: Hex Ed part 2---"""

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


def add_to_total_steps(mov):
    total_steps = 0
    step_type[mov] += 1

    if mov == "n":
        apply_equivalence("n", "se", "ne")
        apply_equivalence("n", "sw", "nw")
    elif mov == "s":
        apply_equivalence("s", "ne", "se")
        apply_equivalence("s", "nw", "sw")
    elif mov == "ne":
        apply_equivalence("ne", "nw", "n")
        apply_equivalence("ne", "s", "se")
    elif mov == "se":
        apply_equivalence("se", "sw", "s")
        apply_equivalence("se", "n", "ne")
    elif mov == "nw":
        apply_equivalence("nw", "ne", "n")
        apply_equivalence("nw", "s", "sw")
    else:
        apply_equivalence("sw", "se", "s")
        apply_equivalence("sw", "n", "nw")

    apply_class1("n", "s")
    apply_class1("sw", "ne")
    apply_class1("nw", "se")
    
    # Count class 2
    for _, val in step_type.iteritems():
        total_steps += val
    
    return total_steps

steps = raw_input()
#steps = "ne,nw,s"
#steps = "ne,se,nw"
#steps = "nw,s,ne"
total_steps = 0
max_steps = 0
for s in steps.split(","):
    total_steps = add_to_total_steps(s)
    if total_steps > max_steps:
        max_steps = total_steps
print "Max steps: {}".format(max_steps)
