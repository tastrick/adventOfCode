with open('input.txt') as f:
    l = f.readlines()
nums = []
all_elves = []
curr_elves = 0
#curr_best = 0
for line in l:
    #print(line)
    if (line != '\n'):
        curr = int(line[:-1])
        curr_elves+= curr 
    else:
        all_elves.append(curr_elves)
        #if (curr_elves > curr_best):
        #    curr_best = curr_elves
        curr_elves = 0
        

m1 = max(all_elves)
index1 = all_elves.index(m1)
all_elves.pop(index1)

m2 = max(all_elves)
index2 = all_elves.index(m2)
all_elves.pop(index2)

m3 = max(all_elves)
index3 = all_elves.index(m3)
all_elves.pop(index3)

print(m1+m2+m3)
