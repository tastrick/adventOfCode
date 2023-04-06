import numpy as np
import cv2
with open('input.txt') as f:
    l = f.readlines()
instructions = []
for line in l:
    instructions.append(line[:-1])
    
#print(instructions)
screen = [[0 for y in range(0,50)] for x in range(0,6)]
#screen = np.array([[0 for y in range(0,50)] for x in range(0,6)])
def generate_blank_im(color, width, height):
        new_im = np.zeros((width,height,3),np.uint8)
        new_color =tuple(reversed(color))
        new_im[:] = (new_color)
        return new_im
def copy(some_l):
    new_l = []
    for l in some_l:
        new_l.append(l)
    return new_l
print(screen)
def roll_row(row_num,step_num):
    c = copy(screen[row_num])
    n = np.array(c)
    n = np.roll(n,step_num)
    screen[row_num] = list(n)
    
def roll_col(col_num,step_num):
    column_of_interest = []
    for y in screen:
        column_of_interest.append(y[col_num])
    n = np.array(column_of_interest)
    n = np.roll(n,step_num)
    for i,item in enumerate(list(n)):
        screen[i][col_num] = item
    
for instr in instructions:
    sp = instr.split(' ')
    if (sp[0] == 'rect'):
        split1 = sp[1].split('x')
        for y in range(0,int(split1[1])):
            for x in range(0,int(split1[0])):  
                screen[y][x] = 1
    elif (sp[0]=='rotate' and sp[1] == 'row'):
        split2 = sp[2].split('=')
        row = int(split2[1])
        amount = int(sp[4])
        roll_row(row,amount)
        #screen.remove(row)
        #destination = (row+amount)%(len(screen)-1)
        
    elif (sp[0]=='rotate' and sp[1]=='column'):
        split2 = sp[2].split('=')
        col = int(split2[1])
        amount = int(sp[4])
        roll_col(col,amount)
final = 0
for row in screen:
    for pixel in row:
        if (pixel==1):
            final+=1


height = len(screen)
width = len(screen[0])
new_im = generate_blank_im((255,255,255),height,width)

for y,row in enumerate(screen):
    for x,col in enumerate(row):
        if (col == 1):
            new_im[y][x] = (0,0,0)
cv2.imwrite('./out.png',new_im)
        
print(final)
    
