import itertools
from scipy.optimize import fsolve
from scipy.optimize import minimize
#from scipy.optimize import maximize
from numpy.random import rand
import math
from in_gr import ingredient
with open('input.txt') as f:
    l = f.readlines()

print(l)
ingr_dict = {}
#list_of_ings = []
for line in l:
    split = line[:-1].split(' ')
    #list_of_ings.append(ingredient(split[0][:-1],int(split[2][:-1]),int(split[4][:-1]),int(split[6][:-1]),int(split[8][:-1]), int(split[10])))
    ingr_dict[split[0][:-1]] = [int(split[2][:-1]),int(split[4][:-1]),int(split[6][:-1]),int(split[8][:-1]), int(split[10])]

print(ingr_dict)

'''    
def subset_sum(numbers, target,length, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print ("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n]) 
   
set_of_nums = [i for i in range(0,100)]

subset_sum(set_of_nums,100,2)
'''

def get_A():
    
    keys =list(ingr_dict.keys())
    cont = ingr_dict[keys[0]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[0]][3]
    return cont

def get_B():
    keys =list(ingr_dict.keys())
    cont = ingr_dict[keys[0]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[0]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[0]][3]+ingr_dict[keys[0]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[0]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[0]][3]
    return cont

def get_C():
    keys =list(ingr_dict.keys())
    cont = ingr_dict[keys[0]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[0]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[0]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[0]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[0]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[0]][3]
    return cont

def get_D():
    keys =list(ingr_dict.keys())
    cont = ingr_dict[keys[1]][0]*ingr_dict[keys[0]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[0]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[0]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[1]][3]+ingr_dict[keys[1]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[0]][3]
    return cont

def get_E():
    keys =list(ingr_dict.keys())
    cont = ingr_dict[keys[1]][0]*ingr_dict[keys[1]][1]*ingr_dict[keys[1]][2]*ingr_dict[keys[1]][3]
    return cont

def equations(p):

    A = get_A()
    B = get_B()
    C = get_C()
    D = get_D()
    E = get_E()
    x,y = p
    print(A,B,C,D,E)
    return ((4*A-B)*x**3+(3*B+2*C)*y*x**2+(2*C-3*D)*x*(y**2)+(D-4*E)*y**3,x+y)

    
def cookie_score(p):
    l = []
    #for i,key in enumerate(list(ingr_dict.keys())):
    #    l.append()
    keys = list(ingr_dict.keys())
    a = p[0]*ingr_dict[keys[0]][0]+p[1]*ingr_dict[keys[1]][0]+p[2]*ingr_dict[keys[2]][0]+p[3]*ingr_dict[keys[3]][0]
    b = p[0]*ingr_dict[keys[0]][1]+p[1]*ingr_dict[keys[1]][1]+p[2]*ingr_dict[keys[2]][1]+p[3]*ingr_dict[keys[3]][1]
    c = p[0]*ingr_dict[keys[0]][2]+p[1]*ingr_dict[keys[1]][2]+p[2]*ingr_dict[keys[2]][2]+p[3]*ingr_dict[keys[3]][2]
    d = p[0]*ingr_dict[keys[0]][3]+p[1]*ingr_dict[keys[1]][3]+p[2]*ingr_dict[keys[2]][3]+p[3]*ingr_dict[keys[3]][3]
    l = [a,b,c,d]
    for i,x in enumerate(l):
        if (x <0):
            l[i] = 0
    return l[0]*l[1]*l[2]*l[3]
 
# objective function
def objective(x):
    A = get_A()
    B = get_B()
    C = get_C()
    D = get_D()
    E = get_E()
    print(A,B,C,D,E)
    return A*x[0]**4+B*x[1]*x[0]**2+C*(x[0]**2)*(x[1]**2)+D*x[0]*(x[1]**3)+4*x[1]**3

list_hun = [i for i in range(0,101)]
#print(list_hun)
all_poss_length = list(itertools.combinations(list_hun,4))
print('got all by length')
#print(len(all_poss_length))
#print(list(all_poss_length))
sum_to_hund = []
for poss in list(all_poss_length):
    if (sum (poss)==100):
        sum_to_hund.append(poss)
calorie_counted = []
for pin in sum_to_hund:
    ps = list(itertools.permutations(pin,len(pin)))
    bflag = False
    for s in ps:
        
        ke = list(ingr_dict.keys())
        calors = s[0]*(ingr_dict[ke[0]][4])+s[1]*(ingr_dict[ke[1]][4])+s[2]*(ingr_dict[ke[2]][4])+s[3]*(ingr_dict[ke[3]][4])
        if (calors == 500):
            if(pin not in calorie_counted):
                calorie_counted.append(s)
            break
        #if (bflag)   
print(len(calorie_counted))
print('got all that sum to 100')
scores = []
poss_ordered = []
for poss in calorie_counted:
    #perm_poss = list(itertools.permutations(poss,len(poss)))
    #for p in perm_poss:
    score = cookie_score(poss)
    scores.append(score)
    poss_ordered.append(poss)
    '''
    scor1 = cookie_score([poss[0],poss[1]])
    scores.append(scor1)
    poss_ordered.append([poss[0],poss[1]])
    scor2 = cookie_score([poss[1],poss[0]])
    scores.append(scor2)
    poss_ordered.append([poss[1],poss[0]])
    '''
    
index = scores.index(max(scores))
po = poss_ordered[index]
print(max(scores),po)
    
'''
# define range for input
r_min, r_max = 0.0, 100.0
# define the starting point as a random sample from the domain
pt = r_min + rand(2) * (r_max - r_min)
# perform the l-bfgs-b algorithm search
result = minimize(objective, pt, method='L-BFGS-B')
# summarize the result
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])
# evaluate solution
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))
'''
