"""--- Day 20: Particle Swarm ---"""

import sys
import re 
import copy

class Point():

    def __init__(self, p, v, a, p_id):
        self.p = p
        self.v = v
        self.a = a
        self.p_id = p_id
        self.distance = self._get_distance()

    def move(self):
        self.v = [v + a for v, a in zip(self.v, self.a)]
        self.p = [p + v for p, v in zip(self.p, self.v)] 
        
        self.distance = self._get_distance()

    def _get_distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])


def get_closest_to_orig(points, times):
    closest_times = [0] * 1000
    closest_points = []
    closest_point = copy.copy(points[0])

    for point in points[1:]:
        if point.distance < closest_point.distance: 
            closest_point = copy.copy(point)
    closest_points.append(closest_point)
    closest_times[closest_point.p_id] += 1
    
    while(True):
        for _ in xrange(0, times):
            points[0].move()
            closest_point = copy.copy(points[0])
            for point in points[1:]:
                point.move()
                if point.distance < closest_point.distance: 
                    closest_point = copy.copy(point)
            closest_points.append(closest_point)
            closest_times[closest_point.p_id] += 1

        #for point in closest_list:
        #    print "p={} v={} a={} p_id {} dist {}".\
        #           format(point.p, point.v, point.a, 
        #                  point.p_id, point.distance)
        print "More times close from orig: p {}".\
              format(closest_times.index(max(closest_times)))    


def main():
    # Print results after 'times' iterations
    times = 1000
    points = []
    closest_dist = None
    idx = None

    for i, line in enumerate(sys.stdin):
        val = re.sub("[pav<>= /\n]", "", line)
        val = val.split(",")
        p = map(int, val[:3])
        v = map(int, val[3:6])
        a = map(int, val[6:])        
        points.append(Point(p, v, a, i))
    
    get_closest_to_orig(points, times)


if __name__ == "__main__":
    main()
