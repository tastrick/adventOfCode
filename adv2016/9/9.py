with open('input.txt') as f:
    l = f.readlines()
input_str = ''
for line in l:
    input_str=line[:-1]
    
#print(input_str)
def is_decom(s):
    flag = True
    cnt = 0
    for char in s:
        if (char=='('):
            cnt+=1
            flag = False
    return flag,cnt
def decompress(string):
    list_of_extents = []
    final_str = ''
    cnt = 0
    continue_flag = False
    while(cnt<len(string)):
        #print(cnt)
        char = string[cnt]
        #print(char)
        if (char=='('):
            nums = ''
            cnt+=1
            char = string[cnt]
            while(char != ')'):
                nums+=char
                cnt+=1
                char = string[cnt]
            number_split = nums.split('x')
            n = [int(number_split[0]),int(number_split[1])]
            cnt+=1#cnt before this references the  ')' character
            seq = ''
            if (len(string)>=cnt+n[0]):
                m = cnt+n[0]
            else:
                m = len(string)
            for x in range(cnt,m):
                seq+=string[x]
            list_of_extents.append([n,seq])
            for y in range(0,n[1]):
                final_str+=seq
            cnt += n[0]
        else:
            final_str+=char
            cnt+=1
        if (cnt %10000==0):
            print(cnt)
    return final_str,list_of_extents

def calc(string):
    list_of_extents = []
    final = 0
    cnt = 0
    continue_flag = False
    while(cnt<len(string)):
        #print(cnt)
        char = string[cnt]
        #print(char)
        if (char=='('):
            nums = ''
            cnt+=1
            char = string[cnt]
            while(char != ')'):
                nums+=char
                cnt+=1
                char = string[cnt]
            number_split = nums.split('x')
            n = [int(number_split[0]),int(number_split[1])]
            cnt+=1#cnt before this references the  ')' character
            seq = ''
            if (len(string)>=cnt+n[0]):
                m = cnt+n[0]
            else:
                m = len(string)
            for x in range(cnt,m):
                seq+=string[x]
            list_of_extents.append([n,seq])
            #for y in range(0,n[1]):
            #    final_str+=seq
            cnt += n[0]
        else:
            final+=1
            cnt+=1
        if (cnt %10000==0):
            print(cnt)
    return final,list_of_extents


  


f,li = calc(input_str)
print(li,f)
'''
flag,c = is_decom(f)
while(flag==False):
    f = decompress(f)
    flag,c = is_decom(f)
    print(c,len(f))
print(f)
print(len(f))     
'''
