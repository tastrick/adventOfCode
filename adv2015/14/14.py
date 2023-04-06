with open('input.txt') as f:
    l = f.readlines()
    
name_dict = {}#key is name, value is lsit [speed,long,rest]
state_dict = {}#key name, value [where they are (km),how long in seconds they have been in state, state ('rest','moving')]

for line in l:
    split = line[:-2].split(' ')
    state_dict[split[0]] = [0,0,'moving',0]
    name_dict[split[0]] = [int(split[3]),int(split[6]),int(split[13])]

print(name_dict,state_dict)    
def get_leader():
    
    all_dist = []
    
    for guy in list(state_dict.keys()):
        all_dist.append(state_dict[guy][0])
        
    best = max(all_dist)
    
    for guy2 in list(state_dict.keys()):
        if (state_dict[guy2][0]==best):
            state_dict[guy2][3]+=1
    
def update_states():
    
    
    
    for r in list(state_dict.keys()):
        state_dict[r][1]+=1
        if (state_dict[r][2]=='moving'):
            state_dict[r][0]+=name_dict[r][0]
            if (state_dict[r][1]>= name_dict[r][1]):
                state_dict[r][1]=0
                state_dict[r][2] = 'rest'
        else:
            
            if (state_dict[r][1]>= name_dict[r][2]):
                state_dict[r][1]=0
                state_dict[r][2] = 'moving'
        
        

counter = 0
while(counter<2503):
    update_states()
    get_leader()
    counter+=1
    
#update_states()
    
print(state_dict)

    
