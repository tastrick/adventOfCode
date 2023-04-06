with open('input.txt') as f :
    l = f.readlines()

lines =[]
for line in l:
    new_line = []
    for char in line[:-1]:
        new_line.append(char)
    lines.append(new_line)
    
    
#points = {')':3,']':57,'}':1197,'>':25137}
points = {')':1,']':2,'}':3,'>':4}
pairs = {'(':')','[':']','{':'}','<':'>'}

illegal = {')':0,']':0,'}':0,'>':0,'(':0,'[':0,'{':0,'<':0}
closed = [')',']','>','}']

ans = []

copy = []
for x in lines:
    n = []
    for l in x:
        n.append(l)
    copy.append(n)
scores = []
for line in lines:
    list_of_open = []
    break_flag = False
    for char in line:
        if (char in closed and char != pairs[list_of_open[len(list_of_open)-1]]):
            ans.append(points[char])
            break_flag = True
            break
        elif (char in closed and char == pairs[list_of_open[len(list_of_open)-1]]):
            list_of_open.pop()
        else:    
            list_of_open.append(char)
    if (break_flag == False):
        remainder = [pairs[x] for x in reversed(list_of_open)]
        tot = 0
        for r in remainder:
            tot*=5
            tot+=points[r]
        scores.append(tot)
    
s = sorted(scores)
index = int(len(s)/2)
print(s[index])
            
            
    
