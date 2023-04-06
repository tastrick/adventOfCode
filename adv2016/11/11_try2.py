import random
import itertools
import time
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
    if(len(arr[3])==10):
        return True
    else:
        return False
def get_possibilities(arr,ele):
    #print('possibilities: ', arr[ele], ele,arr)
    nothing_below = True
    bad_move = ()
    if(moves != []):
        last_move = moves[len(moves)-1]
        if (last_move[-1]==1):
            bad_move = (last_move[0],last_move[1],-1)
        else:
            bad_move = (last_move[0],last_move[1],1)
    for floor in range(ele-1,-1,-1):
        
        if (arr[floor]!=[]):
            nothing_below = False
            
    
    all_poss =[]
    all_singles = arr[ele]
    all_doubles = list(itertools.combinations(arr[ele],2))
    for doubles in all_doubles:
        new_poss = (doubles[0],doubles[1],1)
        #new_poss_2 = (doubles[0],doubles[1],-1)
        all_poss.append(new_poss)
        #all_poss.append(new_poss_2)
    for singles in all_singles:
        #new_poss = (singles,1)
        new_poss_2 = (singles,-1)
        #all_poss.append(new_poss)
        all_poss.append(new_poss_2)
    for singles in all_singles:
        #new_poss = (singles,1)
        new_poss_2 = (singles,1)
        #all_poss.append(new_poss)
        all_poss.append(new_poss_2)
    for doubles in all_doubles:
        new_poss = (doubles[0],doubles[1],-1)
        #new_poss_2 = (doubles[0],doubles[1],-1)
        all_poss.append(new_poss)
        #all_poss.append(new_poss_2)
    
    
    if (ele==0 or nothing_below):
        #print('yes at bottom')
        cc = copy_list(all_poss)
        for yy in cc:
            if (yy[-1]==-1):
                all_poss.remove(yy)
    if(ele == 3):
         #print('yes on top', all_poss)
         c = copy_list(all_poss)
         for y in c:
            #print('outside: ',y, all_poss)
            if (y[-1]==1):
                #print('inside: ',y)
                all_poss.remove(y)
    if (bad_move != () and bad_move in all_poss):
        all_poss.remove(bad_move)
    #print('POSSIBILITIES: ', all_poss)
    return all_poss
def copy_list(l):
    new_l = []
    for x in l:
        new_l.append(x)
    return new_l

start = time.time()

def recurse(arr,elevator,iterator,to_print):
    global start
    too_many_moves = iterator>40
    safe_grid = is_safe_grid(arr)
    solution_grid = is_solved_state(arr)
    #print(too_many_moves,safe_grid,solution_grid,arr)
    #if (moves != []):
    #    print(arr, moves[len(moves)-1])
    #time.sleep(1)
    if (too_many_moves or safe_grid==False):
        #print('before pops: ', moves)
        last_move = moves.pop()
        #print('after pops: ', moves)
        #print(last_move,arr,elevator,moves)
        iterator -=1
        for m in last_move[:-1]:
            arr[elevator].remove(m)
            arr[elevator-last_move[-1]].append(m)
        #print('elevator before: ',elevator)
        elevator-=last_move[-1]
        #print('elevator after: ', elevator)
        return 0,elevator,iterator
    elif(solution_grid):
        #print('solution found')
        last_move = moves.pop()
        iterator -=1
        for m in last_move[:-1]:
            arr[elevator].remove(m)
            arr[elevator-last_move[-1]].append(m)
        elevator-=last_move[-1]
        return 1,elevator,iterator
    else:
        all_possibilities = get_possibilities(grid,elevator)
        #random.shuffle(all_possibilities)
        #print(all_possibilities,elevator)
        for poss in all_possibilities:
            iterator+=1
            #print('ele: ',elevator)
            if (time.time()-start>10):
                start = time.time()
                print(arr[elevator], poss,arr,iterator,elevator, all_possibilities)
            for n in poss[:-1]:
                arr[elevator].remove(n)
                arr[elevator+poss[-1]].append(n)
            elevator+=poss[-1]
            moves.append(poss)
            re,elevator,iterator = recurse(arr,elevator,iterator,to_print)
            #print('recursion result: ', re)
            #time.sleep(1)
            if (re==0):
                pass
            else:
                to_print+=1
                #print('solution found: ', iterator, to_print)
                #time.sleep(1)
                all_solutions[iterator+1] = moves
                if(to_print%1==0):
                    mx = min(list(all_solutions.keys()))
                    print(mx,all_solutions[mx])
        #print(arr,elevator,iterator,moves)
        #time.sleep(1)
        #print('done recurse')
        last_move = moves.pop()
        iterator -=1
        elevator-=last_move[-1]
        for m in last_move[:-1]:
            #print(arr[elevator],m)
            arr[elevator+last_move[-1]].remove(m)
            arr[elevator].append(m)
        #print(elevator)
       
        return 0,elevator,iterator
    
    

all_solutions = {}
iterator = 0
tp = 0
grid = [['PG','PM'],['CG','UG','RG','LG'],['CM','UM','RM','LM'],[]]
#grid = [['HM','LM'],['HG'],['LG'],[]]
moves = []
floor = 0       

recurse(grid,floor,iterator,tp)
