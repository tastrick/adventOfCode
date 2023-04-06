import time
import sys
import json
with open('input.json') as f:
    data = json.load(f)
globals()['count'] = 0

print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())
'''
#print(data)
for x in data:
    for y in x:
        for z in y:
            for j in z:
                for r in j:
                    for l in r:
                        for v in l:
                            for f in v:
                                for h in f:
                                    for g in h:
                                        for oo in g:
                                            for uu in oo:
                                                print(uu)
'''

done = []
sumnums = 0
done.append(data)
print(type(data))
flag = True

while(done != []):
    curr_struct = done.pop(0)
    if (isinstance(curr_struct,dict)):
        has_red_flag = False
        for item in list(curr_struct.values()):
            if (item == 'red'):
                has_red_flag = True
        if (has_red_flag==False):
            for x in list(curr_struct.keys()):
                
                done.append(curr_struct[x])
                
                if (isinstance(x,int)):
                    #print('num in dict keys')
                    sumnums+=x
        
    elif(isinstance(curr_struct,str)):
        pass
        #print('string')
    elif(isinstance(curr_struct,int)):
        #print('num')
        sumnums+=curr_struct
    elif(isinstance(curr_struct,list)):
        for a in curr_struct:
            done.append(a)
        
print(sumnums)
    
