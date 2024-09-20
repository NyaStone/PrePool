from typing import List
from functools import reduce

def removeDuplicates(someIntList: List[int]):
    return list(set(someIntList))

def uniqTotal(someIntList: List[int]):
    if len(someIntList) == 0:
        return None
    return reduce(lambda x, y: x + y, removeDuplicates(someIntList))

print(uniqTotal([ 1, 2, 3]))
print(uniqTotal([ 1, 3, 8, 1, 8]))
print(uniqTotal([ -1, -1, 5, 2, -7]))
print(uniqTotal([]))