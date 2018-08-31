""" Day 4: High-Entropy Passphrases part 1 """

import sys

def is_valid(passprhase):
    words = passprhase.split(" ")
    uniq_words = set(words)
    if len(words) == len(uniq_words):
        return True
    return False

i = 0
for passprhase in sys.stdin:
    if is_valid(passprhase[:-1]):
        i +=1
print i
