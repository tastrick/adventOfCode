import itertools
import random
from functools import reduce
with open('input.txt') as f:
    l = f.readlines()
weights = []
for line in l:
    weights.append(int(line[:-1]))
    
curr_guess = []
#print(weights)

    
    
#print(all_lengths)

# Yield successive n-sized

list_breaks = [i for i in range(1,len(weights)-1)]

all_pairs = list(itertools.combinations(list_breaks,2))
def multiply_list(l):
    p = reduce(lambda x, y: x*y, l)
    #print(p)
    return p

def print_stats():
    #print(all_groups)
    min_length_in_main = 1000000000000000000000
    for i,org in enumerate(len_of_groups):
        for j,group in enumerate(org):
            if (group<min_length_in_main):
                min_length_in_main = group
    print(min_length_in_main)            
    all_mins = []
    for i,org in enumerate(len_of_groups):
        for j,group in enumerate(org):
            if (group==min_length_in_main):
                all_mins.append([i,j])
    ind = 0
    minimum_quantum_score = 1000000000000000000000
    for inc,minimum in enumerate(all_mins):
        if (quantums[minimum[0]][minimum[1]]<minimum_quantum_score):
            ind = inc
            minimum_quantum_score = quantums[minimum[0]][minimum[1]]
    #print(ind) 
    #print(all_mins)
    #index_of_least = all_mins[ind][0]

    #print(quantums[index_of_least][0])
    print(minimum_quantum_score)
#print(all_pairs)
cnt =1
all_groups = []
best = []
quantums = []
len_of_groups = []
while(cnt <100000000):
    
    
    random.shuffle(weights)
    for poss in all_pairs:
        group1 = weights[0:poss[0]-1]
        group2 = weights[poss[0]:poss[1]-1]
        group3 = weights[poss[1]:]
        if (sum(group1) != sum (group2) or sum(group1) !=sum(group3) or sum(group2) != sum(group3)):
            pass
        else:
            #print('made')
            to_be = [group1,group2,group3]
            if (to_be not in all_groups):
                #print(group1)
                #num =
                #print(reduce(lambda x, y: x*y, group1))
                quantums.append([multiply_list(group1),multiply_list(group2),multiply_list(group3)])
                all_groups.append(to_be)
                len_of_groups.append([len(group1),len(group2),len(group3)])

    if(cnt%10000==0):
        #min_quantum = min(quantums)
        #index = #quantums.index(min_quantum)
        #print(min_quantum)
        #print(all_groups[index])
        print_stats()
        
    cnt+=1

            

    
    
    
    
