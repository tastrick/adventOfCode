with open('input.txt') as f:
    l = f.readlines()
instructions = []
for item in l:
    instructions.append(item[:-1])
    
print(instructions)

inst = []
for x in instructions:
    split = x.split(' ')
    if (len(split)>2):
        new = (split[0],split[1][:-1],split[2])
    else:
        new = (split[0],split[1])
    inst.append(new)
    
print(inst)
inst_dict = {'inc':[],'jmp':[],'tpl':[],'jio':[],'jie':[],'hlf':[]}
start = {'a':1,'b':0}
keep_going = True
inc = 0

def run_instruction(i):
    i_has_changed = False
    this_ins = inst[i]
    if (this_ins[0] == 'inc'):
        start[this_ins[1]]+=1
    elif(this_ins[0]=='jmp'):
        i += int(this_ins[1])
        i_has_changed = True
    elif (this_ins[0]=='tpl'):
        start[this_ins[1]]*=3
    elif (this_ins[0]=='jio'):
        print(start[this_ins[1]])
        if (start[this_ins[1]]==1):#odd
            i+=int(this_ins[2])
            print(int(this_ins[2]))
            i_has_changed = True
    elif (this_ins[0]=='jie'):
        if (start[this_ins[1]]%2==0):#one
            i+=int(this_ins[2])
            print(int(this_ins[2]))
            i_has_changed = True
    elif (this_ins[0]=='jmp'):
        i+=int(this_ins[1])
        print(int(this_ins[2]))
        i_has_changed = True
    elif (this_ins[0]=='hlf'):
        #print(start[this_ins])
        start[this_ins[1]] = int(start[this_ins[1]]/2)
    if (i_has_changed):
        return i
    else:
        return i+1
    
while(True):
    inc = run_instruction(inc)
    if (inc>=len(inst)):
        break
    print(start)
print(start['b'],start['a'])
    
    
    

