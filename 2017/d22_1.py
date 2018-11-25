"""--- Day 22: Sporifica Virus ---"""

import sys
import pprint



def infect_grid(grid, start_coord, it):
    infected_nodes = 0
    y = start_coord[0]
    x = start_coord[1]
    
    prev_x = x 
    prev_y = y
    if grid[y][x] == ".":
        grid[y][x] = '#'
        infected_nodes += 1
        x -= 1
    else:
        grid[y][x] = '.' 
        x += 1

    for i in xrange(0, it-1):
        if grid[y][x] == '.':
            grid[y][x] = '#'
            if prev_x - x > 0: 
                prev_x = x
                y += 1
            elif prev_x - x < 0:
                prev_x = x
                y -= 1
            elif prev_y - y > 0: 
                prev_y = y
                x -= 1
            else: 
                prev_y = y
                x += 1
            infected_nodes += 1
        else:
            grid[y][x] = '.'
            if prev_x - x > 0:
                prev_x = x
                y -= 1
            elif prev_x - x < 0:
                prev_x = x
                y += 1
            elif prev_y - y > 0: 
                prev_y = y
                x += 1
            else:
                prev_y = y
                x -= 1
            
    return infected_nodes

def main():
    mtx_size = None
    grid = None
    padd = 1000
    it = 10000

    iterline = iter(sys.stdin)
    line = iterline.next()
    row = list(line[:-1])
    mtx_size = len(row)

    grid = [['.'] * (mtx_size + 2 * padd) for i in xrange(0, padd)]
    row = (['.'] * padd) + row
    row += ['.'] * padd
    grid.extend([row])
    
    for line in iterline:
        row = list(line[:-1])
        row = (['.'] * padd) + row
        row += ['.'] * padd
        grid.extend([row])

    grid.extend([['.'] * (mtx_size + 2 * padd) for i in xrange(0, padd)])


    coord = int(padd + (mtx_size / 2))
    #pprint.pprint(grid)
    print "Infected nodes: {}".format(infect_grid(grid, (coord, coord), it))


if __name__ == "__main__":
    main()
