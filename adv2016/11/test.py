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
            '''
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
            '''
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
