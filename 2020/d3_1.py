"""--- Day 3: Toboggan Trajectory ---"""

import sys

STEP_X = 3
STEP_Y = 1

def parse_input():
    grid = [line[0:-1] for line in sys.stdin]
    return grid


def countTrees(point, max_x, max_y, grid):
    counter = 0

    while point[0] <= max_x and point[1] <= max_y:
        if grid[point[1]][point[0]] == '#':
            counter += 1
        point[0] += STEP_X
        point[1] += STEP_Y

    return counter, point



def main():
    grid = parse_input()
    max_x = len(grid[0]) - 1
    max_y = len(grid) -1
    start_point = [0,0]
    counter = 0

    while start_point[1] < max_y:
        num_trees, start_point = countTrees(start_point, 
                                            max_x,
                                            max_y,
                                            grid)
        
        if start_point[0] > max_x:
            start_point[0] -= len(grid[0])
        
        counter += num_trees   
 
    print("Trees: {}".format(counter))


if __name__ == "__main__":
    main()
