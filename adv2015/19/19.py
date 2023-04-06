import time
from random import shuffle
with open('input.txt') as f:
    l = f.readlines()
all_data =[]
for line in l:
    all_data.append(line[:-1])
all_data.remove('')
input_string = all_data[len(all_data)-1]
print(input_string)
all_data.pop()
all_rules = []
change_dict = {}
for b in all_data:
    split = b.split(' ')
    change_dict[split[0]] = []
    all_rules.append([split[0],split[2]])
for a in all_data:
    split = a.split(' ')
    change_dict[split[0]].append(split[2])
#print(all_data)
#print(change_dict)
final = []
for char in input_string:
    final.append(char)
    
def get_pairs(lo):
    u = copy(lo)
    start = u.pop(0)
    all_pairs = []
    while(u != []):
        all_pairs.append([start,u[0]])
        start = u.pop(0)
    return all_pairs
def copy(li):
    new = []
    for x in li:
        new.append(x)
        
    return new

def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list

def get_all_molecules_str(m):
    
    all_molecules = []    
    mole = []
    for cha in m:
        mole.append(cha)
    keys = list(change_dict.keys())
    for i,c in enumerate(mole):
        co = copy(mole)
        if (c in keys):
            for item in change_dict[c]:
                co[i] = item
                all_molecules.append(co)
                co = copy(mole)
        
        if (i+1<len(final)):
            curr_pair_str = c+final[i+1]
            #print(curr_pair_str)
            if (curr_pair_str in keys):
                for item in change_dict[curr_pair_str]:
                    co[i] = item
                    del co[i+1]
                    all_molecules.append(co)
                    co = copy(mole)
    all_strings = []
    for mol in all_molecules:
        new_str = ''
        for char in mol:
            new_str+=char
        all_strings.append(new_str)
    return all_strings
            
def check_consist(str_val):
    is_consist = True
    lett_list = []
    
    for char in str_val:
        lett_list.append(char)
        
    for i,x in enumerate(lett_list):
        if(x != final[i]):
            is_consist = False
            break
    return is_consist
'''
done = ['e']
groups = []
attempt_dict = {}
groups.append(done)
keep_going = True
list_of_lists = []
count = 0
some_dict = {}
while (keep_going):
    curr = done.pop(0)
    #print(curr)
    #time.sleep(1)
    alll = get_all_molecules_str(curr)
    for strimol in alll:
        if (strimol==input_string):
            keep_going = False
    if (len(curr)<=len(input_string)):
        for x in alll:
            done.append(x)
        groups.append(alll)
    if (count%100000==0):
        print(len(curr))
        print(len(done))
    
    count+=1




fin = 0
for i,d in enumerate(groups):
    for j,f in enumerate(d):
        if (f == input_string):
            fin = j
            

print(fin)        
print(len(groups)-1)
print(count)
#print(all_molecules)
'''

#attempt 2

mol = input_string
done = 'e'
c=0
target = mol
while(target!=done):
    tmp = target
    for a,b in all_rules:
        if(b not in target):
            continue
        target = target.replace(b,a,1)
        c+=1
    if (tmp==target):
        c = 0
        shuffle(all_rules)
    
print(c)




