"""--- Day 6: Chronal Coordinates part 1---"""

import sys

def get_shortestdist_coord(from_c, coords):
    dist = 0
    min_dist = None
    twice = False
    c_idx = None 
    
    min_dist = abs(from_c[0] - coords[0][0]) + abs(from_c[1] - coords[0][1])
    c_idx = 0
    for i, c in enumerate(coords[1:]):
        dist = abs(from_c[0] - c[0]) + abs(from_c[1] - c[1])
        
        if min_dist == dist:
            twice = True
        elif min_dist > dist:
            min_dist = dist
            c_idx = i
            twice = False

    if twice:
        return None
    return c_idx



def get_finite_longest_coord(grid, coords):
    mindist_counter = [0] * len(coords)

    for y in xrange(0, grid[1]):
        for x in xrange(0, grid[0]):
            c_idx = get_shortestdist_coord((x,y), coords)
            if c_idx: 
                mindist_counter[c_idx] += 1

                if y == 0 or x == 0 or \
                   x == grid[0] - 1 or y == grid[1] - 1:
                    mindist_counter[c_idx] = float('-inf')
                
    return max(mindist_counter)
    
    

def main():
    grid = None
    coords = []
    xs = None
    ys = None
    coord = None

    for line in sys.stdin:
        line = line[:-1]
        
        coords.append([int(c) + 1 for c in line.split(",")])

    xs, ys = zip(*coords)
    grid = (max(xs) + 2, max(ys) + 2)
    
    area = get_finite_longest_coord(grid, coords)
    print "Coordinate's area: {}".format(area)

if __name__ == "__main__":
    main()
