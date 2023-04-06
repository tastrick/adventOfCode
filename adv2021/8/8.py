with open('input.txt') as f:
    l = f.readlines()

i = []
o = []

for line in l:
    tempi = []
    tempo = []
    split = line[:-1].split(' | ')
    input_split = split[0].split(' ')
    output_split = split[1].split(' ')
    for word in input_split:
        new = []
        for char in word:
            new.append(char)
        tempi.append(new)
    i.append(tempi)
    for word in output_split:
        new = []
        for char in word:
            new.append(char)
        tempo.append(new)
    o.append(tempo)

#print('input: ',i)
groups = [[6,9,0],[2,3,5]]
#print('output: ', o)
nums = {('a','b','c','e','f','g'):0,('c','f'):1,('a','c','d','e','g'):2,('a','c','d','f','g'):3,('b','c','d','f'):4,('a','b','d','f','g'):5,('a','b','d','e','f','g'):6,('a','c','f'):7,('a','b','c','d','e','f','g'):8,('a','b','c','d','f','g'):9}

def get_a(list1,list7):
    return( [list(set(list7)-set(list1))[0],'a'])

def get_g(list_of_069,list7,list4):
    for x in list_of_069:
        sub = list(set(x)-set(list7)-set(list4))
        if (len(sub)==1):
            print('returning g')
            return([sub[0],'g'])
        else:
            pass
def get_c(list7,list_of_069,list8):
    for x in list_of_069:
        add = list(set(x).union(set(list7)))
        #print(add,list8, set(add)==set(list8))
        if (set(add) == set(list8)):
            print('returning c')
            return([list(set(list8)-set(x))[0],'c'])
            
        else:
            pass
            
def get_b(list4,list8,list_of_235,list1):
    for x in list_of_235:
        add = list(set(x).union(set(list4)))
        
        print(x,list4,add)
        if (set(add)==set(list8)):
            print('returning b')
            return([list(set(list4)-set(list1)-set(x))[0],'b'])
        
def get_e(list8,list4,a_encoded,g_encoded):
    return([list(set(list8)-set(list4)-set([g_encoded])-set([a_encoded]))[0],'e'])
        
def get_d(list4,list1,b_encoded):
    return([list(set(list4)-set(list1)-set([b_encoded]))[0],'d'])

def get_f(list1,c_encoded):
    return([list(set(list1)-set([c_encoded]))[0],'f'])

final_ans = 0
outputs = []

for count,input1 in enumerate(i):
    encoded_decoded_dict = {}
    list1 = [ii for ii in input1 if len(ii)==2][0]
    list4 = [ii for ii in input1 if len(ii)==4][0]
    list7 = [ii for ii in input1 if len(ii)==3][0]
    list8 = [ii for ii in input1 if len(ii)==7][0]
    list_of_069 = [ii for ii in input1 if len(ii)==6]
    list_of_235 = [ii for ii in input1 if len(ii)==5]
    #print(list1,list4,list7,list8,list_of_069,list_of_235)
    a = get_a(list1,list7)[0]
    encoded_decoded_dict[a] = 'a'
    print('key: ',a,'value: ','a')
    g = get_g(list_of_069,list7,list4)[0]
    encoded_decoded_dict[g] = 'g'
    print('key: ',g,'value: ','g')
    c = get_c(list7,list_of_069,list8)[0]
    encoded_decoded_dict[c] ='c' 
    print('key: ',c,'value: ','c')
    b = get_b(list4,list8,list_of_235,list1)[0]
    encoded_decoded_dict[b] = 'b'
    print('key: ',b,'value: ','b')
    e = get_e(list8,list4,a,g)[0]
    encoded_decoded_dict[e] = 'e'
    print('key: ',e,'value: ','e')
    
    d = get_d(list4,list1,b)[0]
    encoded_decoded_dict[d] = 'd'
    print('key: ',d,'value: ','d')
    
    f = get_f(list1,c)[0]
    encoded_decoded_dict[f] = 'f'
    
    print('key: ',f,'value: ','f')
    print(a,g,c,b,e,d,f)
    print(encoded_decoded_dict)
    string_num = ''
    for num in o[count]:
        new_num = []
        for char in num:
            new_num.append(encoded_decoded_dict[char])
        
        for key in list(nums.keys()):
            if (set(list(key))==set(new_num)):
                string_num+=str(nums[key])
    
        
    outputs.append(int(string_num))
    
print(sum(outputs))
        
        
    


    
