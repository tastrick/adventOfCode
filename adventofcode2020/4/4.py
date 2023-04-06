f = open("input4.txt", "r")
pass_list = []
break_list=[]
ans = 0
cred_list = ['byr','iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

dict_cred = {}

byr = [1920, 2002]
iyr = [2010, 2020]
eyr = [2020, 2030]
hgt = ['cm', 150, 193, 'in', 59, 76]
hcl = [0,9,'a', 'f']
ecl_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
pid = [9]

dict_cred['byr']= byr
dict_cred['iyr'] = iyr
dict_cred['eyr'] = eyr
dict_cred['hgt'] = hgt
dict_cred['hcl'] = hcl
dict_cred['ecl'] = ecl_list
dict_cred['pid'] = pid

newline = '\n'
for line in f:
    pass_list.append(line)

f.close()
#print(pass_list)
n=0
for item in pass_list:
    if (item==newline):
       break_list.append(n)
    n+=1
break_list.append(len(pass_list)-1)
#print(break_list)
def deep_copy(somelist):
    newlist = []
    for x in somelist:
       newlist.append(x)
    return newlist
i=0
counter=0

def is_valid(cred, value):
    #print(cred, value)
    if (cred == 'cid'):
        return True
    elif (cred== 'byr' or cred == 'iyr' or cred == 'eyr'):
        if (len(value)==4):
            if (int(value)>= (dict_cred[cred])[0] and int(value)<=(dict_cred[cred])[1]):
                return True
            else:
                return False
        else:
            return False
    elif (cred=='hgt'):
        if (value.find(hgt[0])!=-1):
            new = value.split(hgt[0])
            #print(new[0])
            if (int(new[0])>= hgt[1] and int(new[0])<= hgt[2]):
                return True
            else:
                return False
        elif(value.find(hgt[3])!=-1):
            new = value.split(hgt[3])
            #print(new[0])
            if (int(new[0])>= hgt[4] and int(new[0])<= hgt[5]):
                return True
            else:
                return False
        else:
            return False
    elif (cred == 'ecl'):
        for x in ecl_list:
            if (value==x):
                return True
        return False
        
    elif(cred == 'pid'):
        if (len(value)==9):
            return True
        else:
            return False
    elif(cred == 'hcl'):
        if (value.find('#')!= -1):
            new = value.split("#")
            #print(new[1])
            if (len(new[1])==6):
                for x in new[1]:
                    if ((x<'0' and x>'9') or (x<'a' and x>'f')):
                        #print(x<'0', x> '9', x< 'a', #x>'f')
                        #print(x)
                        return False
                    else:
                        #print("no luck chuck")
                        return True
            else:
                #print("too long or too short")
                return False
        else:
            #print("no hashtag lol")
            return False
#print(pass_list)
while (i < len(break_list)):
    this_creds=deep_copy(cred_list)
    #print(this_creds)
    while (counter<=break_list[i]):
        #check for spaces in line, indicated more than one credential on this line
        if(pass_list[counter].find(" ")!= -1):
            y=pass_list[counter].split(" ")
            for line in y:
                z = line.split(":")
                if (z[1].find(newline)!= -1):
                    #print(z[1])
                    z[1]=(z[1])[:-1]
                if (is_valid(z[0],z[1])):
                    this_creds.remove(z[0])
        elif (pass_list[counter]!=newline):
            x = pass_list[counter].split(":")
            #print(x[1])
            if (x[1].find(newline)!=-1):
                #print('There is a new line')
                x[1]=(x[1])[:-1]
                #print(x[1])
            if (is_valid(x[0], x[1])):
                this_creds.remove(x[0])
        counter+=1
   # print(this_creds)
    if (this_creds==[] or this_creds==['cid']):
        ans+=1
    i+=1

print(ans)
