import copy
with open('input.txt') as f:
    l = f.readlines()

d = {1:['T','Z','B'],2:['N','D','T','H','V'],3:['D','M','F','B'],4:['L','Q','V','W','G','J','T'],5:['M','Q','F','V','P','G','D','W'],6:['S','F','H','G','Q','Z','V'],7:['W','C','T','L','R','N','S','Z'],8:['M','R','N','J','D','W','H','Z'],9:['S','D','F','L','Q','M']}

f = {}
for k,v in d.items():
    f[k] = list(reversed(v))
ff = copy.deepcopy(f)
print(f)
a = []
for line in l:
    li = line[:-1]
    s = li.split(" ")
    a.append([int(s[1]),int(s[3]),int(s[5])])
    
def place(fr, to):
    i = f[fr].pop()
    f[to].append(i)
    
for instruction in a:
    for u in range(0,instruction[0]):
        place(instruction[1],instruction[2])
st = ""
for k,v in f.items():
    st+=v[-1]

#print(st)
def placetwo(n, fr, to):
    p = []
    for x in range(0,n):
        p.append(ff[fr].pop())
    for y in list(reversed(p)):
        ff[to].append(y)
    #i = f[fr].pop()
    #f[to].append(i)
#part2
for instruction in a:
    placetwo(instruction[0],instruction[1],instruction[2])
    

    
st = ""
for k,v in ff.items():
    st+=v[-1]
print(st)
