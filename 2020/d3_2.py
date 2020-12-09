"""--- Day 3: Toboggan Trajectory - part 2---"""

import sys

STEP_X = 3
STEP_Y = 1

def parse_input():
    grid = [line[0:-1] for line in sys.stdin]
    return grid


def countTrees(point, max_x, max_y, step_x, step_y, grid):
    counter = 0

    while point[0] <= max_x and point[1] <= max_y:
        if grid[point[1]][point[0]] == '#':
            counter += 1
        point[0] += step_x
        point[1] += step_y

    return counter, point


def run(step_x, step_y, grid):
    max_x = len(grid[0]) - 1
    max_y = len(grid) -1
    start_point = [0,0]
    counter = 0
    
    while start_point[1] < max_y:
        num_trees, start_point = countTrees(start_point, 
                                            max_x, max_y,
                                            step_x, step_y,
                                            grid)
        
        if start_point[0] > max_x:
            start_point[0] -= len(grid[0])
        
        counter += num_trees   

    print("Trees: {}".format(counter))
    return counter


def main():
    grid = parse_input()
    slopes = [(1,1), (3,1), (5,1,), (7,1), (1,2)]    
    results = 1    

    for step_x, step_y in slopes:
        results *= run(step_x, step_y, grid)

    print("Multiplication:{}".format(results))    

if __name__ == "__main__":
    main()
