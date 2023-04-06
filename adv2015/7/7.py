import time
with open('input.txt') as f:
    l = f.readlines()
s = ['RSHIFT','LSHIFT','NOT','AND','OR']
ins = []
inst_dict_after = {}
list_of_unknown_logic = []
list_of_identifiers = []
for instruction in l:
    split = instruction.split(' ')
    print(split)
    split[len(split)-1] = split[len(split)-1].replace('\n','')
    split.remove('->')
    ins.append(split)
    
print(ins)
def get_operands(com):
    
    if (com[1]=='RSHIFT'):
        return [com[0],com[2]]
    elif(com[1]=='LSHIFT'):
        return [com[0],com[2]]
    elif(com[1]=='AND'):
        return [com[0],com[2]]
    elif(com[0]=='NOT'):
        return [com[1]]
    elif(com[1]=='OR'):
        return [com[0],com[2]]
    else: #com[0] is either an signal or a identifier
        return [com[0]]
for x in ins:
    list_of_identifiers.append(x[len(x)-1])
    
for xi in ins:
    ops = get_operands(xi)
    for o in ops:
        if (o.isnumeric()==False):
            list_of_identifiers.append(o)
    
for y in list_of_identifiers:
    inst_dict_after[y] = None

inst_dict_after['b'] = 46065    
def perform_comand(com,ops):
    dest = com[len(com)-1]
    nums = []
    for i,x in enumerate(ops):
        if (x.isnumeric()==False):
            nums.append(inst_dict_after[x])
        else:
            nums.append(int(x))
    print(nums)
    if (com[1]=='RSHIFT'):
        inst_dict_after[dest] = nums[0] >> nums[1]
    elif(com[1]=='LSHIFT'):
        inst_dict_after[dest] = nums[0] << nums[1]
    elif(com[1]=='AND'):
        inst_dict_after[dest] = nums[0] & nums[1]
    elif(com[0]=='NOT'):
        inst_dict_after[dest] = 65535-nums[0]
    elif(com[1]=='OR'):
        inst_dict_after[dest] = nums[0] | nums[1]
    else: #com[0] is either an signal or a identifier
        inst_dict_after[dest] = nums[0]
def is_filled(instruct):
    fo = True
    ops_in = get_operands(instruct)
    for o in ops_in:
        if (o.isnumeric()==False):
            if(inst_dict_after[o]==None):
                fo = False
    return fo
        
def run(instruct):
    #print(list_of_unknown_logic)
    ops = get_operands(instruct)
    flag = is_filled(instruct)
    if(flag):
        perform_comand(instruct,ops)
        #check all unknown operations to see if we have any that are capable of recieving signals now
        continue_flag = True
        while(continue_flag):
            continue_flag = False
            for unknow in list_of_unknown_logic:
                if (is_filled(unknow)):
                    print('YES')
                    ops2 = get_operands(unknow)
                    perform_comand(unknow,ops2)
                    list_of_unknown_logic.remove(unknow)
                    continue_flag = True
    else:
        list_of_unknown_logic.append(instruct)

        #print(list_of_unknown_logic)
        #time.sleep(2)
        #list_of_unknown_logic.remove(unknow)
for inst in ins:
    run(inst)
    
for u in list_of_unknown_logic:
    if (is_filled(u)):
        ops2 = get_operands(u)
        perform_comand(u,ops2)
#print(inst_dict_after)
print(inst_dict_after['a'])
