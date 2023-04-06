import time
with open('input.txt') as f:
    l = f.readlines()

list_of_tups = []
for item in l:
    split = item.split(' ')
    #print(split)
    
    if (split[0]=='toggle'):
        num_split_1 = split[1].split(',')
        num_split_2 = split[3].split(',')
        nums1 = [int(num_split_1[0]),int(num_split_1[1])]
        num_split_2[1].replace('\n','')
        nums2 = [int(num_split_2[0]),int(num_split_2[1])]
        tupple = ('toggle',nums1,nums2)
    else:
        num_split_1 = split[2].split(',')
        num_split_2 = split[4].split(',')
        nums1 = [int(num_split_1[0]),int(num_split_1[1])]
        num_split_2[1].replace('\n','')
        nums2 = [int(num_split_2[0]),int(num_split_2[1])]
        tupple = (split[1],nums1,nums2)
    list_of_tups.append(tupple)
grid = [[0 for j in range(0,1000)] for i in range(0,1000)]
print(len(grid))
time.sleep(2)
def toggle(coord):
    '''
    if (grid[coord[1]][coord[0]] == 0):
        grid[coord[1]][coord[0]] = 1
    else:
        grid[coord[1]][coord[0]] = 0
        '''
    grid[coord[1]][coord[0]]+=2

def on (coord):
    grid[coord[1]][coord[0]] += 1

def off(coord):
    if (grid[coord[1]][coord[0]]>0):
        grid[coord[1]][coord[0]] -= 1
    
#print(list_of_tups)
#time.sleep(30)
for tup in list_of_tups:
    #print(tup)
    for x in range(tup[1][0], tup[2][0]+1):
        for y in range(tup[1][1],tup[2][1]+1):
            #if (isinstance(x,list) or isinstance(y,list)):
        
            #print(x,y)
            if (tup[0]=='toggle'):
                toggle([x,y])
            elif (tup[0]=='on'):
                on([x,y])
            else:
                off([x,y])
    
print(grid)
lit = 0
for yin in grid:
    for xin in yin:
        if (xin > 0):
            lit+=xin
print(lit)
