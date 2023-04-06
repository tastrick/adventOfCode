f = open("input.txt", "r")
counter = 1
ans = 0
list1 = []
for x in f:
    list1.append(int(x))
f.close()
i = 0
while (i<len(list1)-2):
    temp = list1[i]
    counter = i+1
    while (counter < len(list1)-1):
        counter2 = counter+1
        while (counter2 < len(list1)):
            if (temp+list1[counter] +list1[counter2]==2020):
                ans = temp*list1[counter]*list1[counter2]
            else:
                pass
            counter2+=1
        counter+=1
    i+=1
print(ans)
        
