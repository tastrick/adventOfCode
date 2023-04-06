import time
from string import ascii_lowercase as lett
with open('input.txt') as f:
    l = f.readlines()

all_data = []
for line in l:
    split = line[:-1].split('-')
    all_data.append(split)

valid_list = []
for room in all_data:
    sec = int(room[-1].split('[')[0])
    checksum = room[-1].split('[')[1][:-1]
    
    #room.pop()
    room_all_chars = []
    for string in room[:-1]:
        for char in string:
            room_all_chars.append(char)
        room_stats = []
        for char in room_all_chars:
            curr = [room_all_chars.count(char),char]
            if (curr not in room_stats):
                room_stats.append(curr)
    ordered = sorted(room_stats,key = lambda x:x[0],reverse = True)
    ties = []#list of ranges of the list that have the same number
    #print('before sub orderes: ', ordered)
    all_ranges = []
    i=0
    flag = True
    while(i<len(ordered)):
        #print(i)
        range_ = []
        if (i<len(ordered)-1 and ordered[i+1][0]==ordered[i][0]):
            range_.append(i)
            num = ordered[i][0]
            #print(ordered[i+1:])
            #time.sleep(2)
            cnt = i+1
            for y in ordered[i+1:]:
                #print('True')
                if (ordered[cnt][0]!=num):
                    range_.append(cnt-1)
                    break
                cnt+=1
            if(len(range_)==1):
                range_.append(cnt-1)
            i = cnt
            #print(cnt)
            #time.sleep(2)
            all_ranges.append(range_)
        else:
            i+=1
    print(all_ranges)
    for range1 in all_ranges:
        #print(ordered[range1[0]:range1[1]])
        ordered[range1[0]:range1[1]+1] = sorted(ordered[range1[0]:range1[1]+1], key = lambda x:x[1],reverse = False)
    print('after sub orderes: ',ordered)
    #time.sleep(2)     
    top_five = ordered[0:5]
    valid = True
    for char in checksum:
        if (char not in [x[1] for x in top_five]):
            valid = False
    if (valid):
        valid_list.append(room)
#print(sum(valid_list))

def rotate(string):
    return_string = ''
    for letter in string:
        if (letter in lett):
            return_string+=lett[(lett.index(letter)+1)%len(lett)]
        else:
            return_string+=letter
    return return_string
all_strings_decoded = []
for valid_room in valid_list:
    sec = int(valid_room[-1].split('[')[0])
    cnt = 0
    while(cnt<sec):
        for i,string in enumerate(valid_room[:-1]):
            #print('before: ', valid_room[i])
            valid_room[i] = rotate(string)
            #print('after: ',valid_room[i])
            #time.sleep(2)
        cnt+=1
    #print(valid_room[:-1])
    #time.sleep(2)
    if('storage' in valid_room[:-1]):
        print('got it')
        print(valid_room, sec)
    all_strings_decoded.append([valid_room[:-1],sec])
#print(all_strings_decoded)
            
    
                
    
