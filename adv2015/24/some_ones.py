import itertools
import operator
from functools import reduce
nums = list(map(int, [line.strip("\n") for line in open('input.txt')]))
print(nums)
parts = 3
tot = sum(nums)/parts
all_sums = []
def hasSum(lst, sub):
    for y in range(1,len(lst)): 
        for x in (z for z in itertools.combinations(lst, y) if sum(z) == tot):
            if sub == 2:#if we are here then there are two groups that sum to our num thus the remaining has to sum to our num by the nature of the tot
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return reduce(operator.mul, x, 1)
print(hasSum(nums, parts))
