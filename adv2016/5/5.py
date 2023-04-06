import time
import hashlib
input_str = 'ffykfhsq'
#input_str = 'abc'
#result = hashlib.md5(b'GeeksforGeeks')
#result = hashlib.md5(str2hash.encode())

password = ['','','','','','','','']
start = 0
while('' in password):
    hex_hash = 'fjdksalfd'
    while(hex_hash[0:5]!='00000'):
        #print(start)
        to_be_hashed = input_str+str(start)
        hashed = hashlib.md5(to_be_hashed.encode())
        hex_hash =hashed.hexdigest()
        start+=1
    #print('hex hash: ',hex_hash)
    #print('next char: ',hex_hash[5])
    #time.sleep(2)
    #password+=hex_hash[5]
    #print(int(hex_hash[5]))
    if (hex_hash[5].isalpha()==False):
        if (int(hex_hash[5])<=7 and password[int(hex_hash[5])]==''):
            #print(start)
            password[int(hex_hash[5])] = hex_hash[6]
print('final password: ', password)
