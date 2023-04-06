f = open("input14.txt", "r")
#mem is an array of all memory locations accessed 
ans = []
mask=[]
info=[]
mem=[]
nums = []
done_mems={}
for line in f:
    line=line[:-1]
    info.append(line)
f.close()
#print(info)
n=0
for item in info:
    x=item.split(" = ")
    if (x[0]=='mask'):
        mask.append(x[1])
        mem.append("x")
        nums.append("x")
    else:
        y=x[0].split("[")
        z=y[1].split("]")
        mem.append(int(z[0]))
        nums.append(int(x[1]))
    n+=1
mem.append("x")
nums.append("x")
def get_shifted_num(m, n):
    bin_num = bin(n)
    temp1 = str(bin(n))
    #print(temp1)
    temp = temp1[2:]
    #print(temp)
    string_num = temp
    i = len(string_num)
    j = len (m)
    new_num = j-i
    #print(new_num)
    #adds 0s to start of our num
    if (new_num != 0):
        string_num = ("0"*new_num)+string_num
    #print(string_num)
    #print(m)
    mask_list = list(m)
    new_num_list = list(string_num)
    count=0
    for l in mask_list:
        if (l != 'X'):
            if (l != new_num_list[count]):
                new_num_list[count] = l
        count+=1
    ret = ""
    for num in new_num_list:
        ret = ret+num
    ret = "0b"+ret
    #print(int(ret, 2))
    return (int(ret, 2))    
print(len(mask))
mask_i = 0
n=0
while(mask_i<len(mask)):
    mask_curr = mask[mask_i]
    num = nums[n+1]
    item = mem[n+1]
    while (item != "x"):
        after_shift = get_shifted_num(mask_curr,num)
        done_mems[item]=after_shift
        print(done_mems)
        n+=1
        item = mem[n+1]
        num = nums[n+1]
    print(mask_i, n)
    mask_i+=1
    n+=1

print(done_mems)
print(mask_i)
print(sum(done_mems.values()))
#the following function will take m and n as inputs where m is the mask and n is the number
