with open('input.txt') as f:
    l=f.readlines()
    
lines = []
for line in l:
    new_line = []
    for num in line[:-1]:
        new_line.append(int(num))
    lines.append(new_line)
print(lines)
    
#def check_adjacent_for_smaller(grid,x,y,curr):
def get_adj(p,grid):
    x = p[0]
    y = p[1]
    adj  = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
    #if (point[0]==0):
    height_list = []
    new_list = []
    for point in adj:
        if (point[0]<0 or point[1]<0 or point[0]>=len(grid[0]) or point[1]>=len(grid)):
            pass
        else:
            height_list.append(grid[point[1]][point[0]])
            new_list.append(point)
    return new_list,height_list
    
points_checked = []  
lows = []
in_basin = []
basins = {}




for y,line in enumerate(lines):
    for x,num in enumerate(line):
        adj,height = get_adj([x,y],lines)
        higher = 0
        for point in adj:
            if (lines[point[1]][point[0]]>num):
                higher+=1
        if (higher==len(adj)):
            lows.append([x,y])
            
#print(sum(lows))
done =[]
#start = [
for po in lows:
    done.append(po)
    curr_basin = [po]
    adjacent,h = get_adj(po,lines)
    while (adjacent!=[]):
        curr = adjacent.pop(0)
        curr_h = h.pop(0)
        if(curr_h != 9 and curr not in done):
            curr_basin.append(curr)
            done.append(curr)
            adj,he = get_adj(curr,lines)
            for c,x in enumerate(adj):
                adjacent.append(x)
                h.append(he[c])
    basins[len(curr_basin)] = curr_basin
    #print(basins)

basin_sizes = list(basins.keys())

one = max(basin_sizes)
basin_sizes.remove(one)
two = max(basin_sizes)
basin_sizes.remove(two)
three = max(basin_sizes)

print(one*two*three)
            
