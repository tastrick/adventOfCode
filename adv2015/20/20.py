import time
input_num = 34000000
#key is the house number, value is number of presents
loop_state = True
max_len_elvs = 500
inc_len = 500
houses_elves = {1:[1]}#key is house number, value is list ofelve nums

elves_house = {}

def fill_elves_house():
    for e in range(1,inc_len):
        houses = [i for i in range(e,e*max_len_elvs,e)]
        elves_house[e] = houses
        
    
def get_pres_num(k):
    return sum([10*i for i in houses_elves[k]])
def get_loop_state():
    print('func check global: ', input_num)
    state = True
    hus_num = 0
    for key in list(houses_elves.keys()):
        presents = get_pres_num(key)
        if(presents>= input_num):
            state = False
            hus_num = key
            print(houses_elves[key])
    return state,hus_num

def get_elves(inc1):
    elves_list = []
    for j in range(inc1,inc1*max_len_elvs,inc1):
        elves_list.append(j)
        
    return elves_list
def get_to_be_added(c):
        list_of_elfs = []
        for elf in list(elves_house.keys()):
            if (c in elves_house[elf]):
                list_of_elfs.append(elf)
                
        return list_of_elfs
def fill_dict(inc):
    for i in range(len(list(houses_elves.keys()))+1,len(list(houses_elves.keys()))+inc):
        print('len of list: ', i)
        
        houses_elves[i] = get_to_be_added(i)
        
        print(i,houses_elves[i])
        time.sleep(2)
   
    
    '''
def fill_dict(inc):
    houses_elves[inc] = get_gelves(inc)
    return inc+1
'''
while(loop_state):  
    fill_elves_house()
    fill_dict(max_len_elvs)
    
    loop_state,hous_num = get_loop_state()
    

print(hous_num)
print(get_pres_num(hous_num))
