import time
import random
import itertools
#grid = [['PG','PM'],['CG','UG','RG','LG'],['CM','UM','RM','LM'],[]]
#grid = [['HM','LM'],['HG'],['LG'],[]]
def is_safe(arr):
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
def is_not_in_final_state(arr):
    #print(grid)
    if(len(arr[3])==10):
        return False
    else:
        return True
def last_assump_bad(last_assump,arr):
    #print(grid)
    for x in last_assump[:-1]:
        arr[elevator].remove(x)
        arr[elevator-last_assump[-1]].append(x)
def contents_elevator(conts):
    st = True
    if (len(conts)>1):
        if (conts[0][-1]!= conts[1][-1] and conts[0][0] != conts[1][0]):
            st = False
    
    return st
def check_pair_state(a):
    state = True
    all_m = []
    all_g = []
    for ele in a[elevator]:
        if (ele[-1]=='M'):
            all_m.append(ele)
        else:
            all_g.append(ele)
    if (len(all_m)<=1 and len(all_g)<=1):
        if (len(all_m)==0 or len(all_g)==0):
            state = False
        else:
            if(all_m[0][0]!=all_g[0][0]):
                state = False
    return state

def gen_move(arr):
    
    #get direction of elevator
    dir_flag = False
    dire = 0
    for floor in range(elevator-1,-1,-1):
        if (arr[floor]!=[]):
            dir_flag = True
    if (dir_flag):
        dire = random.choice(dirs)
    else:
        dire  = 1
    
    #should we take one or two things?
    nums = random.randint(1,2)
    if (nums == 1):
        c = [random.choice(arr[elevator])]
    else:
        try:
            c = random.sample(arr[elevator],2)
        except:
            c = [random.choice(arr[elevator])]
    return dire,c
    
    

def roll_back():
    pass
#two directions up and down 1 is up and 0 is down
sta = True
dirs = [-1,1]
all_totals = {100:[]}
cnt=0
while(cnt<10000000):
    elevator = 0
    moves = []
    in_bad_assump = False
    move_cnt = 0
    sf = False
    grid = [['PG','PM'],['CG','UG','RG','LG'],['CM','UM','RM','LM'],[]]
    #grid = [['HM','LM'],['HG'],['LG'],[]]
    cn_bad = 0
    tried_all = []
    tries = []
    forced_break = False
    while (is_not_in_final_state(grid)):
        #print(grid)
        
        #how_many = random.randint(1,2)
        #print(how_many,grid[elevator])
        #if (tried_all):
        #    forced_break = True
        #    break
        direction, to_move = gen_move(grid)
        if (direction==-1):#down
            if(elevator==0):
                continue
            else:
                move = []
                for item in to_move:
                    move.append(item)
                    grid[elevator].remove(item)
                    grid[elevator-1].append(item)
                move.append(direction)
                moves.append(move)
                move_cnt+=1
                elevator-=1
                
        else:
            if(elevator==3):
                continue
            else:
                move = []
                for item in to_move:
                    move.append(item)
                    #print(grid[elevator],item)
                    #print(to_move)
                    #print('moving : ', item, ' to ',elevator+1, moves)
                    grid[elevator].remove(item)
                    grid[elevator+1].append(item)
                move.append(direction)
                elevator+=1
                moves.append(move)
                move_cnt+=1
        grid_state= is_safe(grid)
        #print('grid_state: ', grid_state, 'grid: ', grid, 'move: ', moves)
        #time.sleep(1)
        #if(grid_state==False):
        #   forced_break = True
        #   break
           
        
        if (grid_state == False):
            #print('not valid')
            in_bad_assump = True
            bad_move = moves.pop()
            tries.append(bad_move)
            last_assump_bad(bad_move,grid)
            #print('before: ', move_cnt)
            move_cnt-=1
            #print('after: ', move_cnt)
            elevator-=direction
        else:
            if (in_bad_assump==True):
                tried_all.append(tries)
                tries = []
                cn_bad = 0
                in_bad_assump = False
        if (in_bad_assump):
            cn_bad+=1
        if (cn_bad>100):
            forced_break = True
            break
        
        
    
    if (forced_break):  
        pass
    else:
        if (cnt%1 == 0):
            print('solution')
       # print(grid)
            print('interation: ',cnt,'minimum moves: ',min(list(all_totals.keys())))
        #'moves: ', all_totals[min(list(all_totals.keys()))])
        all_totals[move_cnt] = moves
        cnt+=1
    
    #less than 113 and 99 not right not 95 not 67
    
    
'''
def gen_mov(arr):
    cnt_state = False
    done_state = False
    #get direction
    dir_flag = False#false to having to do down 
    
    #we have access to bad_move and tries
    if(in_bad_assump):
        all_ups = []
        all_downs = []
        for t in tries:
            if (t[-1]==-1):
                all_downs.append(t[:-1][0])
            else:
                all_ups.append(t[:-1])
        all_singles_in_ups = []
        all_doubles_in_ups = []
        for x in all_ups:
            if(len(x)==1):
                all_singles_in_ups.append(x[0])
            else:
                all_doubles_in_ups.append(tuple(x))
                
        all_possible_singles = arr[elevator]
        all_possible_doubles = list(itertools.combinations(arr[elevator],2))
        #print('ALL: ',all_singles_in_ups, all_possible_singles,all_doubles_in_ups,all_possible_doubles)
        #time.sleep(1)
        
        #print('SINGLES LEFT: ', list(set(all_possible_singles)-set(all_singles_in_ups)), 'DOUBLES LEFT: ', list(set(all_possible_doubles)-set(all_doubles_in_ups)))
        
        
        #print(list(set(all_possible_singles)-set(all_singles_in_ups))==[] and list(set(all_possible_doubles)-set(all_doubles_in_ups))==[])
        
        if(list(set(all_possible_singles)-set(all_singles_in_ups))==[] and list(set(all_possible_doubles)-set(all_doubles_in_ups))==[] and list(set(all_possible_singles)-set(all_downs))==[]):
            print('---------------------------------STOP----------------------------------')
            return cnt_state,0,0,True
        else:
            #build all possible moves left, and we will try one at random
            moves_left_down = list(set(all_possible_singles)-set(all_downs))
            moves_left_up_singles = list(set(all_possible_singles)-set(all_singles_in_ups))
            moves_left_up_doubles = list(set(all_possible_doubles)-set(all_doubles_in_ups))
            
            all_moves = []
            for md in moves_left_down:
                all_moves.append((md,-1))
            for mus in moves_left_up_singles:
                all_moves.append((mus,1))
            for mud in moves_left_up_doubles:
                all_moves.append((mud[0],mud[1],1))
                
            new_move = random.choice(all_moves)
            #print('all moves: ', all_moves,'NEW MOVE: ', new_move)
            return False,new_move[-1],new_move[:-1],False
            
            
            
            
        # at have we tried all possible twos and ones? if so we need to roll back on the new move
    else:
        for floor in range(elevator-1,-1,-1):
            if (arr[floor]!=[]):
                dir_flag = True
        if (dir_flag):
            dire = random.choice(dirs)
        else:
            dire  = 1
        
        if (dire == -1):
            hm = 1
        else:
            
            can_move_two = check_pair_state(arr)
            if (can_move_two):
                hm = random.randint(1,2)
            else:
                hm = 1
            
            list_of_pairs_tried = []
            list_of_singles_tried = []
            for t in tried:
                if (len(t)==2):
                    list_of_singles_tried.append(t[:-1])
                else:
                    list_of_pairs_tried.append(tuple(t[:-1]))
            all_pairs = list(itertools.combinations(arr[elevator],2))
            all_singles = arr[elevator]
            #print('all combs: ', all_pairs, 'floor: ', arr[elevator])
            print('all possible pairs: ', all_pairs, ' pairs tried: ', list_of_pairs_tried, ' all possible singles: ', all_singles, ' singles tried: ', list_of_singles_tried)
            if (set(list_of_pairs_tried)==set(all_pairs)):
                if (set(list_of_singles_tried)==set(all_singles)):
                    done_state = True
                hm = 1
                print('yes tried all')
            
            hm = random.randint(1,2)
            
        if(hm==1):
            tm = [random.choice(arr[elevator])]
        else:
            try:
                tm = random.sample(arr[elevator],2)
            except:
                cnt_state = True
        while (contents_elevator(tm)==False):    
            hm = random.randint(1,2)
            #print(how_many,grid[elevator])
            if(hm==1):
                tm = [random.choice(grid[elevator])]
            else:
                try:
                    tm = random.sample(grid[elevator],2)
                except:
                    cnt_state = True
        return cnt_state,dire,tm,done_state
'''
