""" --- Day 3: No Matter How You Slice It part 1---"""

import sys

class Rectangule():
    
    def __init__(self, id_r, paddx, paddy, x, y):
        self.id_r = id_r
        self.paddx = paddx
        self.paddy = paddy
        self.x = x
        self.y = y

def get_overlaped_inches(fabric, rects): 
    inches = 0
    
    for r in rects:
        for y in xrange(r.paddy, r.paddy + r.y):
            for x in xrange(r.paddx, r.paddx + r.x):
                if fabric[y][x] == 0:
                    fabric[y][x] = 1
                elif fabric[y][x] == 1:
                    fabric[y][x] = 2
                    inches += 1  
            
    return inches


def main():
    fabric_size = 1000
    fabric = [[0] * fabric_size for _ in xrange(0, fabric_size)]
    rects = []
    inches = None
    line = None


    for line in sys.stdin:
        line = line[:-1]
        line = line.replace('#', '')
        line = line.replace(' @', '')
        line = line.replace(':', '')
        line = line.replace(',', ' ')
        line = line.replace('x', ' ')
        line = line.split(" ")
        rects.append(Rectangule(*map(int,line))) 
        

    inches = get_overlaped_inches(fabric, rects)
    print "Overlaped inches: {}".format(inches)
              


if __name__ == "__main__":
    main()   

