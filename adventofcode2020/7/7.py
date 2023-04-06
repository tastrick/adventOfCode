f = open("input7.txt", "r")
raw_rules = []
rules_colour = {}
rules_number = {}
my_bag = 'shiny gold bags'
for line in f:
    raw_rules.append(line)

f.close()
#print(raw_rules)

n=0
while(n<len(raw_rules)):
    raw_rules[n] = (raw_rules[n])[:-1]
    n+=1
    
n=0
while(n<len(raw_rules)):
    raw_rules[n] = (raw_rules[n])[:-1]
    n+=1
    
#print(raw_rules)
n=0
while (n<len(raw_rules)):
    x=raw_rules[n].split(" contain")
    #x1 = x[0].split(" bags")
    y = x[1].split(",")#
    temp = []
    temp2=[]
    for line in y:
        temp.append (line[1])
        colour = line[3:]
        if('bag' in colour and 'bags' not in colour):
            colour=colour+'s'
        #print(colour)
        temp2.append(colour)
    rules_colour[x[0]]=temp2
    rules_number[x[0]]=temp
    n+=1
print(rules_colour)
print(rules_number)
def get_stops(some_list, counter, no_repeats):
    
    temp = []
    not_carried = []
    for string in some_list:
        for key in rules_colour:
            #print(string, temp)
            if (string in rules_colour[key] and key not in temp and key not in no_repeats):
                #print(temp)
                #print(string)
                temp.append(key)
                no_repeats.append(key)
        #if (len(temp)>0):
        #    not_carried.append(string)
      #  print(temp, not_carried)
    #print(len(not_carried))
    #print(temp, counter)
    if (len(temp)>0):
        counter+=len(temp)
        get_stops(temp, counter, no_repeats)
    else:
        #counter=len(temp)
        print(counter)
        return counter
  
#some_list has to contain the key, not value
def get_num_bags(key):
    num=0
    print(key)
    #print(number)
    print(rules_number[key])
    print(rules_colour[key])
    if (rules_number[key]==['n']):
        return 0
    else:
        n=0
        for numbers in rules_number[key]:
            print("n")
            colour = (rules_colour[key])[n]
            temp = get_num_bags(colour)
            print("num:", numbers)
            num = num +int(numbers)+int(temp)*int(numbers)
            print("updated num:", num, n)
            n+=1
        return num



first_stop=[]
no_repeats=[]
first_stop.append(my_bag)
get_stops(first_stop, 0, no_repeats)
print("Part 2:") 
some = []
get_num_bags(my_bag)

#input to this function is a string or colour of bag and a "height of the current node", returned value is the number of bags that can hold any combination of that bag


#raw_rules[0].remove("bags")
# = raw_rules[0].split("contain")
#print(x)
#y = x[1].split(",")

#for item in y:
#    print(item[0:2])
#    print (item[3:])
#print(y)
