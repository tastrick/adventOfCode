import copy
import time
with open('./input.txt') as f:
    l = f.readlines()

lines = []

start = l[0]
start = [i for i in start]
#print(start,l)
l.pop(0)
l.pop(0)
for line in l:
    #print(line)
    split = line[:-1].split(' -> ')
    new = [split[0],split[1]]
    lines.append(new)
#print(start)
decomp = {}
start.pop()
for x in lines:
    decomp[x[0]] =x[1] 

#print(decomp)
final_dict = {}
for sr in list(decomp.keys()):
    for char in sr:
        if (char not in list(final_dict.keys())):
            final_dict[char] = 0
#print(final_dict)
            
def get_pairs(s):
    print('in get pairs: ', s)
    pairs = []
    for i,char in enumerate(s):
        if (i>0):
            pairs.append(neigh+char)
        neigh = char
    return pairs
c = {k:0 for k in list(decomp.keys())}
p = get_pairs(start)
for va in p:
    c[va]+=1
count = 0
end = 40

for x in start:
    final_dict[x]+=1
#print(new)
#time.sleep(10)
#print('start: ', start)
for _ in range(end):
    
    new = {k:0 for k in list(decomp.keys())}
    #print(c,new)
    for k,v in c.items():
        if (v>0):
            #print(k,v)
            p1 = k[0]+decomp[k]
            p2 = decomp[k]+k[1]
            new[p1]+=v
            new[p2]+=v
            final_dict[decomp[k]]+=v
    c = copy.deepcopy(new)   
    
    #print(i)
    

#print(start)
print(max(list(final_dict.values()))-min(list(final_dict.values())))
        
    
