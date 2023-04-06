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
def most_common(lst):
    return max(set(lst), key=lst.count)
        
def least_common(lst):
    return min(set(lst), key=lst.count)

most = most_common(list(decomp.values()))
least = least_common(list(decomp.values()))


def get_pairs(s):
    pairs = []
    for i,char in enumerate(s):
        if (i>0):
            pairs.append([neigh,char])
        neigh = char
    return pairs
final_dict = {most: 0,least: 0}

def find_all(string,rules,cnt):
    if (cnt<10):
        pairs = get_pairs(string)
        for pair in pairs:
            to_add = rules[pair[0]+pair[1]]
            if (to_add == most or to_add == least):
                final_dict[to_add]+=1
            
            find_all(pair[0]+to_add+pair[1],rules,cnt+1)
find_all(start,decomp,0)

print(max(list(final_dict.values()))-min(list(final_dict.values())))
