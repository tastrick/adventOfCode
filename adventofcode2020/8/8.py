global a, p
global visited
a=0
p=0
f = open("input8.txt", "r")
inst = []
part1 = []
part2 = []
acc = 'acc'
jmp = 'jmp'
nop = 'nop'
for line in f:
    inst.append(line)
f.close()

n=0
while(n < len(inst)):
    inst[n]=(inst[n])[:-1]
    n+=1
    
n=0
while(n < len(inst)):
    x=inst[n].split(" ")
    part1.append(x[0])
    part2.append(x[1])
    #print(int(x[1]))
    n+=1
#pointer to instruction will be just an integer that represents the index of the inst
def action (s, num):
    global a, p
    print(s,num, p, a)
    if (s==acc):
        a+=num
    elif(s==jmp):
        p+=num
    else:
        pass
    
#this function will take as input a list of instructions (given by index), roll back execution to find a change that will allow p to not be an issue 
#p_value is the value of p that gets repeated, so we want to ensure our change makes it so that p is not repeated we will continue execution until p doesnt hit that one
def roll_back(p_list, p_value, a_list):
    global a, p
    global visited
    steps = len(p_list)
    count=0
    while(p in visited):
        n=0
        #place_change=p_list[count]
        p = p_list[0]
        a = a_list[0]
        while(n<steps):
            if (p not in visited):
                break
            if (n==count):
                mem=p
                if (part1[p]==jmp):
                    action(nop, int(part2[p]))
                elif(part1[p]==nop):
                    action(jmp,int(part2[p]))
                else:
                    action(part1[p], int(part2[p]))
                if (p==mem):
                    p+=1
            else:
                mem=p
                #print(p)
                action(part1[p], int(part2[p]))
                if (p==mem):
                    p+=1
            
            n+=1
        print("exiting:",p, count, a)
        count+=1
    
n=0
visited=[]
accumulator = []
stuck=[]
mem=p
mem_a=a
while (p < len(inst)):
    
   
    if (p not in visited):
        print("here again")
        visited.append(p)
        accumulator.append(a)
        mem=p
        mem_a=a
        action(part1[p], int(part2[p]))
        if (p==mem):
            p+=1
        
    else:
        n+=1
        index_start = visited.index(p)
        print(index_start)
        p_list1 = visited[index_start:]
        a_list1 = accumulator[index_start:]
        print(p_list1, a_list1)
        #break
        #print(new_list)
        #print(visited)
        #print(mem,mem_a)
        roll_back(p_list1, p, a_list1)
        print(p,a, visited)
        #for index in new_list:
        #    print(part1[index])
        #break
        #p=mem
        #a=mem_a
        #print("********")
        #action(nop, int(part2[mem]))
        #p+=1
    #n+=1

print(a)



