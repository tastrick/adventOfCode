import itertools
with open('input.txt') as f:
    l = f.readlines()

new = []
for item in l:
    split = item[:-1].split(' ')
    new.append(split)
dist_loc = {}
locations = []
for line in new:
    if (line[0] not in locations):
        locations.append(line[0])
    if (line[2] not in locations):
        locations.append(line[2])
    dist_loc[tuple([line[0],line[2]])] = line[4]
    
print(locations,dist_loc)

def find_connections(pair):
    for pa in list(dist_loc.keys()):
        if list(pa)==pair:
            return dist_loc[pa]
    return None

all_poss = list(itertools.permutations(locations))
print(len(all_poss))
total_dist_dict = {}
def get_copy(l):
    new = []
    for i in l:
        new.append(i)
        
    return new
for poss in all_poss:
    dist = 0
    copy = get_copy(poss)
    start = copy.pop(0)
    while(copy != []):
        if (tuple([start,copy[0]]) in list(dist_loc.keys())):
            dist += int(dist_loc[tuple([start,copy[0]])])
            start = copy.pop(0)
        elif(tuple([copy[0],start]) in list(dist_loc.keys())):
            dist+=int(dist_loc[tuple([copy[0],start])])
            start = copy.pop(0)
        else:
            break
    if (copy == []):
        total_dist_dict[tuple(poss)] = dist
        
#print(total_dist_dict)

min_dist = max(list(total_dist_dict.values()))

print(min_dist)
