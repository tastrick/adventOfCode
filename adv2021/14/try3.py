with open('./test_input.txt') as f:
    l = f.readlines()

lines = []

start = l[0]
start = [i for i in start]
print(start,l)
l.pop(0)
l.pop(0)
for line in l:
    #print(line)
    split = line[:-1].split(' -> ')
    new = [split[0],split[1]]
    lines.append(new)
print(start)
rules = {}
start.pop()
for x in lines:
    rules[x[0]] =x[1] 


final_dict = {}
for rule in list(rules.keys()):
    for char in rule:
        if (char not in list(final_dict.keys())):
            final_dict[char] = 0
        
print(rules, final_dict)


def rec(pair,cnt):
    if (cnt<30):
        final_dict[rules[pair[0]+pair[1]]]+=1
        rec([pair[0],rules[pair[0]+pair[1]]],cnt+1)
        rec([rules[pair[0]+pair[1]],pair[1]],cnt+1)
    else:
        return

def get_pairs(s):
    pairs = []
    for i,char in enumerate(s):
        if (i>0):
            pairs.append([neigh,char])
        neigh = char
    return pairs

for _ in range(40):
    
    
print(final_dict)
        
    

