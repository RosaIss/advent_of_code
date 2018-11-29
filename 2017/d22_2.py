"""--- Day 22: Sporifica Virus part 2 ---"""

import sys



def infect_grid(grid, start_coord, it):
    infected_nodes = 0
    y = start_coord[0]
    x = start_coord[1]
    
    prev_x = x 
    prev_y = y
    if grid[y][x] == ".":
        grid[y][x] = 'W'
        x -= 1
    else:
        grid[y][x] = 'F' 
        x += 1

    for i in xrange(0, it-1):     
        if grid[y][x] == 'W':
            grid[y][x] = '#'
            if prev_x != x:
                prev_x, x = x, (x - prev_x) + x
            else:
                prev_y, y = y, (y - prev_y) + y     
            infected_nodes += 1
   
        elif grid[y][x] == 'F':
            grid[y][x] = '.'
            if prev_x != x:
                prev_x, x = x, (prev_x - x) + x
            else:         
                prev_y, y = y, (prev_y - y) + y     
 
        elif grid[y][x] == '.':
            grid[y][x] = 'W'
            if prev_x != x:
                y = (prev_x - x) + y
                prev_x = x
            else:
                x = (y - prev_y) + x
                prev_y = y

        else:
            grid[y][x] = 'F'
            if prev_x != x:
                y = (x - prev_x) + y
                prev_x = x
            else:
                x = (prev_y - y) + x
                prev_y = y

    return infected_nodes

def main():
    mtx_size = None
    grid = None
    padd = 1000
    it = 10000000

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
    print "Infected nodes: {}".format(infect_grid(grid, (coord, coord), it))


if __name__ == "__main__":
    main()
