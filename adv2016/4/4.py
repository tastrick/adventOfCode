import time
from operator import itemgetter
with open('test_input.txt') as f:
    l = f.readlines()

check_sums = []
sector_id = []
encryp_name = []
all_data = []
for line in l:
    split = line[:-1].split('-')
    all_data.append(split)
def copy(l):
    r = []
    for item in l:
        r.append(item)
    return r
print(all_data)
valid_list = []


def is_valid(data):
    flag = True
    checksum = data[-1].split('[')[1][:-1]
    
    data.pop()
    lets = []
    for x in data:
        for c in x:
            lets.append(c)
    amounts = []
    for let in lets:
        if ([lets.count(let),let] not in amounts):
            amounts.append([lets.count(let),let])
    #print('unsorted: ',amounts)
    
    amounts = sorted(amounts,key = lambda x:x[0],reverse = True)
    amounts = sorted(amounts,key = lambda x:x[1])
    
    #top_five = get_top_five()
    print('sorted: ',amounts)
    
    summ = []
    for char in checksum:
        if (lets.count(char)==0):
            flag = False
        elif(char not in top_five):
            flag = False
        
    return flag
for dat in all_data:
    sec = int(dat[-1].split('[')[0])
    val = is_valid(dat)
    if (val):
        valid_list.append(sec)
    print(val)
print(sum(valid_list))
