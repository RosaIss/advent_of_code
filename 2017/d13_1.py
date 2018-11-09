"""--- Day 13: Packet Scanners ---"""
import sys


def calculate_severity(layers):
    severity = 0    

    for i, depth in enumerate(layers):
        if depth == 0:
            continue

        half_round = i / (depth - 1)
        reminder = i % (depth - 1)
        if (half_round % 2) == 0 and not reminder:
            severity += i * depth

    return severity


def main():
    layers = [0] * 100

    idx = 0
    for line in sys.stdin:
        idx, depth = line.split(": ")
        layers[int(idx)] = int(depth[:-1])
    
    print "Severity : {}".format(calculate_severity(layers))
    
if __name__ == "__main__":
    main()
