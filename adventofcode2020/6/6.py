f = open("input6.txt", "r")
groups = []
group_breaks = []
ans = []
newline = '\n'
for line in f:
    groups.append(line)

f.close()
print(groups)

n=0
while (n < len(groups)):
    if (groups[n]=='\n'):
        group_breaks.append(n)
    n+=1
group_breaks.append(len(groups))
print(group_breaks)
n=0
while (n < len(groups)):
    groups[n]=(groups[n])[:-1]
    n+=1
    
def get_repeats (some_list, num_people):
    total_count = 0
    i =0
    done_chars = []
    #in_flag = 0
    #copy = deep_copy(some_list)
    for chars in some_list:
        try:
            done_chars.index(chars)
        except(ValueError):
            done_chars.append(chars)
            i = some_list.count(chars)
            print(i, chars)
            if (i==num_people):
                total_count+=1
            
    return total_count
#print(groups)
#print(group_breaks)
n=0 
group = 0
group_yes = []
group_disagree = []
not_at_end=0
person = 1
while (n < len(groups)):
    #print(n)
    if (n == group_breaks[group]):
        group+=1
        temp = get_repeats(group_yes, person-1)
        ans.append(temp)
        print(temp, person-1, group_yes)
        group_yes = []
        #group_disagree = []
        person = 0
        #print("new group")
        
    else:
        #print("same group")
        if (len(groups[n])>1):
            for chars in groups[n]:
                #try:
                #    group_yes.index(chars)
                #except(ValueError):
                group_yes.append(chars)
        else:
            #try:
            #    group_yes.index(groups[n])
            #except(ValueError):
            group_yes.append(groups[n])
    person+=1        
    n+=1
#print(group_yes)
ans.append(get_repeats(group_yes, 2))
print(len(ans)==len(group_breaks))
sum_groups = 0
for line in ans:
    sum_groups+=line
    
print(sum_groups)
