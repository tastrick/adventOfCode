import math
f = open("input5.txt", "r")
board = []
row = []
column = []
seat_ID = []
row_max =127
col_max = 7
for line in f:
    board.append(line)

f.close

n=0 
while(n<len(board)):
    board[n] = (board[n])[:-1]
    n+=1
#print(board)
#some_char should be either F or L
def find_num(left, right, some_str, some_char):
    left_bound = left
    right_bound = right
    counter=0
    while(counter<len(some_str)):
        if (some_str[counter]==some_char):
             right_bound = left_bound + (right_bound-left_bound)/2
        else:
            #roof of right/2
            left_bound = right_bound - (right_bound-left_bound)/2
        counter+=1
    return right_bound

n=0
while(n<len(board)):
    curr_row = (board[n])[0:7]
    row_temp = find_num(0,127,curr_row,'F')
    #print(row_temp)
    row.append(row_temp)
    curr_col = (board[n])[7:11]
    col_temp = find_num(0,7,curr_col,'L')
    #print(col_temp)
    column.append(col_temp)
    n+=1
    
n=0
while(n<len(row)):
    seat_ID.append(math.floor(row[n])*8+math.floor(column[n]))
    n+=1
    
seat_ID.sort()
n=1
start = seat_ID[0]
while(n<len(seat_ID)-1):
    if(seat_ID[n]==start+1):
        pass
    else:
        print(start+1)
    start = seat_ID[n]
    n+=1
#print(seat_ID)
#print(max(seat_ID))
