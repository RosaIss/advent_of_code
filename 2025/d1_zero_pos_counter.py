import sys


def main():
    position = 50
    pzero_count = 0

    for line in sys.stdin:
        direction = line[0]

        val = int(line[1:].strip())
        if val > 100:
            val = val % 100

        if direction == 'R':
            position += val
        else:
            if position - val < 0:
                position += 100
            position -= val
        
        if position % 100 == 0:
            pzero_count += 1

    print(f"Zero position counter: {pzero_count}")


if __name__ == "__main__":
    main()