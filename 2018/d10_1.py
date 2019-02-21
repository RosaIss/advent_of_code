""" """

import sys
import time

class Star():

    def __init__(self, star, x, y, vx, vy):
        self.star = star
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy


def move_stars(stars, sky, sec_x=1, sec_y=1):
    
    for s in stars:
        if s.y >= 0 and s.y < len(sky) and \
           s.x >= 0 and s.x < len(sky[0]) and \
            sky[s.y][s.x] == s.star:
            sky[s.y][s.x] = 0
 
        s.x += s.vx * sec_x
        s.y += s.vy * sec_y

        if s.y >= 0 and s.y < len(sky) and \
           s.x >= 0 and s.x < len(sky[0]):
            sky[s.y][s.x] = s.star
        

def print_sky(sky):
    for line in sky:
        print "".join(['#' if s else '.' for s in line])
    print ""


def main():
    stars = []
    sky = [[0] * 70 for _ in xrange(0, 30)]
    ini_x = 34
    ini_y = 15
    star = 1
    
    x_values = [] 
    y_values = []


    for line in sys.stdin:
        line = line[:-2].replace("<", " ")
        line = line.split()

        x = ini_x + int(line[1][:-1]) 
        y = ini_y + int(line[2][:-1])
        vx = int(line[4][:-1])
        vy = int(line[5])
        s = Star(star, x, y, vx, vy)
        
        stars.append(s)
        if s.y >= 0 and s.y < len(sky) and \
           s.x >= 0 and s.x < len(sky[0]):
            sky[y][x] = s.star

        star += 1
        
        x_values.append(x if x > 0 else x * -1)
        y_values.append(y if y > 0 else y * -1)

    print "min values x{} y{}".format(min(x_values), min(y_values))
    #move_stars(stars, sky, min(x_values), min(y_values))
    move_stars(stars, sky, 10000, 10000)

    print_sky(sky)
    print [(i.x, i.y) for i in stars]

    #while True:
    for i in xrange(0, 100):
        time.sleep(.1)
        move_stars(stars, sky)
        #print_sky(sky)


    print_sky(sky)
    print [(i.x, i.y) for i in stars]
    


if __name__ == "__main__":
    main()
