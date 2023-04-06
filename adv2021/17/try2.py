#inp = '620080001611562C8802118E34'
with open('input.txt') as f:
    l = f.readlines()
print(l)
for line in l:
    inp = line[:-1]
hex_bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
bin_hex = {v:k for k,v in hex_bin.items()}

inp_bin = ''
for x in inp:
    inp_bin+=hex_bin[x]
versions = []
ids = []
packets={'literals': [],'operators':[]}
#print(inp_bin)
bin_str = []
for x in inp_bin:
    bin_str.append(x)
#print(bin_str)

def list_to_sum(l):
    bin_stru = ''
    for string in l:
        bin_stru+=string
    return int(bin_stru,2)
ids.append('start')

def get_packet(s):
    #print('s: ',s)
    if (s==[] or s == ['0' for i in s]):
        pass
    else:
        if (len(ids)!=0 and ids[len(ids)-1] !='start'):
            ids.append('end')
        v_bin = s[0:3]
        v_dec = ''
        for x in v_bin:
            v_dec +=x
        version = int(v_dec,2)
        
        id_bin = s[3:6]
        id_dec = ''
        for x in id_bin:
            id_dec+=x
        #print(id_dec)
        type_id = int(id_dec,2)
        print(version,type_id)
        versions.append(version)
        ids.append(type_id)
        del s[0:6]
        if (type_id == 4):#literal packet 
            print('literal value')
            if (s[0]=='0'):
                print('ending literal first')
                #only one packet of info
                paket = s[1:5]
                print(paket)
                packets['literals'].append(paket)
                #print(paket)
                del s[0:5]
            else:
                leading = '1'
                while(leading!='0'):
                    paket = s[1:5]
                    packets['literals'].append(paket)
                    del s[0:5]
                    leading = s[0]
                print('ending literal after')
                paket = s[1:5]
                print(paket)
                packets['literals'].append(paket)
                del s[0:5]
            #ids.append('start')
            get_packet(s)
        else:
            print('operator','length type id: ', s[0])
            if(s[0]=='0'):
                #next 15 bits are total length of subpacks
                sub_num_bin = s[1:16]
                sub_dec=''
                for x in sub_num_bin:
                    sub_dec+=x
                length_in_bits = int(sub_dec,2)
                del s[0:16]
                paket = s[0:length_in_bits]
                packets['operators'].append(paket)
                #ids.append(str(list_to_sum(paket))+' bits')
                ids.append('start')
                get_packet(s)
                #ids.append('end')
                #del s[0:length_in_bits]
            else:
                sub_num_bin = s[1:12]
                sub_dec = ''
                for x in sub_num_bin:
                    sub_dec+=x
                num_of_packets = int(sub_dec,2)
                del s[0:12]
                #ids.append(str(num_of_packets)+' sub-packets')
                ids.append('start')
                get_packet(s)
                #ids.append('end')
                #next 11 bits are total number of sub-packs
        '''    
        if (s!=[]):
            curr = s[0]
            print(isinstance(curr,str))
            while(curr == '0' and s!=[] ):
                print('r')
                del s[0]
                if (s!=[]):
                    curr = s[0]
        '''   

get_packet(bin_str)        
#print(sum(versions))
print(ids)
#print(packets)
curr_inside = []
curr = []


    
'''
while(ids!= []):
    i= ids.pop()
    if (isinstance(i,int)):
        if (i==4):
            curr_inside.append(list_to_sum(packets['literals'].pop()))
        elif (i == 0):
            temp = copy.deepcopy(curr_inside)
            curr_inside = []
            curr_inside.append(sum([i for i in temp]))
        elif(i==1):
            temp = copy.deepcopy(curr_inside)
            curr_inside = []
            prod = 1
            for x in temp:
                prod*=x
            curr_inside.append(prod)
        elif(i==2):
            mini = curr_inside.pop()
            for x in curr_inside:
                if (x<mini):
                    mini = x
            curr_inside = [mini]
        elif(i==3):
            mini = curr_inside.pop()
            for x in curr_inside:
                if (x>mini):
                    mini = x
            curr_inside = [mini]
        elif(i==6):
            pass
        elif(i==5):
            pass
        elif(i==7):
            pass
    else:
        split = i.split(' ')
        if (split[1][0]=='s'):
            pass
            #subpackets
        else:
            #individual
            pass
'''
