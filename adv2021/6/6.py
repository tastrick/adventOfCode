start_state = [1,1,3,5,3,1,1,4,1,1,5,2,4,3,1,1,3,1,1,5,5,1,3,2,5,4,1,1,5,1,4,2,1,4,2,1,4,4,1,5,1,4,4,1,1,5,1,5,1,5,1,1,1,5,1,2,5,1,1,3,2,2,2,1,4,1,1,2,4,1,3,1,2,1,3,5,2,3,5,1,1,4,3,3,5,1,5,3,1,2,3,4,1,1,5,4,1,3,4,4,1,2,4,4,1,1,3,5,3,1,2,2,5,1,4,1,3,3,3,3,1,1,2,1,5,3,4,5,1,5,2,5,3,2,1,4,2,1,1,1,4,1,2,1,2,2,4,5,5,5,4,1,4,1,4,2,3,2,3,1,1,2,3,1,1,1,5,2,2,5,3,1,4,1,2,1,1,5,3,1,4,5,1,4,2,1,1,5,1,5,4,1,5,5,2,3,1,3,5,1,1,1,1,3,1,1,4,1,5,2,1,1,3,5,1,1,4,2,1,2,5,2,5,1,1,1,2,3,5,5,1,4,3,2,2,3,2,1,1,4,1,3,5,2,3,1,1,5,1,3,5,1,1,5,5,3,1,3,3,1,2,3,1,5,1,3,2,1,3,1,1,2,3,5,3,5,5,4,3,1,5,1,1,2,3,2,2,1,1,2,1,4,1,2,3,3,3,1,3,5]

#start_state = [3,4,3,1,2]

fish_dict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
for x in start_state:
    fish_dict[x]+=1
    
print(fish_dict)
#start_state = [3,4,3,1,2]
i = 0
'''
while (i<256):
    end = len(start_state)
    for x in range(0,end):
        
        if (start_state[x]==0):
            start_state.append(8)
            start_state[x] = 6
        else:
            start_state[x]-=1
    #print(start_state)
    i+=1
    print(i)
    
print(len(start_state))
'''
def update():
    tmp = fish_dict[0]
    fish_dict[0] = fish_dict[1]
    fish_dict[1] = fish_dict[2]
    fish_dict[2] = fish_dict[3]
    fish_dict[3] = fish_dict[4]
    fish_dict[4] = fish_dict[5]
    fish_dict[5] = fish_dict[6]
    fish_dict[6] = fish_dict[7]
    fish_dict[7] = fish_dict[8]
    fish_dict[8] = tmp
    fish_dict[6]+=tmp
    
while (i<256):
    
    update()
    #print(fish_dict.values())
    #time.sleep(2)
    i+=1
print(sum(list(fish_dict.values())))
