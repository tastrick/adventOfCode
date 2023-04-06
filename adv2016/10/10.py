with open('input.txt') as f:
    l = f.readlines()

bot_instructions = {}
bot_contents = {}
outputs = {}
inputs = {}

def run_bot_inst(number):
    ls = [number]
    while(ls != []):
        num = ls.pop(0)
        lower = min(bot_contents[num])
        high = max(bot_contents[num])
        if (lower ==17 and high == 61):
            print('comparison: ', lower,high,'     bot: ',num)
        #print(bot_contents[num])
        if (len(bot_contents[num])==2):
            if ( num in list(bot_instructions.keys())):
                if (bot_instructions[num][0]=='output'):
                    if (bot_instructions[num][1] in list(outputs.keys())):
                        outputs[bot_instructions[num][1]].append(lower)
                    else:
                        outputs[bot_instructions[num][1]] = [lower]
                else:
                    if (bot_instructions[num][1] in list(bot_contents.keys())):
                        bot_contents[bot_instructions[num][1]].append(lower)
                        ls.append(bot_instructions[num][1])
                    else:
                        bot_contents[bot_instructions[num][1]] =[lower]
            
                if (bot_instructions[num][2]=='output'):
                    if (bot_instructions[num][3] in list(outputs.keys())):
                        outputs[bot_instructions[num][3]].append(high)
                    else:
                        outputs[bot_instructions[num][3]] = [high]
                else:
                    if (bot_instructions[num][3] in list(bot_contents.keys())):
                        bot_contents[bot_instructions[num][3]].append(high)
                        ls.append(bot_instructions[num][3])
                    else:
                        bot_contents[bot_instructions[num][3]] = [high]
                del bot_contents[num]
                del bot_instructions[num]
for line in l:
    split = line[:-1].split(' ')
    if (split[0]=='bot'):
         bot_instructions[int(split[1])] = (split[5],int(split[6]),split[10],int(split[11]))
for line in l:
    split = line[:-1].split(' ')
    if (split[0]=='bot'):
        pass
    else:
        bot = int(split[len(split)-1]) 
        if (bot in list(bot_contents.keys())):
            bot_contents[bot].append(int(split[1]))
            run_bot_inst(bot)
        else:
            bot_contents[bot] = [int(split[1])]
            
#print(bot_contents)
#print(bot_instructions)
print(outputs[0][0]*outputs[1][0]*outputs[2][0])
