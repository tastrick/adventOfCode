import time
import cv2
with open('./input.txt') as f:
    l = f.readlines()

coords = []
folds = []
list_curr = 'coords'
for line in l:
    #print (line)
    if(line=='\n'):
        list_curr= 'folds'
    else:
        if (list_curr=='coords'):
            split = line[:-1].split(',')
            coord = [int(split[0]),int(split[1])]
            coords.append(coord)
        else:
            split1 = line[:-1].split(' ')   
            split2 = split1[-1].split('=')
            fold = (split2[0],int(split2[1]))
            folds.append(fold)
        
mins = []
maxs = []
#print(coords)
def build_grid(points):
    return [[0 if [x,y] not in points else  1 for x in range(0,1311)] for y in range(0,895)]

def fold_left(x_val,grid):
    left_part = [l[0:x_val] for l in grid]
    right_part = [list(reversed(r[x_val:])) for r in grid]
    #print(right_part)
    '''
    new = []
    for y in range(0,len(left_part)):
        lk = []
        for x in range(0,len(left_part[0])):
            if (left_part[y][x]==right_part[y][x]):
                lk.append(left_part[y][x])
            else:
                lk.append(1)
        new.append(lk)
        '''
    new_grid = [[left_part[j][i] if left_part[j][i]==right_part[j][i] else 1 for i in range(0,len(left_part[0]))] for j in range(0,len(left_part))]
    
    
    #print(new_grid)
    return new_grid
def generate_blank_im(self,color, height, width):
        new_im = np.zeros((width,height,3),np.uint8)
        new_color =tuple(reversed(color))
        new_im[:] = (new_color)
        return new_im
def fold_up(y_val,grid):
    top_part = [grid[i] for i in range(0,y_val)]
    bottom_part = [grid[i] for i in range(len(grid)-1,y_val-1,-1)]
    print(len(grid)-1,y_val-1)
    #print(len(grid),len(bottom_part))
    #print(top_part,bottom_part)
    #time.sleep(2)
    new_grid = [[top_part[j][i] if top_part[j][i]==bottom_part[j][i] else 1 for i in range(0,len(top_part[0]))] for j in range(0,len(top_part))]
    return new_grid
g = build_grid(coords)
#print(g[850][500])
#print(g)
#print(folds)
#c = fold_left(655,g)
for direction in folds:
    if (direction[0]=='x'):
        print('folding about x')
        g = fold_left(direction[1],g)
        print(g)
    else:
        print('folding about y')
        g = fold_up(direction[1],g)
        print(g)
print(folds)
#c= []
ans = 0

            
im = generate_blank_im((0,0,0), len(g),len(g[0]))
for j,x in enumerate(g) :
    for i,num in enumerate(x):
        if (num==1):
            im[j][i] = (255,255,255)
cv2.imwrite('./test.png',im)
print(ans)
        
