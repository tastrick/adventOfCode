f = open("input2.txt", "r")
list2 = []
for x in f:
    list2.append(x)
f.close()
#print(list2)
n=0
while (n < len(list2)):
    list2[n] = (list2[n])[:-1]
    n+=1

ans=0
lower = 0
upper = 0
prob= ''
stored_char = ''
prob_count = 0

for string in list2:
    x = string.split(":")
    y = x[0].split(" ")
    z = y[0].split("-")
    lower = int(z[0])
    upper = int(z[1])
    prob = y[1]
    n=0
    prob_count=0
    for character in x[1]:
        if (n==lower):
            if (character==prob):
                prob_count+=1
        elif(n==upper):
            if (character==prob):
                prob_count+=1
        n+=1
    if (prob_count == 1):
        ans+=1
        
print(ans)
