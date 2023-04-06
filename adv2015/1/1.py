with open('input.txt') as f:
    new = f.readlines()
    
print(new)
s = []
for i in new:
    for char in i:
        s.append(char)
        
print(s)
s.remove('\n')
dict_dir = {'(':1,')':-1}
start = 0
count = 1
for x in s:
    start+=dict_dir[x]
    if (start == -1):
        print('position: ',count)
        break
    count+=1
print(start)
