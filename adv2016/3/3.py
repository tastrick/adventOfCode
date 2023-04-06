import itertools
import time
with open('input.txt') as f:
    l = f.readlines()
shapes = []
#print(l)
for line in l:
    split = line[:-1].split('  ')
    split = [x for x in split if x != '']
    ints_l = [int(x) for x in split]
    shapes.append(ints_l)
    
print(shapes)
first_col = [item[0] for item in shapes]
second_col = [item[1] for item in shapes]
third_col = [item[2] for item in shapes]

final = []
for x in first_col:
    final.append(x)
for x in second_col:
    final.append(x)
for x in third_col:
    final.append(x)
shapes = []
new_shape = []
i=1
for item in final:
    new_shape.append(item)
    if (i%3 ==0):
        i = 1
        print(new_shape)
        #time.sleep(1)
        new_shape = []
        shapes.append(new_shape)
    else:
        i+=1
        


valid_l = []
for triangle in shapes:
    valid = True
    for poss in itertools.combinations(triangle,2):
        print(list(set(triangle)-set(poss)))
        if (sum(list(poss))<=sum(list(set(triangle)-set(poss)))):
            valid = False
    if (valid):
        valid_l.append(triangle)
        
print(len(valid_l))
