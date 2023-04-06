lines = [[6,1,1,1,8,2,1,7,6,7],[1,7,6,3,6,1,1,6,1,5],[3,5,1,2,6,8,3,1,3,1],[8,5,8,2,7,7,1,4,7,3],[8,2,1,4,8,1,3,8,7,4],[2,3,2,5,8,2,3,2,1,7],[2,2,2,2,4,8,2,8,2,3],[5,4,7,1,3,5,6,7,8,2],[3,7,3,8,6,7,1,2,8,7],[8,6,7,5,2,2,6,5,7,4]]
#lines = [[5,4,8,3,1,4,3,2,2,3],[2,7,4,5,8,5,4,7,1,1],[5,2,6,4,5,5,6,1,7,3],[6,1,4,1,3,3,6,1,4,6],[6,3,5,7,3,8,5,4,7,8],[4,1,6,7,5,2,4,6,4,5],[2,1,7,6,8,4,1,7,2,1],[6,8,8,2,8,8,1,1,3,4],[4,8,4,6,8,4,8,5,5,4],[5,2,8,3,7,5,1,5,2,6]]
    


def get_adj(p,grid):
    x = p[0]
    y = p[1]
    adj  = [[x+1,y],[x-1,y],[x,y+1],[x,y-1],[x+1,y+1],[x-1,y+1],[x+1,y-1],[x-1,y-1]]
    #if (point[0]==0):
    
    new_list = []
    for point in adj:
        if (point[0]<0 or point[1]<0 or point[0]>=len(grid[0]) or point[1]>=len(grid)):
            pass
        else:
            new_list.append(point)
    return new_list

count = 0
steps = 100
ans = 0
flashes = 0
while(True):
    flash_group = []
    has_flashed = []
    to_zero = []
    #increment all 
    for y, line in enumerate(lines):
        for x, num in enumerate(line):
            lines[y][x]+=1
            if (num+1>9):
                flash_group.append([x,y])
    
    #dealing with possible flashes within flashes
    print(flash_group,count)
    while(flash_group!=[]):
        point = flash_group.pop(0)
        if (lines[point[1]][point[0]]>9 and point not in has_flashed):
            to_zero.append(point)
            flashes+=1
            has_flashed.append(point)
            adjacent = get_adj(point,lines)
            for p in adjacent:
                lines[p[1]][p[0]]+=1
                flash_group.append(p)
        #if (lines[point[1]][point[0]]>9):
    if (len(has_flashed)==100):
        break
    for point in has_flashed:
        lines[point[1]][point[0]] = 0
    print(flashes)
    count+=1
    
#print(flashes)
print(count)
