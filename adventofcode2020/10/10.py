f = open("input10.txt", "r")
nums = []
diff=[]
for line in f:
    line = line[:-1]
    nums.append(int(line))
f.close()
print(nums)
nums.sort()
nums.append(nums[len(nums)-1]+3)
curr_out=0
print(nums)
i=0
while(i <len(nums)):
    if (nums[i]-curr_out<=3):
       diff.append(nums[i]-curr_out)
       curr_out=nums[i]
       i+=1
    else:
        print("didnt make it")
        break
   
print(diff)

ones = diff.count(1)
threes = diff.count(3)

print(ones*threes)
ans=1
i=0
curr_left=0
count=0
right=1
while (i < len(diff)):
    if (diff[i]==1):
        count+=1
    elif(diff[i]==3):
        if(count>=4):
            #7 is the result from adding all possibilities--> one out of three is in, two out of three is in and all three are in (3 choose 2) + (3 choose 1) +1 = 7
            ans=ans*7
        elif(count==3):
            ans=ans*4
        elif(count==2):
            ans=ans*2
        count=0
    i+=1
print(ans)
