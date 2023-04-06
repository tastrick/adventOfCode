with open('input.txt') as f:
    l = f.readlines()

print(l)
new = []
for item in l:
    split = item.split('\n')
    new.append(split[0])
    
print(new)

nums = []
for x in new:
    split2 = x.split('x')
    #print(split2)
    nums.append(split2)
    
def get_surface(pre):
    copy = []
    for x in pre:
        copy.append(x)
    lowest = min(copy)
    index = copy.index(lowest)
    copy.pop(index)
    second_lowest = min(copy)
    #return 2*pre[0]*pre[1]+2*pre[1]*pre[2]+2*pre[2]*pre[0]+lowest*second_lowest
    return 2*lowest+2*second_lowest+pre[0]*pre[1]*pre[2]
    
tot = 0
for present in nums:
    numerical = [int(i) for i in present]
    print(numerical)
    tot+=get_surface(numerical)
    
print(tot)
