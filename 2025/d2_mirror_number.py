import sys

def main():
    total = 0

    line = sys.stdin.readline()
    num_intervals = line.split(',')

    for ni in num_intervals:
        start, end = ni.split('-')
        
        for num in range(int(start), int(end) + 1):
            strnum = str(num)
            if len(strnum) % 2 != 0:
                continue
            
            i = int(len(strnum) / 2 - 1)
            j = int(len(strnum) - 1)
            mirror_num = True
            while mirror_num and i >= 0:
                if strnum[i] != strnum[j]:
                    mirror_num = False
                i -= 1
                j -= 1

            if mirror_num:
                total += num

    
    print(f"Total: {total}")
    
if __name__ == "__main__":
    main()  
