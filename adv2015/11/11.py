import string

input_string = 'hepxxzaa'
#input_string = 'ghijklmn'
#input_string ='abcdefgh'
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def get_list_of_threes(lo):
    c = copy(lo)
    list_of_threes = []
    one = c.pop(0)
    two = c.pop(0)
    while(c!=[]):
        new_ele = [one,two,c[0]]
        list_of_threes.append(new_ele)
        one = two
        two = c.pop(0)
    
    return list_of_threes
def copy(li):
    neww = []
    for item in li:
        neww.append(item)
    return neww
have_tried_dict = {}

for i in range(0,8):
    have_tried_dict[i] = []

print(have_tried_dict)
bad = ['i','o','l']
valid = False
threes = get_list_of_threes(lower)

def str_to_list(s):
    l = []
    for char in s:
        l.append(char)
    return l



def get_list_of_twos(l1):
    c = copy(l1)
    list_of_twos = []
    one = c.pop(0)
    while(c!=[]):
        new_ele = [one,c[0]]
        list_of_twos.append(new_ele)
        one = c.pop(0)
    
    return list_of_twos

def check_valid(list_of_chars):
    flag = False
    threes_to_check = get_list_of_threes(list_of_chars)
    first_condition = False
    second_condition = True
    third_condition = False
    for t in threes:
        if (t in threes_to_check):
            first_condition = True
            break
    
    for x in list_of_chars:
        if (x in bad):
            second_condition = False
            break
    
    list_of_twos_to_check = get_list_of_twos(list_of_chars)
    
    count_of_pairs = 0
    last_index = 0
    for i, item in enumerate(list_of_twos_to_check):
        if (item[0]==item[1] and count_of_pairs == 0):
            count_of_pairs+=1
            last_index = i
        elif(item[0]== item[1] and count_of_pairs>0):
            if (i>last_index+1):
                count_of_pairs+=1
    
    if(count_of_pairs>=2):
        third_condition = True

    
    if (first_condition and second_condition and third_condition):
        flag = True
    
    return flag
def get_next_gu(curr_lett):
    next_let = ''
    if (curr_lett=='z'):
        next_let = 'a'
    else:
        index_in = lower.index(curr_lett)
        next_let = lower[index_in+1]
    return next_let
#def get_guess_state(m):
#    state = set(lower)==set(have_tried_dict[m])
    #print(state)
#    return state
def get_guess_state(lis,m):
    if (lis[m]=='z'):
        return True
    else:
        return False
def roll_back(ld,index):
    while(get_guess_state(ld,index)):
        ld[index] = 'a'
        index -=1
    orig = str_to_list(input_string)
    #for x in range(index+1,8):
    #    ld[x] = 'a'
    return ld, index
    
def get_next(som,i):
    c = copy(som)
    have_rolled_back = False
    guessed_state = get_guess_state(c,i)
    if (guessed_state):
        c,i = roll_back(c,i)
        have_rolled_back = True
 
    lett = get_next_gu(c[i])
    
    c[i] = lett
    #have_tried_dict[i].append(lett)
    i = 7
    #if (i!=7):
    #    i+=1
    return c,i

s1 = str_to_list(input_string)
valid = check_valid(s1)
curr_index_for_guess = 7
count = 0
while(valid == False):
    
    s1,curr_index_for_guess = get_next(s1, curr_index_for_guess)
    #print(s1)
    valid  = check_valid(s1)
    if (count%100000 == 0):
        print(s1)
    count+=1
    
    
print('final: ', s1)

'''
# update the string list
def get_next_string(stringlist,index):
    #check if weve used all possibilities
    #print(have_tried_dict)
    while (lower == have_tried_dict[index]):
        index -=1
        have_tried_dict[index] = []
        #print(index)
    ind_of_curr_low = lower.index(stringlist[index])+1
    for y in lower[ind_of_curr_low:]:
        if (y in have_tried_dict[index]):
            ind_of_curr_low = 0
            
    
    for element in lower[ind_of_curr_low:]:
        if (element not in have_tried_dict[index]):
            have_tried_dict[index].append(element)
            stringlist[index] = element
            break
    return stringlist,index

print(check_valid(str_to_list(input_string)))
'''

'''    
threes = get_list_of_threes(lower)
s1 = str_to_list(input_string)
valid = check_valid(s1)
index = 7
while (valid ==False):
    s1,index = get_next_string(s1,index)
    print(s1)
    valid = check_valid(s1)
    
print(s1)
'''
