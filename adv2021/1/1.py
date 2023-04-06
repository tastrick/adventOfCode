with open('input.txt') as f:
    l = f.readlines()
nums = []
for line in l:
    #print(line)
    nums.append(int(line[:-1]))
    
print(nums)
mem = 0
inc = 0
lis = []
for count,i in enumerate(nums):
    #print(count)
    if (count<=2):
        lis.append(i)
        if(count==2):
            mem = sum(lis)
    else:
        lis.pop(0)
        lis.append(i)
        
        if (sum(lis)>mem):
            inc+=1
        mem = sum(lis)
print(inc)
        
    
