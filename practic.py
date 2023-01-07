from itertools import groupby
from collections import Counter


def length_frequencies(strs):
    counter = 0
    gr = [list(g) for k, g in groupby(strs)]
    l = []
    for i in gr:
        l.append(len(i[0]))
        
    l_set = set(l)

    result = Counter(l)

    return result
    
    
    

print(length_frequencies('Use the Force, Luke!'.split()))


print('-' * 100)

def length_frequencies2(items):
    len_list = list(map(len, items))
    return {i: len_list.count(i) for i in set(len_list)}


print(length_frequencies2('Use the Force, Luke!'.split()))