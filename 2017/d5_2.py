""" Day 5: A Maze of Twisty Trampolines, All Alike part 2 """

import sys

def calculate_steps(maze):
    i = 0
    steps = 1
    tmp = None
    end = len(maze)

    while(i + maze[i] < end):
        tmp = maze[i]
        if maze[i] >= 3:
            maze[i] -= 1
        else:
            maze[i] += 1
        i += tmp
        steps += 1
    return steps

maze = []
for i in sys.stdin:
    maze.append(int(i))
print calculate_steps(maze)
