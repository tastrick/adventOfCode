import copy
with open('input.txt') as f:
    l = f.readlines()
    
inp = l[0][:-1]
print(inp)
c = 13
li = list(inp)
while(c!=len(inp)-4):
    m = [li[i] for i in range(c-13,c+1)]
    
    
    if (len(set(m))!= len(m)):
        pass
    else:
        print(c+1)
        break
    
    c+=1
