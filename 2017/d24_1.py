import sys


class Comp():

    def __init__(self, comp):
        self.key = comp

        ports = comp.split("/")
        self.port = ports[0]
        self.free_port = ports[1]
        self.strength = sum(map(int, ports))
        self.max_strength = self.strength
        if ports[0] == ports[1]:
            self.equal_port = True
        else:
            self.equal_port = False
        self.max_bridge = (self.key,)
            


def find_strongest_bridge(comps, visited_comps, comp):
    strength = 0
    max_strength = comp.max_strength
    max_bridge = comp.max_bridge
    cs = comps[comp.free_port]
    #print comp.key
    #print comp.strength
    #print comp.max_strength
    #print [c.key for c in comps[comp.free_port]]
    visited_comps[comp.key][0] = True
    if comp.max_strength == comp.strength:
        #print visited_comps
        #print "---"

        for c in cs:
            #print "for"
            #print "visites {} ?".format(c.key)
            if visited_comps[c.key][0]:
                continue

            strength, sub_bridge = find_strongest_bridge(comps, visited_comps, c)
            #print "calculating max"
            #print comp.key
            #print [c.key for c in comps[comp.free_port]]
            #print strength
            #print comp.strength
            #print comp.max_strength
            #print "***"
            if comp.max_strength < strength + comp.strength:
                comp.max_bridge = (comp.key,) + sub_bridge
                comp.max_strength = strength + comp.strength
        max_strength = comp.max_strength
        max_bridge = comp.max_bridge
    elif comp.equal_port:
        print "entre por aqui plop"
        max_comp_strs = [(c.max_strength, c.max_bridge) \
                         for c in cs \
                         if visited_comps[c.key][0] == False]
        #print max_comp_strs
        #print keys
        if max_comp_strs:
            print "entre por aqui"
            max_comp = sorted(max_comp_strs, key=lambda x: x[0])[-1]
            #print max_comp
            max_strength = max_comp[0] + comp.strength
            max_bridge = (comp.key,) + max_comp[1]

    visited_comps[comp.key][0] = False

    return max_strength, max_bridge


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

    strength, bridge = find_strongest_bridge(comps, visited_comps, start_comp)
    print "Max strength: {}".format(strength)             
    print bridge
    print sum([sum(map(int,c.split("/"))) for c in bridge])


if __name__ == "__main__":
    main()
