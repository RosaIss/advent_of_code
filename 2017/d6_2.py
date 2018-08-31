"""Day 6: Memory Reallocation part 2"""
import re
import math

combinations = {}
numbers = []

def find_loop(numbers):
    iterations = 0
    while(True):
        key = " ".join(map(str,numbers))
        if key in combinations:
            loop_iterations = iterations - combinations[key]
            return iterations, loop_iterations
        combinations[key] = iterations
        iterations += 1
        max_num = max(numbers)
        idx = numbers.index(max_num)
        numbers[idx] = 0
        intg = max_num / len(numbers)
        left = max_num % len(numbers)

        if intg != 0:
            numbers = [n + intg for n in numbers]

        for i, _ in enumerate(numbers[idx + 1:], 1):
            if left == 0:
                break;
            numbers[idx+i] += 1 
            left -= 1

        for i, _ in enumerate(numbers[:idx]):
            if left == 0:
                break;
            numbers[i] += 1
            left -= 1
            

numbers = raw_input()
it, loop_it = find_loop(map(int, re.split("[ \t]+", numbers)))
print "Total iterations: " + str(it)
print "Infinit loop size: " + str(loop_it)
