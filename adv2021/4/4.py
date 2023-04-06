with open('input.txt') as f:
    l = f.readlines()
    
l = list(filter(lambda i: i != '\n', l))
print(l)    
def get_nums(string):
    split = string.split(',')
    nums = []
    for char in split:
        nums.append(int(char))
    return nums
nums_to_be_called = l.pop(0)[:-1]
#l.pop(0)
boards = []
new_board = []
for i,x in enumerate(l):
    if (i !=0 and i%5==0):
        boards.append(new_board)
        new_board = [x[:-1]]
    else:
        new_board.append(x[:-1])
boards2 = []        
for board in boards:
    new_board = []
    for line in board:
        split = line.split(' ')
       # print(split)
        split = list(filter(lambda j: j!= '' ,split))
        new_line = []
        for num in split:
            new_line.append(int(num))
        new_board.append(new_line)
    boards2.append(new_board)
#print(boards2)

def star_vals(val, boards):
    for z,board in enumerate(boards):
        for y,line in enumerate(board):
            for x,num in enumerate(line):
                if (num==val):
                    boards[z][y][x] = -1
                    
def check_boards(boards):
    won = False
    winners = [] 
    for z,board in enumerate(boards):
        for y,line in enumerate(board):
            if (line == [-1,-1,-1,-1,-1]):
                if (z not in winners):
                    winners.append(z)
                won = True
                #break_flag = True
                #break
        #if (break_flag):
        #    break
    break_flag = False    
    for z,board in enumerate(boards):
        for i in range(0,len(board)-1):
            col = []
            for line in board:
                col.append(line[i])
            if (col == [-1,-1,-1,-1,-1]):
                if (z not in winners):
                    winners.append(z)
                won = True
                #break_flag = True
                #break
        #if (break_flag):
        #    break
    return won,winners
winners = []
players = len(boards2)
for x in get_nums(nums_to_be_called):
    #print(x)
    star_vals(x,boards2)
    is_won,winn = check_boards(boards2)
    if (is_won):
        print('WINNER: ', winn)
        for ii in winn:
            if (ii not in winners):
                winners.append(ii)
            
        
    if (len(boards2)==len(winners)):
        break
an = winners[len(winners)-1]
print(boards2[an])
    #elif (is_won and len(boards2)==1):
    #    print('second condition')
    #    break
#print(x)

#print(winn)
ans = 0
for line in boards2[an]:
    for num in line:
        if (num != -1):
            ans+=num
            
print(ans*x)

    
    
