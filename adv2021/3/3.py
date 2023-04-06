with open('input.txt') as f:
    l = f.readlines()
    
lines = []
for li in l:
    lines.append(li[:-1])
    
print(lines)
'''
z = {i : [0,0] for i in range(0,12)}
#one = {}


b = ''
c = ''
for x in list(z.keys()):
    if (z[x][0]>z[x][1]):
        b+='0'
        c+='1'
    else:
        b+='1'
        c+='0'
print(int(b,2))
print(int(c,2))
print(int(b,2)*int(c,2))
'''

def fill_dict (l,dic):
    for num in l:
        for i in range(0,12):
            if (num[i]=='0'):
                dic[i][0]+=1
            else:
                dic[i][1]+=1
    return dic


place = 0
def cop(l):
    s = []
    for n in l:
        s.append(n)
    return s
oxygen = cop(lines)
#print(oxygen)
while (len(oxygen)!=1):
    print(len(oxygen))
    for x in range(0,12):
        if (len(oxygen)==1):
            break
        else:
            z = {i : [0,0] for i in range(0,12)}
            z = fill_dict(oxygen,z)
        
            if (z[x][0]>z[x][1]):
                oxygen = [o for o in oxygen if o[x]=='0']
            else:
                oxygen = [o for o in oxygen if o[x]=='1']
print(oxygen)

co2 = cop(lines)
#print(co2)
z = {i : [0,0] for i in range(0,12)}
while (len(co2)!=1):
    
    for x in range(0,12):
        
        if (len(co2)==1):
            break
        else:
            z = {i : [0,0] for i in range(0,12)}
            z = fill_dict(co2,z)
            if (z[x][0]>z[x][1]):
                co2= [o for o in co2 if o[x]=='1']
            else:
                co2 = [o for o in co2 if o[x]=='0']
print(int(oxygen[0],2)*int(co2[0],2))


