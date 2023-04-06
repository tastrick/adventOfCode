with open('input.txt') as f:
    l = f.readlines()
wins = [["A","Y"],["C","X"], ["B","Z"]]
loose_dict = {"A":"Z","B":"X","C":"Y"}
win_dict = {"A":"Y","C":"X","B":"Z"}
all = []
for line in l:
   s = line.split(" ")
   #print(s)
   all.append([s[0], s[1][0]])

#print(all)
p_dict = {"X":1,"Y":2,"Z":3}  
same = {"A":"X","B":"Y","C":"Z"}
def winner(l):
    if (l in wins):
        #print("winner!")
        return True
    else:
        return False
def issame(l):
    if (same[l[0]]==l[1]):
        return True
    else:
        return False
total = 0
for round1 in all:
    game_points = 0
    if (issame(round1)):
        game_points+=3
    elif winner(round1):
        game_points+=6
    game_points+=p_dict[round1[1]]
    total+=game_points

#print(total)
        
#part 2
total = 0
for round1 in all:
    newmove = [round1[0],round1[1]]
    if (round1[1]=="X"):
        newmove[1]=loose_dict[round1[0]]
    elif (round1[1]=="Y"):
        newmove[1]=same[round1[0]]
    elif (round1[1]=="Z"):
        newmove[1]=win_dict[round1[0]]
    
    game_points = 0
    if (issame(newmove)):
        game_points+=3
    elif winner(newmove):
        game_points+=6
    game_points+=p_dict[newmove[1]]
    total+=game_points
print(total)
