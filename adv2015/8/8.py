import time
with open('input.txt') as f:
    l = f.readlines()
hex_car = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
new = []
orig_string = []
for line in l:
    orig_string.append(line[:-1])
    new_line = []
    for char in line[1:-2]:
        new_line.append(char)
    new.append(new_line)
    #print(new_line)
print(new)
for i,x in enumerate(orig_string):
    pass
    #print(len(new[i]),len(x))
#length of the string is the memory string
#print(orig_string)
#time.sleep(3)
in_mem_to_code = {'\'':1,'\\':1,'\"':1}

num_code = 0
num_enc = 0
def get_copy(l):
    ne = []
    for n in l:
        ne.append(n)
    return ne
def get_num_code(string):
    return 2+len(string)
def get_num_mem(string):
    bad = 0
    copy = get_copy(string)
    print(copy)
    while(copy != []):
        x = copy.pop(0)
        if (x == '\\'):
            if (len(copy)-1>=0):
                if (copy[0]=='\"'):
                    bad+=1
                elif(copy[0]=='\\'):
                    bad+=1
                    copy.pop(0)
                    
                elif(copy[0]=='x'):
                    if(len(copy)-1>=2):
                        if (copy[1] in hex_car and copy[2] in hex_car):
                            bad+=3
            else:
                bad+=1
            #check for x...
            
            #check for "
    return len(string)-bad

def get_num_enc(string):
    add = 6
    copy = get_copy(string)
    print(copy)
    while(copy != []):
        x = copy.pop(0)
        if (x == '\\'):
            if (len(copy)-1>=0):
                if (copy[0]=='\"'):
                    add+=2
                elif(copy[0]=='\\'):
                    add+=2
                    copy.pop(0)
                    
                elif(copy[0]=='x'):
                    if(len(copy)-1>=2):
                        if (copy[1] in hex_car and copy[2] in hex_car):
                            add+=1
            #else:
            #    add+=1
            #check for x...
            
            #check for "
    return len(string)+add
for line in new:
    num_code+=get_num_code(line)
    num_enc+=get_num_enc(line)
print('code: ', num_code)
print('mem: ',num_enc)
print(num_enc-num_code)


