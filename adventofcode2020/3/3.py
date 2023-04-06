f = open("input3.txt", "r")
trees = []
string_length = 0
ans=0
ans_list = []
bad = '#'
good = '.'
for line in f:
    trees.append(line)

f.close()
n=0
while (n < len(trees)):
    trees[n] = (trees[n])[:-1]
    n+=1
#print(trees)    
string_length = len(trees[0])
#print(string_length)
tree_locs = [[0 for i in range(string_length)]for j in range(len(trees))]
n=0    
while (n<len(trees)):
    count=0
    for char in trees[n]:
        #print(char)
        if (char==bad):
            #print(char)
            tree_locs[n][count] = 1
        else:
            tree_locs[n][count]=0
        count+=1
    n+=1

def get_trees(i_start, i_inc ,j_inc):
    ans = 0
    i=i_start
    j=0
    while(i<len(trees)):
        j=j+j_inc
        if (j>30):
            j=abs(30-j)-1
        if (tree_locs[i][j]==1):
            ans+=1
        i=i+i_inc
    return ans

ans_list.append(get_trees(1,1,3))
ans_list.append(get_trees(1,1,1))
ans_list.append(get_trees(1,1,5))
ans_list.append(get_trees(1,1,7))
ans_list.append(get_trees(2,2,1))
y=1
for x in ans_list:
    y=y*x
print(y)
