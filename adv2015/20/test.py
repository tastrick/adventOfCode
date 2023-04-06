def get_pres_num(n):
    l = []
    b = []
    
    
    
    for x in range(1,n+1):
        if ((n/x).is_integer()):
            l.append(11*x)
            b.append(x)
            
    for elf in b:
        houses = [h for h in range(elf,50*elf,elf)]
                                   
        if (n not in houses):
            ind = l.index(11*elf)
            l.pop(ind)
    
        
            
    #print(l,n)
    #time.sleep(1)
    return sum(l),l

#num = 831600
#num = 900480

num = 831600
print(get_pres_num(num))

#831720

#8331612
