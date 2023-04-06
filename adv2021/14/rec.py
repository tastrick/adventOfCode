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
    #print(x)
    decomp[x[0]] =x[1]
    
#print(decomp)

def get_pairs(s):
    pairs = []
    for i,char in enumerate(s):
        if (i>0):
            pairs.append([neigh,char])
        neigh = char
    return pairs
final_dict = {}
for x in start:
    if (x not in list(final_dict.keys())):
        final_dict[x]=1
    else:
        final_dict[x]+=1

def find_all(string,rules,cnt):
    #print(cnt)
    if (cnt<40):
        p = get_pairs(string)
        for pair in p:
            if (pair[0]+pair[1] in list(rules.keys())):
                to_add = rules[pair[0]+pair[1]]
                if (to_add not in list(final_dict.keys())):
                    final_dict[to_add] = 1
                else:
                    final_dict[to_add]+=1
                find_all(pair[0]+to_add+pair[1],rules,cnt+1)
                #find_all(to_add+pair[1],rules,cnt+1)
                '''
pairs = get_pairs(start)
for c,pair in enumerate(pairs):
    find_all(pair,decomp,0)
    print('done pair: ', pair,c)
#start = ['C','O']
'''
find_all(start,decomp,0)
print(final_dict)
print(max(list(final_dict.values()))-min(list(final_dict.values())))
            
    
