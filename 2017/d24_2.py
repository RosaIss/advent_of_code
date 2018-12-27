"""--- Day 24: Electromagnetic Moat part 2---"""

import sys


class Comp():

    def __init__(self, comp):
        self.key = comp

        ports = comp.split("/")
        self.port = ports[0]
        self.free_port = ports[1]
        self.strength = sum(map(int, ports))


def find_longest_bridge(comps, visited_comps, comp):
    max_length = 1
    strength = comp.strength
    bridge = (comp.key,)

    visited_comps[comp.key][0] = True
    for c in comps[comp.free_port]:
        if visited_comps[c.key][0]:
            continue
        new_strength, sub_bridge = find_longest_bridge(comps,
                                                         visited_comps,
                                                         c)
        length = len(sub_bridge) + 1 
        if max_length < length or \
           (max_length == length and comp.strength + new_strength > strength):
            strength = comp.strength + new_strength
            bridge = (comp.key,) + sub_bridge
            max_length = length
    visited_comps[comp.key][0] = False

    return strength, bridge


def add_comp_to_comps(comps, visited_comps, comp):
    visited = [False]
    
    ports = comp.split("/")
    key1 = ports[0]
    key2 = ports[1]

    if key1 in comps:
        comps[key1].append(Comp(comp))
    else:
        comps[key1] = [Comp(comp)]
    visited_comps[comp] = visited

    if key1 != key2:
        rev_comp = "/".join(ports[::-1])
        if key2 in comps:
            comps[key2].append(Comp(rev_comp))
        else:
            comps[key2] = [Comp(rev_comp)]
        visited_comps[rev_comp] = visited

def main():
    start_comp = Comp("0/0")
    comps = {0: [start_comp]}    
    visited_comps = {"0/0": [False]}

    for comp in sys.stdin:
        add_comp_to_comps(comps, visited_comps, comp[:-1])

    strength, bridge = find_longest_bridge(comps, visited_comps, start_comp)
    print "Max length: {}".format(len(bridge))             
    print "Strength: {}".format(strength)             
    print "Bridge:"             
    print bridge

if __name__ == "__main__":
    main()
