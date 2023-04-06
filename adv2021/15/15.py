import random
import time
import copy
with open('test_input.txt') as f:
    l = f.readlines()




def get_adj(p,grid):
    x = p[0]
    y = p[1]
    adj  = [[x,y+1],[x+1,y],[x-1,y],[x,y-1]]
    #if (point[0]==0):
    
    new_list = []
    for point in adj:
        if (point[0]<0 or point[1]<0 or point[0]>=len(grid[0]) or point[1]>=len(grid)):
            pass
        else:
            new_list.append(point)
    return new_list




cave = []
for line in l:
    new_row  =[]
    for num in line[:-1]:
        new_row.append(int(num))
    cave.append(new_row)
    
#print(grid)
end = [len(cave[0])-1,len(cave)-1]
final = []
all_ = []
done = []

paths = {(x,y):0 for x in range(0,len(cave[0])) for y in range(0,len(cave))}
paths[(0,0)]+=1

weights = {(x,y): cave[y][x] for x in range(0,len(cave[0])) for y in range(0,len(cave))}
#print(weights)
#time.sleep(2)
#print(end)
def get_next(path, point):
    adj =get_adj(point,cave)
    for x in adj:
        if (path[tuple(x)]<1):
            path[tuple(x)]+=1
            #poss = []
            w= [v for k,v in weights.items() if path[k]>0]
            if (x==end):
                #print('done',path)
                final.append(sum(w))
                path[tuple(x)]=0
            else:
                get_next(path,x)
    path[tuple(point)]=0
    
    
    
    
    
            
get_next(paths,[0,0])        
#get_next(cave,[0,0],[[0,0]],0)
print(final)            
                
            
    
