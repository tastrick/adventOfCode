with open('input.txt') as f:
    l = f.readlines()

vowels = ['a','e','i','o','u']
bad = [['a','b'],['c','d'],['p','q'],['x','y']]
l2 = []
for line in l:
    new = []
    for char in line:
        new.append(char)
    l2.append(new)

for line in l2:
    line.remove('\n')
print(l2)    
def is_nice(list_of_chars):
    #print(list_of_chars)
    '''
    vowel_cnt = 0
    #get vowel count
    for c in list_of_chars:
        if (c in vowels):
            vowel_cnt+=1
    '''
    #find in a rows
    list_of_pairs=[]
    last = list_of_chars[0]
    for i,c in enumerate(list_of_chars):
        if (i != 0):
            par = [last,c]
            last = c
            list_of_pairs.append(par)
    has_double = False
    for pair in list_of_pairs:
        if (list_of_pairs.count(pair)>=2):
            indexs = [index for index, element in enumerate(list_of_pairs) if element == pair]
            copycat = []
            for i in indexs:
                copycat.append(i)
            sorted(copycat)
            #print(copycat,list_of_pairs)
            st = copycat[0]
            if (copycat[1]>copycat[0]+1):
                has_double = True
                

    list_of_threes = []
    last = list_of_chars[0]
    second_last = list_of_chars[1]
    for m,o in enumerate(list_of_chars):
        if (m>1):
            tre = [last,second_last,o]
            last = second_last
            second_last = o
            list_of_threes.append(tre)
    #print(list_of_threes)        
    has_second = False
    for tre in list_of_threes:
        if (tre[0]==tre[2]):
            has_second = True
            break
    print(has_double, has_second)    
    
    '''
    has_repeat = False
    for pair in list_of_pairs:
        if (pair in bad):
            has_bad = True
            break
    '''
    if (has_double and has_second):
        return True
    else:
        return False
    

good_strings = 0    
for stringl in l2:
    if(is_nice(stringl)):
        good_strings+=1
        
print(good_strings)
    
        
