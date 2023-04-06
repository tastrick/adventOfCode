with open('input.txt') as f:
    l = f.readlines()
#print(l)
for line in l:
    start = line[:-1]
        
#print(start)
#convert to binary
hex_bin = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
bin_hex = {v:k for k,v in hex_bin.items()}
new = ''
for c in start:
    new+=hex_bin[c]
    
#print(new)
operators = []
literals = []
versions_dec = []
ids = []
s= [char for char in new]
#outer_most = s[0:6]
#del s[0:6]
#print(outer_most)
i=0
while (s!=[]):
    #print(i)
    v_bin = s[i:i+3]
    v_dec = ''
    for x in v_bin:
        v_dec +=x
    v_dec = int(v_dec,2)
    id_bin = s[i+3:i+6]
    id_dec = ''
    for x in id_bin:
        id_dec+=x
    id_dec = int(id_dec,2)
    
    versions_dec.append(v_dec)
    ids.append(id_bin)
    #print(v_dec)
    del s[i:i+6]
    if (id_dec==4):
        if (s[i]=='0'):
            #only one packet of info
            paket = s[i+1:i+6]
            literals.append(paket)
            del s[i+1:i+6]
        else:
            leading = '1'
            while(leading!='0'):
                paket = s[i+1:i+6]
                literals.append(paket)
                del s[i+1:i+6]
                leading = s[0]
            paket = s[i+1:i+6]
            literals.append(paket)
            del s[i+1:i+6]
            #more than one packet of info
    else:
        #print(s)
        if(s[i]=='0'):
            #next 15 bits are total length of subpacks
            sub_num_bin = s[i+1:i+16]
            sub_dec=''
            for x in sub_num_bin:
                sub_dec+=x
            sub_dec = int(sub_dec,2)
            del s[i:i+16]
            paket = s[i:i+sub_dec]
            operators.append(paket)
            del s[i:i+sub_dec]
        else:
            sub_num_bin = s[i+1:i+12]
            sub_dec = ''
            for x in sub_num_bin:
                sub_dec+=x
            sub_dec = int(sub_dec,2)
            del s[i:i+12]
            paket = s[i:i+sub_dec]
            operators.append(paket)
            del s[i:i+sub_dec]
            #next 11 bits are total number of sub-packs
        
    curr = s[i]
    print(isinstance(curr,str))
    while(curr == '0' and s!=[] ):
        print('r')
        del s[i]
        if (s!=[]):
            curr = s[i]
    print(s)        
print(sum(versions_dec))    

