#import sys
import copy
#iMaxStackSize = 5000
#sys.setrecursionlimit(iMaxStackSize)
#print(sys.getrecursionlimit())
with open('input.txt') as f:
    l = f.readlines()
lines = []
for line in l:
    li = line[:-1]
    #s = li.split(" ")
    lines.append(li)
    
def getS(d):
    #print(d)
    v=0
    if (directories[d]==[]):
        #if(d=='jssl'):
        #    print('yep')
        return sizes[d]
    for x in directories[d]:
        ne = getS(x)
        #print(d,x,ne)
        v+=ne
    v+=sizes[d]
    return v

        
    
#print(lines)
cwd = []
ordering = []
directories = {}
sizes = {}
cntr=0
for command in lines:
    s = command.split(" ")
    #print(s)
    if (s[0] == '$'):
        if (s[1] == 'cd' and s[2] != '..'):
            ss=s[2]
            if (ss in list(directories.keys())):
                ss+=str(cntr)
                cntr+=1
            cwd.append(ss)
            ordering.append(ss)
            directories[ss]  = []
            sizes[ss] = 0
        elif (s[1]=='cd' and s[2]=='..'):
            cwd.pop(-1)
    elif (s[0] == 'dir'):
        di = cwd[-1]
        directories[di].append(s[1])
    elif (isinstance(int(s[0]),int)):
        for x in cwd:
            sizes[x]+=int(s[0])
#part 1
h = 0
for k,va2 in sizes.items():
    if (va2<=100000):
        h+=va2
print(h)

#part 2 
goal = 30000000-(70000000-sizes['/'])
part2 = goal
ans = 0
for k,v in sizes.items():
    if sizes[k]>=goal:
        if (sizes[k]-goal<part2):
            part2 = sizes[k]-goal
            ans = sizes[k]
print(ans)
