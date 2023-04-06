import itertools
import time
with open('input.txt') as f:
    l = f.readlines()

all_nums = []
for line in l:
    all_nums.append(int(line[:-1]))
    
print(all_nums)

total_pickle = 150
all_combs = []
#list_to_all = [i for i in range(0,total_pickle+1)]
for x in range(1,len(all_nums)):
    #print(x)
    al =         list(itertools.combinations(all_nums,x))
    print(len(al))
    #time.sleep(1)
    for i,comb in enumerate(al):
        if (sum(comb)==total_pickle):
            all_combs.append(comb)
        #print(i)
    
print(len(all_combs))
all_lengths = []
for u in all_combs:
    all_lengths.append(len(u))

mins = min(all_lengths)
print(mins)
length_combs = []
for x in all_combs:
    if (len(x)==mins):
        length_combs.append(x)
        
print(len(length_combs))
#print(all_combs)
#print(len(all_combs))


    
