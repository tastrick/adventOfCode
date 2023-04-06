f = open("input9.txt", "r")
nums = []
last = []
continuous=[]
for line in f:
    temp = line[:-1]
    nums.append(int(temp))

f.close()
print(nums)
#n=0
#while(n<25):
#    last.append(nums[n])
#    n+=1

print(last)

i=25
while(i<len(nums)):
    next_num = nums[i]
    print("next number: ", next_num)
    j=i-25
    bound = j+25
    sum_flag=0
    while(j < bound):
        tmp = nums[j]
        counter = j+1
        while(counter<bound):
            if (tmp+nums[counter]==next_num):
                sum_flag=1
                print(tmp, nums[counter], next_num)
            counter+=1
        j+=1
    if(sum_flag==0):
        print(next_num)
        break
    i+=1
sum_flag=0
ans=[]
i=0
while(i<len(nums)):
    j=i+1
    cont = nums[i]
    ans.append(cont)
    while(j<len(nums)):
        cont+=nums[j]
        if (cont>next_num):
            ans=[]
            cont=0
            break
        elif(cont==next_num):
            ans.append(nums[j])
            sum_flag=1
            break
        else:
            ans.append(nums[j])
        j+=1
    if (sum_flag==1):
        break
    i+=1
print(ans)
print(sum(ans), i, j, next_num)
max1=max(ans)
#ans.remove(max(ans))
max2=min(ans)
print(max1+max2)
