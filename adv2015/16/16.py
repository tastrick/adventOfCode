with open('input.txt') as f:
    l = f.readlines()


sue_dict = {}#key is index of sue number, value is list of two lists one of the names of detected, and the other of integers

for line in l:
    split = line[:-1].split(' ')
    sue_dict[int(split[1][:-1])] = {split[2][:-1]:int(split[3][:-1]),split[4][:-1]:int(split[5][:-1]),split[6][:-1]:int(split[7])}
    
print(sue_dict)    
to_detect = {'children':3,'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas':0,'goldfish':5, 'trees': 3,'cars': 2,'perfumes': 1}
our_sue = None
for sue in list(sue_dict.keys()):
    all_things = list(sue_dict[sue].keys())
    is_in = list(to_detect.keys())
    is_sue = True
    
    #check nums
    for item in is_in:
        if (item in all_things):
            if (item == 'cats' or item == 'trees'):
                if (sue_dict[sue][item]<=to_detect[item]):
                    is_sue = False
            elif (item == 'pomeranians' or item == 'goldfish'):
                if (sue_dict[sue][item]>=to_detect[item]):
                    is_sue = False
            else:
                if (sue_dict[sue][item]!=to_detect[item]):
                    is_sue = False
                
            
        
    if (is_sue):
        our_sue = sue
        break
    
print(sue)
