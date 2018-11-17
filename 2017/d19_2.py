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

    def move(self, mv_coord):
        while(True):
            char = self.grid[self.y][self.x]
    
            if char == '+':
                self.steps_counter += 1
                return False
    
            if char == ' ':
                return True
    
            if char.isalpha():
                self.str_path.append(char)
    
            self.y += mv_coord[0] 
            self.x += mv_coord[1] 
            self.steps_counter += 1
    
    def traverse_path(self):
        drtn = self.DOWN
        self.x = self.grid[1].index('|')
        self.y = 1
        char = None
        end_of_grid = False
    
        while(True):
            if drtn == self.UP:
                end_of_grid = self.move((-1, 0)) 
            elif drtn == self.DOWN:
                end_of_grid = self.move((1, 0))
            elif drtn == self.RIGHT:
                end_of_grid = self.move((0, 1))
            else:
                end_of_grid = self.move((0, -1))
     
            if end_of_grid:
                break
    
            y = self.y
            x = self.x
            if drtn != self.DOWN and self.grid[y - 1][x] != ' ':
                drtn = self.UP
                self.y -= 1
            elif  drtn != self.UP and self.grid[y + 1][x] != ' ':
                drtn = self.DOWN
                self.y += 1
            elif drtn != self.LEFT and self.grid[y][x + 1] != ' ':
                drtn = self.RIGHT
                self.x += 1
            else:
                drtn = self.LEFT
                self.x -= 1


def main():
    grid = Grid() 
    grid.fill()
    
    grid.traverse_path()
    print "Number of steps: {}".format(grid.steps_counter) 

if __name__ == "__main__":
    main()

