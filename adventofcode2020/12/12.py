import math
global position, waypoint
global curr_line
global zero_dem
f = open("input12.txt", "r")
direction=[]
nums=[]
turn=['L','R']
move = ['N','S','E','W','F']
temp = [0,1,2,3]
name={0:'N',1:'E',2:'S',3:'W'}
zero_dem=0
#curr line represents the line that passes through the waypoint and the ship, the number at index 0 is the slope and the number at index 1 is the y-intercept
curr_line=[0.0,0.0]
#cards = cycle(temp)
#position will contain 3 ints the first represents x-position, second y-position and third is an int between 0 and 3 representing the cardinal directions N,E,S,W respectively

#always faces east to start
position=[0,0]
waypoint=[10,1]
for line in f:
    line=line[:-1]
    direction.append(line[0])
    nums.append(int(line[1:]))
    
#print(direction)
#print(nums)

def moveit(direct, x):
    global waypoint, position, curr_line
    if (direct in turn):
        temp1=int(x/90)
        if (direct=='L'):
            y=4-temp1
        else:
            y=temp1
        n=0
        while(n<y):
            new_position = get_newpos()
            print("new_pos: ", new_position)
            if (new_position[0]<0):
                waypoint[0] = int (new_position[0]-0.5)
            else:
                waypoint[0] = int (new_position[0]+0.5)
            if (new_position[1]<0):
                waypoint[1] = int (new_position[1]-0.5)
            else:
                waypoint[1] = int (new_position[1]+0.5)
            #waypoint[1] = int(new_position[1]+0.5)
            #get_line()
            #print(waypoint[0], waypoint[1])
            n+=1
        #start = position[2]ne
        #new = start+y
        #if (new>len(temp)-1):
        #    new = new-4
        #print(new)
        #position[2]=new
    elif(direct in move):
        if (direct=='N'):
            waypoint[1]= waypoint[1]+x
        elif(direct=='S'):
            waypoint[1]= waypoint[1]-x
        elif(direct=='E'):
            waypoint[0]=waypoint[0]+x
        elif(direct=='W'):
            waypoint[0]=waypoint[0]-x
        elif(direct=='F'):
            diff1=abs(position[0]-waypoint[0])
            diff2=abs(position[1]-waypoint[1])
            #print(diff1, diff2)
            quad=get_quad()
            if (quad==3):
                position[0]=position[0]-x*diff1
                position[1] =position[1]- x*diff2
                waypoint[0] = position[0]-diff1
                waypoint[1] = position[1]-diff2
            elif(quad==2):
                position[0]=position[0]+x*diff1
                position[1] =position[1]- x*diff2
                waypoint[0] = position[0]+diff1
                waypoint[1] = position[1]-diff2
            elif(quad==1):
                position[0]=position[0]+x*diff1
                position[1] =position[1]+ x*diff2
                waypoint[0] = position[0]+diff1
                waypoint[1] = position[1]+diff2
            elif(quad==4):
                position[0]=position[0]-x*diff1
                position[1] =position[1]+ x*diff2
                waypoint[0] = position[0]-diff1
                waypoint[1] = position[1]+diff2
            elif(quad==0):
                if (position[0]==waypoint[0]):
                    if (position[1]>waypoint[1]):
                        position[1]=position[1]-x*diff2
                        waypoint[1]=position[1]-diff2
                    else:
                        position[1] = position[1]+x*diff2
                        waypoint[1] = position[1]+diff2
                elif(position[1]==waypoint[1]):
                    if (position[0]>waypoint[0]):
                        position[0] = position[0] - x*diff1
                        waypoint[0]= position[0] - diff1
                    else:
                        position[0] = position[0] + x*diff1
                        waypoint[0] = position[0] + diff1
def get_quad():
    global waypoint, position, curr_line
    quad=0
    if (position[0]>waypoint[0] and position[1]>waypoint[1]):
        quad=3
    elif(position[0]<waypoint[0] and position[1]>waypoint[1]):
        quad=2
    elif(position[0]<waypoint[0] and position[1]<waypoint[1]):
        quad=1
    elif(position[0]>waypoint[0] and position[1]<waypoint[1]):
        quad=4
    return quad        
            
def distance():
    global waypoint, position, curr_line
    side1=abs(position[0]-waypoint[0])
    side2 = abs(position[1]-waypoint[1])
    return math.sqrt(side1**2+side2**2)
    
def get_perp():
    global waypoint, position, curr_line
    new_line=[0.0,0.0]
    perp_slope = -(1.0/curr_line[0])
    new_line[0]=perp_slope
    new_int=position[1]-perp_slope*position[0]
    new_line[1]=new_int
    return new_line
#returns the point 90 degrees from current waypoint location            
def get_newpos():
    global waypoint, position, curr_line
    new_list=[0.0,0.0]
    dist1=distance()
    quad=get_quad()
    print("QUAD: ", quad)
    #print(dist1)
    #if position of waypoint does not have any of the same coordinates as the ship
    if (quad !=0):
        get_line()
        perp=get_perp()
        #print((dist1**2)/(1+(int(perp[0]))**2))
        if (quad==1or quad==4):
            new_list[0]=position[0]+math.sqrt((dist1**2)/(1+perp[0]**2))
            new_list[1] = perp[0]*new_list[0]+perp[1]
        elif(quad==2 or quad==3):
            new_list[0]=position[0]-math.sqrt((dist1**2)/(1+perp[0]**2))
            new_list[1] = perp[0]*new_list[0]+perp[1]
    #if there is at least one of the coordinates that is the same
    else:
        if (position[1]==waypoint[1] and position[0]>waypoint[0]):
            new_list[0] = position[0]
            new_list[1] = position[1]+dist1
        elif(position[1]==waypoint[1] and position[0]<waypoint[0]):
            new_list[0] = position[0]
            new_list[1] = position[1]-dist1
        elif(position[0]==waypoint[0] and position[1]> waypoint[1]):
            new_list[0]=position[0]-dist1
            new_list[1]=position[1]
        elif(position[0]==waypoint[0] and position[1]< waypoint[1]):
            new_list[0]=position[0]+dist1
            new_list[1]=position[1]
            
    #print("THE LIST:", new_list)
    return new_list 

    
def get_line():
    global waypoint, position, curr_line
    #print(position[0], waypoint[0])
    m=(position[1]-waypoint[1])/(position[0]-waypoint[0])
    intercept = position[1]-m*position[0]
    curr_line[0]=m
    curr_line[1]=intercept

n=0
while(n < len(nums)):
    print(nums[n], direction[n])
    print(waypoint, position)
    moveit(direction[n], nums[n])
    
    n+=1
   


print(waypoint, position)
