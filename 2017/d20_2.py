"""--- Day 20: Particle Swarm part 2 ---"""

import sys
import re 
import copy
import time

class Point():

    def __init__(self, p, v, a, p_id):
        self.p = p
        self.v = v
        self.a = a
        self.p_id = p_id
        self.alive = True

    def move(self):
        self.v = [v + a for v, a in zip(self.v, self.a)]
        self.p = [p + v for p, v in zip(self.p, self.v)] 


def delete_collisions(points, times):

    grid = {}
    for point in points:
        key = "".join(map(str, point.p))
        if key in grid:
            point.alive = False
            grid[key].alive = False
        else:
            grid[key] = point
    
    while(True):
        grid = {}
        for _ in xrange(0, times):
            for point in points:
                if not point.alive:
                    continue

                point.move()
                key = "".join(map(str, point.p))
                if key in grid:
                    point.alive = False
                    grid[key].alive = False
                else:
                    grid[key] = point
                
        #Print particles that are still alived
        #for p in points:
        #    if p.alive:
        #        print "p={} v={} a={} p_id {}". \
        #              format(p.p, p.v, p.a, p.p_id)
        #
        print "Particles alived: {}". \
              format(len([p for p in points if p.alive]))


def main():
    # Print results after 'times' iterations.
    times = 1000
    points = []

    for i, line in enumerate(sys.stdin):
        val = re.sub("[pav<>= /\n]", "", line)
        val = val.split(",")
        p = map(int, val[:3])
        v = map(int, val[3:6])
        a = map(int, val[6:])        
        points.append(Point(p, v, a, i))
    
    delete_collisions(points, times)


if __name__ == "__main__":
    main()
