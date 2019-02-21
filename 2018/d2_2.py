""" --- Day 2: Inventory Management System part 2---"""

import sys


def add_id_to_dict(id_dict, i):
    unmat_idx = None
    curr_dict = id_dict

    for idx, c in enumerate(i):
        if c not in curr_dict:
            curr_dict[c] = {}
            if not unmat_idx:
                unmat_idx = idx

        curr_dict = curr_dict[c]
    
    return unmat_idx


def get_matching_string(ids):
    id_dict = {}
    id_dict_rev = {}
    unmat_idx = None
    unmat_idx_rev = None
   
     
    for i in ids:
        unmat_idx = add_id_to_dict(id_dict, i)
        unmat_idx_rev = add_id_to_dict(id_dict_rev, i[::-1])

        if unmat_idx == (len(i) - unmat_idx_rev - 1):
            return i[:unmat_idx] + i[unmat_idx + 1:]


def main():
    ids = []    

    for line in sys.stdin:
        line = line[:-1]
        ids.append(line)

    matching_str = get_matching_string(ids)

    print "Matching string: {}".format(matching_str)


if __name__ == "__main__":
    main()
