from dijkstra import dijkstra
import copy
import numpy as np
with open('input.txt') as f:
    l = f.readlines()

cave = []
for line in l:
    new_row  =[]
    for num in line[:-1]:
        new_row.append(int(num))
    cave.append(new_row)

start = (0,0)
temp = copy.deepcopy(cave)

template = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]

all_nine = []
for cnt in range(2,10):
    new = []
    for row in temp:
        new_row = []
        for col in row:
            val = col+1
            if (val>9):
                val = val%9
            new_row.append(val)
        new.append(new_row)
    all_nine.append(new)
    temp = copy.deepcopy(new)

#print(all_nine)
'''
r1 = np.hstack([np.array(cave),np.array(all_nine[0]),np.array(all_nine[1]),np.array(all_nine[2]),np.array(all_nine[3])])
r2 = np.hstack([np.array(all_nine[0]),np.array(all_nine[1]),np.array(all_nine[2]),np.array(all_nine[3]),np.array(all_nine[4])])
r3 = np.hstack([np.array(all_nine[1]),np.array(all_nine[2]),np.array(all_nine[3]),np.array(all_nine[4]),np.array(all_nine[5])])
r4 = np.hstack([np.array(all_nine[2]),np.array(all_nine[3]),np.array(all_nine[4]),np.array(all_nine[5]),np.array(all_nine[6])])
r5 = np.hstack([np.array(all_nine[3]),np.array(all_nine[4]),np.array(all_nine[5]),np.array(all_nine[6]),np.array(all_nine[7])])
'''
r1 = np.hstack([cave,all_nine[0],all_nine[1],all_nine[2],all_nine[3]])
r2 = np.hstack([all_nine[0],all_nine[1],all_nine[2],all_nine[3],all_nine[4]])
r3 = np.hstack([all_nine[1],all_nine[2],all_nine[3],all_nine[4],all_nine[5]])
r4 = np.hstack([all_nine[2],all_nine[3],all_nine[4],all_nine[5],all_nine[6]])
r5 = np.hstack([all_nine[3],all_nine[4],all_nine[5],all_nine[6],all_nine[7]])

f = np.vstack([r1,r2,r3,r4,r5])


#print(f.tolist())
cave = copy.deepcopy(f.tolist())
targ = (len(cave[0])-1,len(cave)-1)
nodes = [(x,y) for x in range(0,len(cave[0])) for y in range(0,len(cave))]
init_graph = {}
for node in nodes:
    init_graph[node] = {}

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

    
for y, row in enumerate(cave):
    for x,col in enumerate(row):
        adj  = get_adj([x,y],cave)
        for point in adj:
            init_graph[(x,y)][tuple(point)] = cave[point[1]][point[0]]

#print(init_graph)

dijkstra(init_graph,nodes,start,targ)
