#ans = 741745043105674
f=open("input13.txt","r")
info=[]
buses=[]
wait = []
time_stamp=0
for line in f:
    line=line[:-1]
    info.append(line)

print(info)
time_stamp = int(info[0])
temp = info[1].split(",")
for x in temp:
    if (x=='x'):
        pass
    else:
        buses.append(int(x))
for bus in buses:
    wait.append(bus-time_stamp%bus)
    
#print(wait)
index = wait.index(min(wait))
print(buses[index]*wait[index])
#mins=[19,10, 8, 5, 4, 2, 12, 37]
mins=[]
n=1
while(n<len(buses)):
    index=temp.index(str(buses[n]))
    if (index<buses[n]):
        mins.append(index)
    else:
        mins.append(index%buses[n])
   #print(index)
    n+=1 
#mins.append(60)
print(mins)
#mins = [1,4,6,7]
#ans will cound up until it finds a num such that xmod(buses[0])=0, (x+1)mod(buses[1])=0...(x+len(buses)-1)mod(buses[len(buses)-1])=0
#ans=100000322837136
#ans=100000736300373
#ans=100001220604433
ans = 100001569706723
#ans=0
#print(mins)


#while(True):
#    mods=[]
#    i=1
#    j=0
#    while(i<len(buses)):
#        temp1 = buses[i]-(ans)%buses[i]
#        if(temp1!=mins[j]):
#            i=len(buses)
#        else:
#            mods.append(temp1)
#        i+=1
#        j+=1
#    print(mods, ans)
#    if (mods==mins):
#        print(ans)#
#        break
#    ans+=buses[0]
