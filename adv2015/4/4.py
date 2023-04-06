import hashlib

ins = 'ckczppom'
leading_flag = False
start = 0
def is_leading_0(ha):
    zer = 0
    for char in ha:
        if (char == '0'):
            zer+=1
        elif (char != '0'):
            break
    if (zer == 6):
        return True
    else:
        return False
while (leading_flag == False):
    to_be_hashed = ins+str(start)
    h = hashlib.md5(to_be_hashed.encode()).hexdigest()
    start+=1
    leading_flag = is_leading_0(h)

print(start)
