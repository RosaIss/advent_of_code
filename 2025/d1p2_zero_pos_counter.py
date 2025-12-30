import sys


def main():
    position = 50
    pzero_count = 0

    for line in sys.stdin:
        direction = line[0]

        val = int(line[1:].strip())
        if val > 100:
            pzero_count += int(val / 100)
            val = val % 100

        if val == 0:
            continue

        if direction == 'R':
            position += val
            
            if position > 100:
                pzero_count += int(position / 100)
                position = position % 100
            elif position == 100:
                pzero_count += 1
                position = 0
        else:
            if position == 0:
                position = 100 - val
            else:
                if position < val:
                    position += 100 - val
                    pzero_count += 1
                elif position > val:
                    position -= val
                else:
                    position = 0
                    pzero_count += 1

    print(f"Zero position counter: {pzero_count}")


if __name__ == "__main__":
    main()