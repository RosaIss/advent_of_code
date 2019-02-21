"""--- Day 8: Memory Maneuver part 1---"""

def remove_hdrs(root, tree):
    
    if root > len(tree):
        return 0     

    childs = tree[root]
    entries = tree[root + 1]

    tree[root] = 0
    tree[root + 1] = 0

    if not childs:
        return root + entries + 2

    next_child = root + 2
    for i in xrange(0, childs):
        next_child = remove_hdrs(next_child, tree)

    return next_child + entries


def main():
    tree = raw_input()
    tree = map(int, tree.split(" "))

    last_pos = remove_hdrs(0, tree)
    print "Metadata entries: {}".format(sum(tree))

if __name__ == "__main__":
    main()
