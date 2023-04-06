row = 2981
#row = 2
col = 3075
#col = 4
start = 20151125
mult_fact = 252533
div = 33554393

gap_row = 2982
s = 1
inc = 1
for x in range(1,row):
    s+=inc
    inc+=1

inc+=1
for x in range(1,col):
    s+=inc
    inc+=1
print(s)

past = start
loop_start = 1
while(loop_start<=s):
    past = (past*mult_fact)%div
    loop_start+=1
print(past)
'''
for x in range(1,s):
    past = (past*mult_fact)%div
print(past)
'''
#print(s*(mult_fact)%(s*div))
