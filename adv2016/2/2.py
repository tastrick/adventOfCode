with open('input.txt') as f:
     l = f.readlines()
     
instructions = []
for line in l:
    instructions.append(line[:-1])

#print(instructions)

dir_dict = {'U':[0,-1],'R':[1,0],'D':[0,1],'L':[-1,0]}

curr_loc = [-2,0]
defined_values = [[0,0],[1,1],[-1,1],[1,-1],[-1,-1],[0,1],[1,0],[-1,0],[0,-1],[0,-2],[0,2],[2,0],[-2,0]]
def copy(lists):
    return_lsit = []
    for x in lists:
        return_lsit.append(x)
    return return_lsit
for line in instructions:
    for char in line:
        for i,move in enumerate(dir_dict[char]):
            c = copy(curr_loc)
            c[i]+=move
            if (c not in defined_values):
                pass
            else:   
                curr_loc[i]+=move
    print(curr_loc)

