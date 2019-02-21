"""--- Day 9: Marble Mania part 2---"""

def get_highest_score(players, num_marbels, mo):
    p = 2
    current_mb = 1
    prev_mb = None
    next_mb = None
    
    for mb in xrange(2, num_marbels + 1):
        if mb % 23 == 0:
            next_mb = mo[current_mb][0]
            for _ in xrange(0, 5):
                next_mb = mo[next_mb][0]

            players[p] += mb + mo[next_mb][0]

            prev_mb = mo[mo[next_mb][0]][0] 
            mo[prev_mb][1], mo[next_mb][0] = next_mb, prev_mb

            current_mb = next_mb
        else:
            mo[mb] = [0,0]
            prev_mb = mo[current_mb][1]
            next_mb = mo[prev_mb][1]
            
            mo[prev_mb][1], mo[mb][1] = mb, mo[prev_mb][1]
            mo[next_mb][0], mo[mb][0] = mb, mo[next_mb][0]

            current_mb = mb

        if p == len(players) - 1:
            p = 0
        else:
            p +=1

    return max(players)


def main():
    line = raw_input()
    line = line.split(" ")
    
    players = [0] * int(line[0])
    num_marbels = int(line[6]) * 100
    marbel_order = {0: [1, 1],  1: [0, 0]}

    score = get_highest_score(players, num_marbels, marbel_order)
    print "Highest score: {}".format(score)

if __name__ == "__main__":
    main()
