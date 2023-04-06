with open('input.txt') as f:
    l = f.readlines()
    
items = []
for line in l:
    li = line[:-1]
    sp = li.split(",")
    nums1 = sp[0].split("-")
    nums2 =sp[1].split("-")
    
    n1 = int(nums1[0])
    n2 = int(nums1[1])
    n3 = int(nums2[0])
    n4 = int(nums2[1])
    
    items.append([n1,n2,n3,n4])
    
print(items)
c=0
bf = False
for ranges in items:
    l1 = [x for x in range(ranges[0],ranges[1]+1)]
    l2 = [y for y in range(ranges[2],ranges[3]+1)]
    for one in l1:
        for two in l2:
            if one == two:
                c+=1
                bf = True
                break
        if(bf):
            bf = False
            break
    
    

print(c)
