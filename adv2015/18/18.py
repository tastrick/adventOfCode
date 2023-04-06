with open('input.txt') as f:
    l = f.readlines()

grid_string = []
for line in l:
    grid_string.append(line[:-1])

print(grid_string)
grid = []
for string in grid_string:
    new_line = []
    for char in string:
        if(char == '.'):
            new_line.append(0)
        else:
            new_line.append(1)
    grid.append(new_line)
    
print(grid)
def copy(lists):
    new_l = []
    for item in lists:
        line = []
        for thing in item:
            line.append(thing)
        new_l.append(line)
        
    return new_l

bad = [[0,0],[0,len(grid)-1],[len(grid[0])-1,0],[len(grid[0])-1,len(grid)-1]]

for x in bad:
    grid[x[1]][x[0]] = 1
def update_state():
    copy_grid = copy(grid)
    for j,y in enumerate(grid):
        for i,x in enumerate(y):
            curr_loc =[i,j] 
            neighs = [[curr_loc[0]+1,curr_loc[1]],[curr_loc[0]-1,curr_loc[1]],[curr_loc[0],curr_loc[1]+1],[curr_loc[0],curr_loc[1]-1],[curr_loc[0]+1,curr_loc[1]+1],[curr_loc[0]-1,curr_loc[1]-1],[curr_loc[0]+1,curr_loc[1]-1],[curr_loc[0]-1,curr_loc[1]+1]]
            on = 0
            off = 0
            for n in neighs:
                if (n[0]>=0 and n[0]<len(y) and n[1]>=0 and n[1]<len(grid)):
                    if(copy_grid[n[1]][n[0]]==0):
                        off+=1
                    else:
                        on+=1
            #print(curr_loc,on,off)
            #print('on and off: ', on, off)        
            if (copy_grid[curr_loc[1]][curr_loc[0]]== 0):
                if (on ==3):
                    #print('changing to on: ', curr_loc,on,off)
                    grid[curr_loc[1]][curr_loc[0]] = 1
                    
            else:
                if (on==2 or on==3):
                    pass
                else:
                    #print('changing to off: ', curr_loc,on,off)
                    if (curr_loc not in bad):
                        grid[curr_loc[1]][curr_loc[0]] = 0
                    #print(grid)
                    #print(copy_grid)
            #print('on and off: ', on, off)
            
count = 0
while(count<100):
    update_state()
    print(grid)
    count+=1


print(grid)
on_tot = 0
for li in grid:
    for v in li:
        if(v==1):
            on_tot+=1
            
print(on_tot)
