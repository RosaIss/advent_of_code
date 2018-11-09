"""--- Day 13: Packet Scanners part 2 ---"""
import sys


def detect_severity(layers, delay=0):
    severity = 0    

    for i, depth in enumerate(layers):
        ps = i + delay
        if depth == 0:
            continue

        half_round = ps / (depth - 1)
        reminder = ps % (depth - 1)
        if (half_round % 2) == 0 and not reminder:
                return True
            
    return False


def main():
    layers = [0] * 100
    delay = 0
    idx = 0

    for line in sys.stdin:
        idx, depth = line.split(": ")
        layers[int(idx)] = int(depth[:-1])

    while detect_severity(layers, delay) != 0:
        delay += 1
    
    print "Delay to avoid scanner: {}".format(delay)

    
if __name__ == "__main__":
    main()
