"""--- Day 19: A Series of Tubes part 2---"""

import sys
from enum import Enum

class Grid():
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def __init__(self):
        self.grid = []
        self.x = 0
        self.y = 0
        self.str_path = []
        self.steps_counter = 0

    def fill(self):
        it = iter(sys.stdin)
        
        line_val = it.next()[:-1]
        line = [' '] + list(line_val) + [' '] 
        self.grid.append([' '] * (len(line)))
        self.grid.append(line) 
        
        for line_val in it:
            line = [' '] + list(line_val)[:-1] + [' '] 
            self.grid.append(line) 

        self.grid.append([' '] * len(line))
        #self.print_grid()
        
    def print_grid(self):
        for line in self.grid:
            print line 
    

def move(grid, mv_coord):
    while(True):
        char = grid.grid[grid.y][grid.x]

        if char == '+':
            grid.steps_counter += 1
            return False

        if char == ' ':
            return True

        if char.isalpha():
            grid.str_path.append(char)

        grid.y += mv_coord[0] 
        grid.x += mv_coord[1] 
        grid.steps_counter += 1


def traverse_path(grid):
    drtn = Grid.DOWN
    grid.x = grid.grid[1].index('|')
    grid.y = 1
    char = None
    end_of_grid = False

    while(True):
        if drtn == Grid.UP:
            end_of_grid = move(grid, (-1, 0)) 
        elif drtn == Grid.DOWN:
            end_of_grid = move(grid, (1, 0))
        elif drtn == Grid.RIGHT:
            end_of_grid = move(grid, (0, 1))
        else:
            end_of_grid = move(grid, (0, -1))
 
        if end_of_grid:
            break

        y = grid.y
        x = grid.x
        if drtn != Grid.DOWN and grid.grid[y - 1][x] != ' ':
            drtn = Grid.UP
            grid.y -= 1
        elif  drtn != Grid.UP and grid.grid[y + 1][x] != ' ':
            drtn = Grid.DOWN
            grid.y += 1
        elif drtn != Grid.LEFT and grid.grid[y][x + 1] != ' ':
            drtn = Grid.RIGHT
            grid.x += 1
        else:
            drtn = Grid.LEFT
            grid.x -= 1


def main():
    grid = Grid() 
    grid.fill()
    
    traverse_path(grid)
    print "Number of steps: {}".format(grid.steps_counter) 

if __name__ == "__main__":
    main()

