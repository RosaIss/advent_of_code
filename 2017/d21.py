"""--- Day 21: Fractal Art part 1 and part 2---"""

import math
import sys
import pprint

def get_all_mtx(row):
    eqv = []
    key = reduce(lambda x,y: x + y, row)
    eqv.append("".join(key))

    key = [reduce(lambda x,y: x + y, r[::-1]) \
           for r in row]
    eqv.append("".join(key))

    key = reduce(lambda x,y: x + y, key[::-1])
    eqv.append("".join(key))

    key = reduce(lambda x,y: x + y, row[::-1])
    eqv.append("".join(key))
    
    if len(row) == 3: 
        key = zip(row[0], row[1], row[2])
    else:
        key = zip(row[0], row[1])
    key1 = reduce(lambda x,y: x + y, key[::-1])
    eqv.append("".join(key1))

    key1 = [reduce(lambda x,y: x + y, r[::-1]) \
            for r in key]
    eqv.append("".join(key1))

    key1 = reduce(lambda x,y: x + y, key1[::-1])
    eqv.append("".join(key1))
     
    key1 = reduce(lambda x,y: x + y, key)
    eqv.append("".join(key1))

    return eqv

def print_eqv(eqv):
    for mtx in eqv:
        print mtx
    	print "" 

def divide_mtx(mtx, size):
    mtxs = None
    num_mtx_side = None

    if size == 2:
        num_mtx_side = len(mtx) / 2
    else:
        num_mtx_side = len(mtx) / 3
    
    mtxs = [[] for _ in xrange(0, num_mtx_side*num_mtx_side)]

    i = 0
    j = 0
    while(i < num_mtx_side):
        for row in mtx[i * size: i * size + size]:
            j = i * num_mtx_side
            for x in xrange(0, len(mtx), size):
                mtxs[j].append(row[x:x + size])
                j += 1
        i += 1
    return mtxs
 

def join_mtxs(mtxs_str):
    mtxs = [m.split("/") for m in mtxs_str]
    size = int(math.sqrt(len(mtxs)))
    mtx = []

    i = 0
    while(i < size):
        mtx.append(zip(*mtxs[i * size: i * size + size]))
        i += 1
  
    mtx = "/".join(["".join(subr) for r in mtx for subr in r])
    return mtx 


def apply_rules(rules, mtx, it):
    mtxs = None
    
    for i in xrange(0, it):
        mtx = mtx.split("/")
        if len(mtx[0]) % 2 == 0:
            mtxs = divide_mtx(mtx, 2)
        else:
            mtxs = divide_mtx(mtx, 3)
        new_mtxs = []
        for m in mtxs:
            key = "".join(m)
            new_mtxs.append(rules[key])
        mtx = join_mtxs(new_mtxs)
        
    return mtx
        

def set_rules(rules):
    for line in sys.stdin:
        rule = line[:-1].split(" => ")
        rule[0] = rule[0].split("/")
        rule_eqv = get_all_mtx(rule[0])
        for eqv in rule_eqv:
            rules[eqv] = rule[1]

def main():
    rules = {}
    set_rules(rules)
    matrix = ".#./..#/###"

    new_matrix = apply_rules(rules, matrix, 5)

    print "Pixels on: {}".format(new_matrix.count('#'))
	
    #eqv = get_all_mtx([["1","2"],["3","4"]])
    #eqv = get_all_mtx([["1","2","3"],["4","5","6"], ["7","8","9"]])    
    #print_eqv(eqv)



if __name__ == "__main__":
    main()
