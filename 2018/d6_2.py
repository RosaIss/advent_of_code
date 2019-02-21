"""--- Day 6: Chronal Coordinates part 2---"""

import sys

def calculate_dist(from_c, coords):
    dist = 0
    for c in coords:
        dist += abs(from_c[0] - c[0]) + abs(from_c[1] - c[1])
    
    return dist

def get_area_in_maxdist(max_dist, grid, coords):
    area = 0

    for y in xrange(0, grid[1]):
        for x in xrange(0, grid[0]):
            if calculate_dist((x,y), coords) < max_dist:
                area += 1
                
    return area
    

def main():
    max_dist = 10000
    area = 0
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
    
    area = get_area_in_maxdist(max_dist, grid, coords)
    print "Area with distance less than {}: {}".format(max_dist, area)

if __name__ == "__main__":
    main()
