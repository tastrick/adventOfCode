import string

with open('input.txt') as f:
    l = f.readlines()
    
items = []
for line in l:
    li = line[:-1]
    items.append(li)

priority_dict = {"a":1,"b":2,"c":3,"d":4}
print(items)
total = 0
a =[]
for item in items:
    half = int(len(item)/2)
    
    first_half = item[0:half]
    second_half = item[half:]
    #print(first_half, second_half)
    first = []
    
    #print(len(first_half), len(first_half))
    a = []
    for x in list(first_half):
        for y in list(second_half):
            if (x==y):
                
                if (x.isupper()):
                    #position =string.index(string.ascii_lowercase,x)+27
                    position = string.ascii_lowercase.index(x.lower())+27
                    #print(position,x)
                else:
                    position = string.ascii_lowercase.index(x)+1
                    #print(position,x)
                if (y not in a):
                    #print(position,x)
                    total+=position
                    a.append(y)
#print(total)
v=[]
s = []
c=0
for item in items:
    if(c%3!=0 or c ==0):
       s.append(item)
    if ((c%3==0 and c!=0)or c == len(items)-1):
       v.append(s)
       s = []
       s.append(item)
    c+=1
print(v)
tot = 0
for x in v:
    m1 = x[0]
    m2 = x[1]
    m3 = x[2]
    a = []
    for y in m1:
        for z in m2:
            for u in m3:
                if (y==z and y==u):
                    if (y.isupper()):
                         position = string.ascii_lowercase.index(y.lower())+27
                    else:
                        position = string.ascii_lowercase.index(y)+1
                    if (y not in a):
                        tot+=position
                        a.append(y)
                        
                    
print(tot)                
