f = open("input11.txt", "r")
seat = []
for line in f:
    line = line[:-1]
    seat.append(line)
    
print(seat)
string_length = len(seat[0])
orig = [[0 for i in range(string_length)]for j in range(len(seat))]
#print(seat_tot)
n=0
while(n<len(seat)):
    count=0
    for char in seat[n]:
        if (char=='L'):
            orig[n][count]=0
        else:
            orig[n][count]=2
        count+=1
    n+=1
print(orig)

def deep_copy(somelist):
    string_length=len(somelist[0])
    newlist = [[0 for i in range(string_length)]for j in range(len(somelist))]
    i=0
    while(i<len(somelist)):
        j=0
        while(j<len(somelist[0])):
            newlist[i][j]=somelist[i][j]
            j+=1
        i+=1
    return newlist

def get_neighs(index_i, index_j):
    num=0
    if (index_j>0 and seat_num[index_i][index_j-1]==1):
        num+=1
    if(index_j<len(seat[0])-1 and seat_num[index_i][index_j+1]==1):
        num+=1
    if(index_i < len(seat_num)-1 and seat_num[index_i+1][index_j]==1):
        num+=1
    if(index_i < len(seat_num)-1 and index_j>0 and seat_num[index_i+1][index_j-1]==1):
        num+=1
    if (index_i < len(seat_num)-1 and index_j < len(seat[0])-1 and seat_num[index_i+1][index_j+1]==1):
        num+=1
    if (index_i>0 and seat_num[index_i-1][index_j]==1):
        num+=1
    if(index_i>0 and index_j< len(seat[0])-1 and seat_num[index_i-1][index_j+1]==1):
        num+=1
    if (index_i>0 and index_j>0 and seat_num[index_i-1][index_j-1]==1):
        num+=1
    return num

def get_neighs_2(index_i, index_j):
    num=0
    temp = diagonal_rLL(index_i,index_j, num)
    temp1 = diagonal_rLU(index_i, index_j, temp)
    temp2 = diagonal_rRL(index_i,index_j, temp1)
    temp3 = diagonal_rRU(index_i, index_j, temp2)
    temp4 = up(index_i,index_j,temp3)
    temp5 = down(index_i,index_j,temp4)
    temp6 = left(index_i, index_j, temp5)
    temp7 = right(index_i,index_j, temp6)
    return temp7


def diagonal_rLU(i,j, number):
    if (i>0 and j>0):
        if (seat_num[i-1][j-1]==1):
            number+=1
            return number
        elif(seat_num[i-1][j-1]==0):
            return number
        else:
            return diagonal_rLU(i-1,j-1, number)
    else:
        return number
def diagonal_rRL(i,j,number):
    if (i<len(seat_num)-1 and j<len(seat[0])-1):
        if (seat_num[i+1][j+1]==1):
            number+=1
            return number
        elif(seat_num[i+1][j+1]==0):
            return number
        else:
            return diagonal_rRL(i+1,j+1, number)
    else:
        return number

def diagonal_rRU(i,j,number):
    if (i>0 and j<len(seat[0])-1):
        if (seat_num[i-1][j+1]==1):
            number+=1
            return number
        elif(seat_num[i-1][j+1]==0):
            return number
        else:
            return diagonal_rRU(i-1,j+1, number)
    else:
        return number
    
def diagonal_rLL(i,j,number):
    if (i<len(seat_num)-1 and j>0):
        if (seat_num[i+1][j-1]==1):
            number+=1
            return number
        elif(seat_num[i+1][j-1]==0):
            return number
        else:
            return diagonal_rLL(i+1,j-1, number)
    else:
        return number

def up(i,j,number):
    if (i>0):
        if (seat_num[i-1][j]==1):
            number+=1
            return number
        elif(seat_num[i-1][j]==0):
            return number
        else:
            return up(i-1,j, number)
    else:
        return number

def down(i,j,number):
    if (i<len(seat_num)-1):
        if (seat_num[i+1][j]==1):
            number+=1
            return number
        elif(seat_num[i+1][j]==0):
            return number
        else:
            return down(i+1,j, number)
    else:
        return number
    
def right(i,j,number):
    if (j<len(seat[0])-1):
        if (seat_num[i][j+1]==1):
            number+=1
            return number
        elif(seat_num[i][j+1]==0):
            return number
        else:
            return right(i,j+1, number)
    else:
        return number
    
def left(i,j,number):
    if (j>0):
        if (seat_num[i][j-1]==1):
            number+=1
            return number
        elif(seat_num[i][j-1]==0):
            return number
        else:
            return left(i,j-1, number)
    else:
        return number
n=0
changed = deep_copy(orig)
while(True):
    change_counter=0
    i=0
    seat_num=deep_copy(changed)
    while(i<len(seat_num)):
        j=0
        while(j<len(seat[0])):
            if (seat_num[i][j]!=2):
                num_neighs = get_neighs_2(i,j)
                #print(i,j,num_neighs)
                if(num_neighs==0 and seat_num[i][j]==0):
                    change_counter+=1
                    changed[i][j]=1
                if(num_neighs>=5 and seat_num[i][j]==1):
                    change_counter+=1
                    changed[i][j]=0
            j+=1
        i+=1
    print(changed)
    if (change_counter==0):
        #print(seat_num)
        print(n)
        break
    n+=1
    
i=0
count=0
while(i<len(seat_num)):
    j=0
    while(j<len(seat[0])):
        if (seat_num[i][j]==1):
           count+=1
        j+=1
    i+=1
    
print(count)
        
