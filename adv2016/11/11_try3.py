import random

def is_safe_grid(arr):
    state = True
    for floor in arr:
        gens_not_paired = []
        mic_not_paired = []
        has_gen = False
        for element in floor:
            if (element[-1]=='G'):
                has_gen = True
                string = element[0]+'M'
                if (string not in floor):
                    gens_not_paired.append(element)
            else:
                string = element[0]+'G'
                if (string not in floor):
                    mic_not_paired.append(element)
        if ((len(gens_not_paired)>0 and len(mic_not_paired)>0) or (len(mic_not_paired)>0 and has_gen)):
            state = False
            break
            
    return state

def is_solved_state(arr):
    if(len(arr[3])==4):
        return True
    else:
        return False
    
def get_move(arr,fl):
     #get direction of elevator
    dir_flag = False
    dire = 0
    for floor in range(fl-1,-1,-1):
        if (arr[fl]!=[]):
            dir_flag = True
    if (dir_flag):
        dire = random.choice(dirs)
    else:
        dire  = 1
    
    #should we take one or two things?
    if (dire ==-1):
        nums = 1
    else:
        nums = random.randint(1,2)
    if (nums == 1):
        c = [random.choice(arr[elevator])]
    else:
        try:
            c = random.sample(arr[elevator],2)
        except:
            c = [random.choice(arr[elevator])]
    return c,dire    
    
cnt = 0 
all_solutions = {}
max_sc = 100

while(cnt<3000000):
    grid = [['HM','LM'],['HG'],['LG'],[]]
    elevator = 0
    moves = []
    forced_break = False
    step_cnt = 0
    direction = 0
    while(is_solved_state(grid)==False):
        if (step_cnt>50):
            forced_break = True
            break
        else:
            things_to_move, directon = get_move(grid,elevator)
            for x in things_to_move:
                grid[elevator].remove(x)
                grid[elevator+direction].append(x)
            elevator+=direction
        safe = is_safe_grid(grid)
        if(safe==False):
            forced_break = True
            break
    
        step_cnt+=1
    if(forced_break):
        pass
    else:
        all_solutions[step_cnt] = moves
    if (cnt%1000==0 and list(all_solutions.keys())!=[]):
        print('best so far: ', min(list(all_solutions.keys())))
    cnt+=1
