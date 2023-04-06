inp = '1113222113'
new = []
for char in inp:
    new.append(char)
count = 0
def copy(l):
    n = []
    for i in l:
        n.append(i)
    return n
while(count <50):
    new_replacement = []
    c = copy(new)
    start = c.pop(0)
    curr_count = 1
    while(c != []):
        if (c[0] != start):
            new_replacement.append(str(curr_count))
            new_replacement.append(start)
            start = c.pop(0)
            curr_count = 1
        elif(c[0]==start):
            curr_count+=1
            c.pop(0)
    new_replacement.append(str(curr_count))
    new_replacement.append(start)
    new = copy(new_replacement)
    count+=1
    #print('done: ',count, new)
    print(count)
            #
        #update new
print(len(new))        
