"""--- Day 3: No Matter How You Slice It part 2---"""

import sys

class Rectangule():
    
    def __init__(self, id_r, paddx, paddy, x, y):
        self.id_r = id_r
        self.paddx = paddx
        self.paddy = paddy
        self.x = x
        self.y = y
        self.overlaped = False

def mark_rect_in_fabric(fabric, rects):
    for r in rects:
        for y in xrange(r.paddy, r.paddy + r.y):
            for x in xrange(r.paddx, r.paddx + r.x):
                if fabric[y][x] == None:
                    fabric[y][x] = r
                else:
                    r.overlaped = True
                    fabric[y][x].overlaped = True
                    fabric[y][x] = r
                    
def main():
    fabric_size = 1000
    fabric = [[None] * fabric_size for _ in xrange(0, fabric_size)]
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
        

    mark_rect_in_fabric(fabric, rects)
    rect_id = [r.id_r for r in rects if not r.overlaped][0]
    print "Non overlaped rectangule: {}".format(rect_id)
              


if __name__ == "__main__":
    main()   

