import time
lines = ['ax-end','xq-GF','end-xq','im-wg','ax-ie','start-ws','ie-ws','CV-start','ng-wg','ng-ie','GF-ng','ng-av','CV-end','ie-GF','CV-ie','im-xq','start-GF','GF-ws','wg-LY','CV-ws','im-CV','CV-wg']
#lines = ['start-A','start-b','A-c','A-b','b-d','A-end','b-end']
l = []
for li in lines:
    split = li.split('-')
    new = [split[0],split[1]]
    l.append(new)
    
#map1 = {}
#for x in l:
#    if (x[0] not in list(map1.keys())):
#        map1[x[0]] = [x[1]]
#    else:
#        map1[x[0]].append(x[1])

#print(map1)

def get_next(current, list_of_pairs):
    next1= []
    for x in list_of_pairs:
        if (current in x):
            next1.append(list(set(x)-set([current]))[0])
    return next1
all_paths = []
def find_path(curr_path, li, done_small):
    n = get_next(curr_path[len(curr_path)-1],li)
    for x in n:
        possible = [i for i in curr_path]
        possible.append(x)
        no_repeats = []
        for o in done_small:
            if (o not in no_repeats):
                no_repeats.append(o)
        num_small = [done_small.count(i) for i in no_repeats]
        if (x=='end'):
            all_paths.append(possible)
        elif(x=='start' or (2 in num_small and x in done_small)):
            continue
        else:
            print(num_small,done_small)
            if(x.islower()):
                done_small.append(x)

                
            curr_path.append(x)
            find_path(curr_path,li,done_small)
    
    c = curr_path.pop()
    if (done_small != [] and c == done_small[len(done_small)-1]):
        print('popped last small')
        done_small.pop()
    
find_path(['start'],l,[])
print(all_paths,len(all_paths))
