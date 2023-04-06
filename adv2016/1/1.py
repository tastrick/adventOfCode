with open('input.txt') as f:
    l = f.readlines()
input_ins = []   
for line in l:
    input_ins.append(line[:-1])

print(input_ins)

split = input_ins[0].split(', ')
print(split)

have_visited = []
    
dirs = ['N','E','S','W']
index_of_dirs = [0,1,2,3]
to_compare = []
start = [0,0,0]
last_added =None
dirr = {'R':1,'L':-1}
for instruc in split:
    d = instruc[0]
    num = int(instruc[1:])
    last_added = [start[0],start[1]]
    start[2]=(start[2]+dirr[d])%4
    if (dirs[start[2]]=='N'):
        for x in range(0,num):
            if ([start[0],start[1]+x] not in have_visited):
                have_visited.append([start[0],start[1]+x])
            else:
                if (to_compare == []):
                    to_compare = [start[0],start[1]+x]
        start[1]+=num
    elif(dirs[start[2]]=='E'):
        for x in range(0,num):
            if ([start[0]+x,start[1]] not in have_visited):
                have_visited.append([start[0]+x,start[1]])
            else:
                if (to_compare == []):
                    to_compare = [start[0]+x,start[1]]
        start[0]+=num
    elif(dirs[start[2]]=='S'):
        for x in range(0,num):
            if ([start[0],start[1]-x] not in have_visited):
                have_visited.append([start[0],start[1]-x])
            else:
                if (to_compare==[]):
                    to_compare = [start[0],start[1]-x]
        start[1]-=num
    else:
        for x in range(0,num):
            if ([start[0]-x,start[1]] not in have_visited):
                have_visited.append([start[0]-x,start[1]])
            else:
                if (to_compare==[]):
                    to_compare = [start[0]-x,start[1]]
        start[0]-=num
    '''
    if ((start[0],start[1]) not in list(have_visited.keys())):
        if (start[0]!=last_added[0]):
            if (start[0]>last_added[0]):
                inc = -1
            else:
                inc = 1
            for x in range(start[0],last_added[0]):
                have_visited[(x,start[1])] = 1
        elif (start[1]!=last_added[1]):
            if (start[1]>last_added[1]):
                inc = -1
            else:
                inc =1
            for x in range(start[1],last_added[1]):
                have_visited[(start[0],x)]=1
    else:
        if (start[0]!=last_added[0]):
            if (start[0]>last_added[0]):
                inc = -1
            else:
                inc = 1
            for x in range(start[0],last_added[0]):
                have_visited[(x,start[1])] += 1
        elif (start[1]!=last_added[1]):
            if (start[1]>last_added[1]):
                inc = -1
            else:
                inc =1
            for x in range(start[1],last_added[1]):
                have_visited[(start[0],x)]+=1
   ''' 

            
print(start)
print(to_compare)
    
    
    
