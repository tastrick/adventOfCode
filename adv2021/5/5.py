with open('input.txt') as f:
    l = f.readlines()
lines = []
for x in l:
    #new_line = []
    split = x[:-1].split('->')
    s1 = split[0].split(',')
    s2 = split[1].split(',')
    point1 = [int(s1[0]),int(s1[1])]
    point2 = [int(s2[0]),int(s2[1])]
    new_line = [point1,point2]
    lines.append(new_line)
    
print(len(lines))

points_covered =[]

def get_points(li):
    p = []
    if (li[0][0]==li[1][0]):
        if (li[0][1]<li[1][1]):
            for x in range(li[0][1],li[1][1]+1):
                new_point = (li[0][0],x)
                p.append(new_point)
        else:
            for x in range(li[1][1],li[0][1]+1):
                new_point = (li[0][0],x)
                p.append(new_point)
    elif (li[0][1]==li[1][1]):
        if (li[0][0]<li[1][0]):
            for x in range(li[0][0],li[1][0]+1):
                new_point = (x,li[0][1])
                p.append(new_point)
        else:
            for x in range(li[1][0],li[0][0]+1):
                new_point = (x,li[0][1])
                p.append(new_point)
    else:
        if (li[0][0]>li[1][0]):
            if (li[0][1]>li[1][1]):#x dec y dec
                start = tuple(li[0])
                p.append(start)
                print('start while')
                while (start != tuple(li[1])):
                    start = (start[0]-1,start[1]-1)
                    #start[0]-=1
                    #start[1]-=1
                    p.append(start)
                print('end while')
                #p.append(tuple(li[1]))
            else:#x dec y inc
                start = tuple(li[0])
                p.append(start)
                print('start while')
                while (start != tuple(li[1])):
                    start = (start[0]-1,start[1]+1)
                    #start[0]-=1
                    #start[1]+=1
                    p.append(start)
                print('end while')
                #p.append(tuple(li[1]))
        else:
            if (li[0][1]>li[1][1]):#x inc y dec
                start = tuple(li[0])
                p.append(start)
                print('start while')
                while (start != tuple(li[1])):
                    start = (start[0]+1,start[1]-1)
                    #start[0]+=1
                    #start[1]-=1
                    p.append(start)
                print('end while')
                #p.append(tuple(li[1]))
            else:#x inc y inc
                start = tuple(li[0])
                p.append(start)
                print('start while')
                while (start != tuple(li[1])):
                    start = (start[0]+1,start[1]+1)
                    #start[0]+=1
                    #start[1]+=1
                    p.append(start)
                print('end while')
                #p.append(tuple(li[1]))
            
    return p



for i,line in enumerate(lines):
    #print(i)
    points = get_points(line)
    points_covered.append(points)
#print(points_covered)
over_dict = {}
print('filling dictionary')
for r in points_covered:
    for point in r:
        if (point not in list(over_dict.keys())):
            over_dict[point] = 1
        else:
            over_dict[point]+=1

print('done dictionary')

print(over_dict)
num = 0
for x in list(over_dict.values()):
    if (x>=2):
        num+=1
print(num)
        
'''
#print(points_covered)
overlap = []
for y,lin in enumerate(points_covered):
    num_overlap = 0
    for c,k in enumerate(points_covered):
        if (c==y):
            pass
        else:
            #print('line1: ',lin,'line2:',k)
            num_overlap += len(list(set(lin).intersection(k)))
    overlap.append(num_overlap)
#print(overlap)  
#print(len(overlap))

    
num=0
for ov in overlap:
    if (ov>=2):
        num+=1
print(num)
'''
