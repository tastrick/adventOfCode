with open('./input.txt') as f:
    l = f.readlines()
    
dire = []
for line in l:
    split = line[:-1].split(' ')
    dire.append([split[0],split[1]])
    
print(dire)

start = [0,0,0]

for m in dire:
    print(start)
    if (m[0] == 'forward'):
        start[0]+=int(m[1])
        start[1]+=int(m[1])*start[2]
    elif(m[0] == 'down'):
        start[2]+=int(m[1])
    else:
        start[2]-=int(m[1])
        
print(start[0]*start[1])
