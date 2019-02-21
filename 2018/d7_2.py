"""--- Day 7: The Sum of Its Parts part 2---"""

import sys
import heapq


def get_time_exec(roots, deps, c_deps, workers):
    steps_h = roots
    steps = []
    s_dep_idx = None
    s_ini = ord("A")
    fst_s = s_ini - 2
    snd_s = s_ini - 1
    time_dif = 0
    time = 0
    start = None

    for s in roots:
        c_deps[ord(s) - s_ini] = -1
        

    while steps_h:
        steps = []
        start = 1 if time_dif else 0
        for _ in xrange(start, workers):
            if not steps_h:
                break

            steps.append(heapq.heappop(steps_h))
            
            if fst_s <= snd_s and fst_s < ord(steps[-1]):
                fst_s = ord(steps[-1])
                continue

            if snd_s < fst_s and snd_s < ord(steps[-1]):
                snd_s = ord(steps[-1])
        print "steps"
        print steps
        
        print chr(fst_s) + " " + chr(snd_s)
        time_dif = abs(fst_s - snd_s)
        print time_dif

        if fst_s < snd_s:
            print "entre aquii"
            fst_s, snd_s = snd_s, fst_s

        if snd_s == s_ini - 1:
            time += time_dif
        else:
            time += snd_s - (s_ini - 1) 
        #print str(fst_s)
        #print str(fst_s - (s_ini - 1))
        print "time " + str(time)
        if (fst_s - (s_ini - 1)) == time_dif:
            fst_s = s_ini - 2
            time_dif = 0
        else:
            fst_s -= (snd_s - (s_ini - 1))

        snd_s = s_ini - 1
        
        print "second " + chr(fst_s) + " " + chr(snd_s)

        
        
        for s in steps:
            print "deps"
            print deps[s]
            for s_dep in deps[s]:
                s_dep_idx = ord(s_dep) - s_ini
                c_deps[s_dep_idx] -= 1   
                if c_deps[s_dep_idx] == 0:
                    heapq.heappush(steps_h, s_dep)
                    c_deps[s_dep_idx] = -1
        print "heap"
        print steps_h

    return time


def main():
    alpha = set()
    alpha_sub = set()
    alpha_deps = dict()
    c_deps = [0] * 26
    workers = 2
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

    time = get_time_exec(roots, alpha_deps, c_deps, workers) + num_steps * 60

    print "Execution time in seconds: {}".format(time)
     


if __name__ == "__main__":
    main()
