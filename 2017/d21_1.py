import sys


def get_all_mtx3x3(row):
    eqv = []
    key = row[0]+row[1]+row[2]
    eqv.append("".join(key))

    key = [r[2] + r[1] + r[0] for r in row]
    eqv.append("".join(key))

    key = key[2] + key[1] + key[0] 
    eqv.append("".join(key))

    key = row[2]+row[1]+row[0]
    eqv.append("".join(key))
    
    key = zip(row[0], row[1], row[2])
    key1 = key[2]+key[0]+key[1]
    eqv.append("".join(key1))

    key1 = [r[2] + r[1] + r[0] for r in key]
    eqv.append("".join(key1))

    key1 = key1[2] + key1[1] + key1[0]
    eqv.append("".join(key1))
     
    key1 = key[0]+key[1]+key[2]
    eqv.append("".join(key1))

    return eqv

def get_all_mtx2x2(row):
    eqv = []
    
    key = row[0] + row[1]
    eqv.append("".join(key))
    
    key = row[1] + row[0]
    eqv.append("".join(key))

    key = row[0][1] + row[0][0] + \
          row[1][1] + row[1][0]
    eqv.append(key)

    key = row[1][1] + row[1][0] + \
          row[0][1] + row[0][0]
    eqv.append(key)

    return eqv


def print_eqv(eqv):
    for mtx in eqv:
        print mtx
        #for i in mtx:
	#    print i
    	print "" 

#def set_rules(rules)
#	for line in sys.stdin:
#		rows = line[:-1].split(" => ")
#		rows = matrix.split("/")
#		
#		if rows == 3:
#			rules[row[0]+row[1]+row[2]]
#			rules[row[2]+row[1]+row[0]]
#			key = [r[0]+r[1]+r[2] for r in zip(row[0], row[1], row[2])]
#			rules[key]
#			key = [r[2]+r[1]+r[0] for r in zip(row[0], row[1], row[2])]
#			rules[key]
#			key = [r[0]+r[1]+r[2] for r in zip(row[2], row[1], row[0])]
#			rules[key]
#			key = [r[2]+r[1]+r[0] for r in zip(row[2], row[1], row[0])]
#			rules[key]
#		else:

def divide_mtx(mtx_str):
    mtx = mtx_str.split("/")
    mtxs = None

    if len(mtx) % 2:
        num_mtx = len(mtx) / 2
        size = 2
    else:
        num_mtx = len(mtx) / 3
        size = 3
    
    mtxs = [[] * num_mtx]

    i = 0
    while(i < num_mtx):
        for row in mtx[i * size: i * size + size]:
            for x in xrange(0, len(mtx), size):
                mtxs[i] = row[x:x + size]

    return mtxs
 
        

def join_mtx(mtx):


def apply_rules(rules, mtx, it):
    
    key = "".join(mtx.split("/"))
    mtx = rule[key]

    for _ in xrange(0, it):
        mtxs = divide_mtx(mtx)
        for m in mtxs:
            new_mtxs.append(rule[key])
        mtx = join(mtxs)
        

def set_rules(rules):
    for line in sys.stdin:
        rule = line[:-1].split(" => ")
        rule = matrix.split("/")
        if len(rule) == 3:
            rule_eqv = get_all_mtx3x3(rule[0])
        else: 
            rule_eqv = get_all_mtx2x2(rule[0])

        for eqv in rule_eqv:
            rules[eqv] = rule[1]

def main():
    rules = {}
    set_rules(rules)
    matrix = ".#./..#/###"

    apply_rules(rules, matrix, it)
	
    #eqv = get_all_mtx3x3([["1","2","3"],["4","5","6"], ["7","8","9"]])
    #eqv = get_all_mtx2x2([["1","2"],["3","4"]])
    
    print_eqv(eqv)
	#set_rules(rules)



if __name__ == "__main__":
    main()
