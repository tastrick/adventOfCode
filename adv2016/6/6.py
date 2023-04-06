from collections import Counter
with open('input.txt') as f:
    l = f.readlines()
input_strings = []
for line in l:
    input_strings.append(line[:-1])
#print(input_strings)
list_positions = [[],[],[],[],[],[],[],[]]

for string in input_strings:
    for i in range(0,8):
        list_positions[i].append(string[i])
for position in list_positions:
    #c = Counter(position)
    print(min(position,key = position.count))
#print(list_positions)
