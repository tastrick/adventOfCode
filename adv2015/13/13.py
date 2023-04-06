import itertools
import time
with open('input.txt') as f:
    l = f.readlines()
    
    
final_dict = {}#key positive or negative addition to points, values are the arrangement

pair_dict = {}# keys pair, value is the positive or negative addition of points in the case that this was a pairing

for line in l:
    split = line[:-2].split(' ')
    if (split[2]=='gain'):
        
        pair_dict[tuple([split[0],split[10]])] =int(split[3])
    else:
        pair_dict[tuple([split[0],split[10]])] =0-int(split[3])
print(pair_dict)
time.sleep(2)
all_attendees = []
for key in list(pair_dict.keys()):
    if (key[0] not in all_attendees):
        all_attendees.append(key[0])
    if (key[1] not in all_attendees):
        
        all_attendees.append(key[1])
    
#adding myself in the list
for x in all_attendees:
    pair_dict[tuple(['Tara',x])] = 0
    pair_dict[tuple([x,'Tara'])] = 0
    
all_attendees.append('Tara')

def get_happiness_of_curr(p):
    total = 0
    for i,person in enumerate(p):
        neighs_i = [(i-1)%num_people,(i+1)%num_people]
        #print(neighs_i[0],i,neighs_i[1])
        #print(neighs_i)
        total+=pair_dict[tuple([person,p[neighs_i[1]]])]
        total+=pair_dict[tuple([person,p[neighs_i[0]]])]
            
            
    return total


all_poss = list(itertools.permutations(all_attendees))
print(all_poss)
num_people = len(all_attendees)

for poss in all_poss:
    tot = 0
    #print(poss)
    tot+=get_happiness_of_curr(poss)
    #print(tot,poss)
    
    final_dict[tot] = poss
    
print(final_dict)
lowest = max(list(final_dict.keys()))
print('best: ', lowest, final_dict[lowest])
print('recalculated: ', get_happiness_of_curr(final_dict[lowest]))

    
    
