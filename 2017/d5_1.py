""" Day 5: A Maze of Twisty Trampolines, All Alike part 1 """

import sys

def calculate_steps(maze):
    i = 0
    steps = 1
    end = len(maze)

    while(i + maze[i] < end):
        maze[i], i = maze[i] + 1, i + maze[i]
        steps += 1
    return steps

maze = []
for i in sys.stdin:
    maze.append(int(i))
print calculate_steps(maze)
