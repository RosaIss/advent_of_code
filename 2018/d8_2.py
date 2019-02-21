"""--- Day 8: Memory Maneuver part 2---"""

def remove_hdrs(root, tree):

    if root > len(tree):
        return 0, 0

    childs = tree[root]
    entries = tree[root + 1]
    value = 0 

    tree[root] = 0
    tree[root + 1] = 0

    if not childs:
        if entries == 1:
            value = tree[root + 2]
        else:
            value = sum(tree[root + 2: root + 2 + entries])
        return root + entries + 2, value

    child_values = []
    ent_values = []
    next_root = root + 2
    for i in xrange(0, childs):
        next_root, tmp_value = remove_hdrs(next_root, tree)
        child_values.append(tmp_value)

    ent_values = tree[next_root:next_root + entries]
    values = [child_values[e - 1]
             for e in ent_values if e - 1 < len(child_values)]

    return next_root + entries, sum(values)


def main():
    tree = raw_input()
    tree = map(int, tree.split(" "))

    _, value = remove_hdrs(0, tree)
    print "Value of root: {}".format(value)

if __name__ == "__main__":
    main()
