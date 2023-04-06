import math
import time
with open('input.txt') as f:
    l = f.readlines()
    
nums = []
split = l[0][:-1].split(',')
for n in split:
    nums.append(int(n))
    
#print(nums)
def factorial(n):
    li = [1]
    
    for num in range(2, n + 1):
        li.append(num)
    return li
lowest = min(nums)
highest = max(nums)
all_fuels = {}
print(lowest, highest)
time.sleep(2)
for x in range(lowest,highest+1):
    fuel_consump = 0
    for nu in nums:
        diff=abs(nu-x)
        fact = factorial(diff)
        for q in fact:
            fuel_consump+=q
    all_fuels[fuel_consump] = x
    print(x)

smallest = min(list(all_fuels.keys()))
print(smallest, all_fuels[smallest])
