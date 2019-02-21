"""--- Day 7: The Sum of Its Parts part 1---"""

import sys
import heapq


def get_steps(roots, deps, c_deps):
    steps_h = roots[:]
    steps = ""
    step = None
    s_idx = None
    s_ini = ord("A")

    heapq.heapify(steps_h)

    for s in roots:
        c_deps[ord(s) - s_ini] = -1


    while steps_h:
        step = heapq.heappop(steps_h)
        steps += step 
       
        for s in deps[step]:
            s_idx = ord(s) - s_ini
            c_deps[s_idx] -= 1    
            if c_deps[s_idx] == 0:
                heapq.heappush(steps_h, s)
                c_deps[s_idx] = -1

    return steps


def main():
    alpha = set()
    alpha_sub = set()
    alpha_deps = dict()
    c_deps = [0] * 26

    for line in sys.stdin:
        line = line.split(" ")
        alpha.add(line[1])
        alpha_sub.add(line[7])
        if line[1] in alpha_deps:
            alpha_deps[line[1]].append(line[7])
        else:
            alpha_deps[line[1]] = [line[7]]
            
        if line[7] not in alpha_deps:
            alpha_deps[line[7]] = []

        c_deps[ord(line[7]) - ord("A")] += 1
     
    roots = sorted(alpha - alpha_sub)

    steps = get_steps(roots, alpha_deps, c_deps)

    print "Steps: {}".format(steps)
     


if __name__ == "__main__":
    main()
