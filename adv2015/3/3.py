import time
with open('input.txt') as f:
    l = f.readlines()
print(l)

instructions = []
for line in l:
    new_inst = []
    for char in line:
        new_inst.append(char)
    instructions.append(new_inst)
    
instructions[0].remove('\n')
print(instructions[0])
all_houses = []
h = []
s = [0,0]
r = [0,0]
h.append(s)
print(h)
for i,direc in enumerate(instructions[0]):
    if (i%2==0):
        if (direc == '>'):
            s[0]+=1
        elif (direc == '<'):
            s[0]-=1
        elif (direc == '^'):
            s[1]+=1
        elif(direc == 'v'):
            s[1]-=1
    else:
        if (direc == '>'):
            r[0]+=1
        elif (direc == '<'):
            r[0]-=1
        elif (direc == '^'):
            r[1]+=1
        elif(direc == 'v'):
            r[1]-=1
    #print(h,s)
    #time.sleep(1)
    h.append(s[:]) 
    h.append(r[:])
    #print(s)
    #if(startss not in houses_visited):
    #    print('appending')
    #    houses_visited.append(startss)
#print(h)       
        

for x in h:
    if (x not in all_houses):
        all_houses.append(x)
#print(houses_visited)
print(len(all_houses))
#print(len(houses_visited))
