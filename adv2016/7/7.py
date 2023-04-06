import time
with open('input.txt') as f:
    l = f.readlines()
input_strings = []
for line in l:
    input_strings.append(line[:-1])

def is_abba(list_strings):
    flag = False
    for seg in list_strings:
        for i,char in enumerate(seg):
            #print(i)
            if (i<len(seg)-1 and seg[i+1]==seg[i]):
                if (i>0 and i<len(seg) -2 and seg[i-1]==seg[i+2] and seg[i-1]!=char):
                    flag = True
                    #print('it is true')
                    break
        if (flag == True):
            break
    return flag

def is_aba_out(list_strings):
    abas = []
    for string in list_strings:
        for i,char in enumerate(string):
            if (i<len(string)-1):
                if (i>0 and string[i-1]==string[i+1] and string[i-1] != char):
                    aba = [string[i-1],string[i],string[i+1]]
                    abas.append(aba)
    return abas
def is_bab_in(list_strings,aba_list):
    flag = False
    for string in list_strings:
        for i,char in enumerate(string):
            if (i<len(string)-1):
                if (i>0 and string[i-1]==string[i+1] and string[i-1] != char):
                    if ([string[i],string[i-1],string[i]] in aba_list):
                        flag=True
                        break
        if (flag):
            break
    return flag
#print(input_strings)
inc = 0
for string in input_strings:
    out_brackets = []
    in_brackets = []
    flag = False
    new_out = []
    new_in = []
    for char in string:
        if (flag):
            if (char == ']'):
                in_brackets.append(new_in)
                new_in = []
                flag = False
            else:
                new_in.append(char)
        if (char == '['):
            flag = True
            out_brackets.append(new_out)
            new_out = []
        if (flag ==False and char !=']'):
            new_out.append(char)
    out_brackets.append(new_out)
    abas_l = is_aba_out(out_brackets)
    if (is_bab_in(in_brackets,abas_l)):
    #if (is_abba(out_brackets) and is_abba(in_brackets)==False):
        #print(in_brackets,out_brackets)
        inc+=1
    #print(out_brackets)
    #print(in_brackets)
    #time.sleep(2)
    
print(inc)
