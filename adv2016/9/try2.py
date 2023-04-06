with open('input.txt') as f:
    l = f.readlines()
    
print(l)

def get_inside(st):
    if ('(' not in st):
        return len(st)
    i=0
    while('(' in st):
        i+=st.find('(')
        st = st[st.find('('):]
        string = st[1:st.find(')')]
        st = st[st.find(')')+1:]
        spl = string.split('x')
        i+=get_inside(st[:int(spl[0])])*int(spl[1])
        st = st[int(spl[0]):]
    i+=len(st)
    return i
print(get_inside(l[0][:-1]))    
