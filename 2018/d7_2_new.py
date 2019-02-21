"""--- Day 7: The Sum of Its Parts part 1---"""

import sys
import heapq


def get_exec_time(roots, deps, c_deps, num_workers):
    steps_h = roots[:]
    steps = []
    step = None
    s_idx = None
    s_ini = ord("A")
    steps_str = ""

    min_s = None
    wks = []
    new_wks = []
    time = 0

    heapq.heapify(steps_h)

    for s in roots:
        c_deps[ord(s) - s_ini] = -1


    while steps_h or wks:
        steps = []
        new_wks = []

        for _ in xrange(len(wks), num_workers):
            if not steps_h:
                break

            step = heapq.heappop(steps_h)
            wks.append([step, ord(step) - s_ini + 1])


        min_sec = min(wks, key=(lambda x: x[1]))[1]
        time += min_sec

        print min_sec
        print "time " + str(time)
        print wks

        tmp_steps_str = ""
        for s, sec in wks:
            if sec - min_sec:
                new_wks.append([s, sec - min_sec])
            else:
                steps.append(s)
                tmp_steps_str += s

        wks = new_wks
        steps_str += "".join(sorted(tmp_steps_str))

        for s in steps:
            for s_dep in deps[s]:
                s_dep_idx = ord(s_dep) - s_ini
                c_deps[s_dep_idx] -= 1    
                if c_deps[s_dep_idx] == 0:
                    heapq.heappush(steps_h, s_dep)
                    c_deps[s_dep_idx] = -1

    print steps_str
    return time


def main():
    alpha = set()
    alpha_sub = set()
    alpha_deps = dict()
    c_deps = [0] * 26
   
    num_workers = 5
    num_steps = 0

    for line in sys.stdin:
        line = line.split(" ")
        alpha.add(line[1])
        alpha_sub.add(line[7])
        if line[1] in alpha_deps:
            alpha_deps[line[1]].append(line[7])
        else:
            alpha_deps[line[1]] = [line[7]]
            num_steps += 1
            
        if line[7] not in alpha_deps:
            alpha_deps[line[7]] = []
            num_steps += 1

        c_deps[ord(line[7]) - ord("A")] += 1
     
    roots = sorted(alpha - alpha_sub)
    time = get_exec_time(roots, alpha_deps, c_deps, num_workers)
    print "Steps: {}".format(time)
     


if __name__ == "__main__":
    main()
