cnt = 0
li = 4
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
decomp = {}
start.pop()
for x in lines:
    decomp[x[0]] =x[1] 


def most_common(lst):
    return max(set(lst), key=lst.count)
        
def least_common(lst):
    return min(set(lst), key=lst.count)

most = list(decomp.values()).count(most_common(list(decomp.values())))
least = list(decomp.values()).count(least_common(list(decomp.values())))
tot = len(list(decomp.keys()))
print(most,least,tot)
perc_most = most/(tot)
perc_least = least/(tot)
while(cnt<40):
    li = 2*li -1
    cnt+=1
print(li)
print(int((li-len(start))*perc_most))
print(int((li-len(start))*perc_least))
