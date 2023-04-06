import time
input_num = 34000000

max_len_houses_checked = 50#this is the number of elves and houses to go to in the first max_len_houses_checked
elf_length = 300
chuck_incrementer = 300

def elf_elf_houses(chunk):
    elf_houses = {}
    for x in range(1,elf_length*chunk):
        elf_houses[x] = [i for i in range(x,x*max_len_houses_checked,x)]
    return elf_houses

def get_elves_in_house(chunk,dict_elves):
    house_dict = {}
    for house in range(1,chunk*max_len_houses_checked):
        elves_tot = []
        print(house)
        for elf in list(dict_elves.keys()):
            if(house in dict_elves[elf]):
                elves_tot.append(elf)
        house_dict[house] = elves_tot
    return house_dict
def get_pres(ho,house_dict):
    return sum([10*i for i in house_dict[ho]])


def get_pres_num(n):
    l = []
    b = []
    
    
    
    for x in range(1,n+1):
        if ((n/x).is_integer()):
            l.append(11*x)
            b.append(x)
            
    for elf in b:
        houses = [h for h in range(elf,50*elf,elf)]
                                   
        if (n not in houses):
            ind = l.index(11*elf)
            l.pop(ind)
    
        
            
    #print(l,n)
    #time.sleep(1)
    return sum(l),l
state = True
final = 0
i = 810900
alll = []

while(final<input_num):
    final,li = get_pres_num(i)
    
    if (i%100 ==0):
        print(i,final,li)
    #time.sleep(1)
        
    i+=2
print(i)
#786252 no
#786360 no
#847920
