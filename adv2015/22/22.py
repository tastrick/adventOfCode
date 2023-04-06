import random
import itertools
import time

class player:
    def __init__(self,hp,d,a,mana):
        self.set_hp(hp)
        self.set_d(d)
        self.set_a(a)
        self.set_mana(mana)
        self.spent = 0
    def set_mana(self,m):
        self.mana = m
    def set_a(self,a):
        self.a = a
    def set_hp(self,hp):
        self.hp = hp
    def set_d(self,d):
        self.d = d
    def set_spent(self,how):
        self.spent=how
        
        
    
    
    def get_spent(self):
        return self.spent
    def get_mana(self):
        return self.mana
    def get_a(self):
        return self.a
    def get_hp(self):
        return self.hp
    def get_d(self):
        return self.d
    
class game:
    def __init__(self,boss_hp,boss_d,boss_a):
        self.boss = player(boss_hp,boss_d,boss_a,0)
        self.winner = None
        #self.store = {'w':{'dagger':[8,4,0],'shortsword':[10,5,0],'warhammer':[25,6,0],'longsword':[40,7,0],'greataxe':[74,8,0]},'a':{'leather':[13,0,1],'chainmail':[31,0,2],'splitmail':[53,0,3],'bandedmail':[75,0,4],'platemail':[102,0,5],'none':[0,0,0]},'r':{'none':[0,0,0],'damage +1':[25,1,0],'damage +2':[50,2,0],'damage +3':[100,3,0],'defense +1':[20,0,1],'defence +2':[40,0,2],'defence +3':[80,0,3]}}
        #spells give possibility for mana, damage,heals,effect,armor,healing,timer
        self.spells = {'magic missile':[53,4,0,0,0,0,0],'drain':[73,2,2,0,0,0,0],'sheild':[113,0,0,6,7,0,0],'poison':[173,3,0,6,0,0,0],'recharge': [229,0,0,5,0,101,0]}
        self.p1 = player(50,0,0,500)
    def cast_potion(self):
        random_potion = random.choice(list(self.spells.keys()))
        
        return random_potion
    def get_active(self):
        a = []
        for spell in list(self.spells.keys()):
            if (self.spells[spell][len(self.spells[spell])-1]!=0):
                a.append((spell,self.spells[spell][len(self.spells[spell])-1]))
                
        return a
    def update_spells_single(self,potion):
        effects = self.spells[potion]
        self.boss.set_hp(self.boss.get_hp()-effects[1])
        self.spells[potion][len(self.spells[potion])-1]-=1
        if ( potion =='sheild'):
            self.p1.set_a(self.p1.get_a()-effects[4])
        self.p1.set_mana(self.p1.get_mana()+self.spells[potion][5])
    def update_spells(self,p):
        
        for spell in list(self.spells.keys()):
            dont_sub = False
            if (self.spells[spell][len(self.spells[spell])-1]!=0):
                if (spell != p or p == 'sheild'):
                    #print(self.spells[spell][len(self.spells[spell])-1])
                    effects = self.spells[spell]
                    #self.p1.set_mana(self.p1.get_mana()+effects[0])
                    
                    
                    
                    if (spell == p and p == 'sheild'):
                        self.p1.set_a(self.p1.get_a()+effects[4])
                        #print('armor activated', )
                        dont_sub = True
                        #self.spells[spell][len(self.spells[spell])-1]-=1
                        #self.spells[spell][len(self.spells[spell])-1]+=1
                    
                    self.boss.set_hp(self.boss.get_hp()-effects[1])
                    if (dont_sub==False):
                        self.spells[spell][len(self.spells[spell])-1]-=1
                    if (self.spells[spell][len(self.spells[spell])-1]==0 and spell =='sheild'):
                        self.p1.set_a(self.p1.get_a()-effects[4])
                        #print('deactivated')
                    
                    #print(spell)
                    #print('before: ',self.p1.get_mana())
                    #if(self.spells[spell][5]!=0):
                        #print('adding mana for recharge')
                    self.p1.set_mana(self.p1.get_mana()+self.spells[spell][5])
                    #print('after: ', self.p1.get_mana())
                    #time.sleep(1)
                    #print('new', self.p1.get_mana())
                
    
    def check_price(self):
        flag = True
        for x in list(self.spells.keys()):
            if (abs(self.spells[x][0])<=self.p1.get_mana()):
                flag = False
                
        return flag
                
    def play(self,poss_list):
        curr_spells = []
        start = 1
        p1_start_po_flag = False
        state = []
        #list_of_potions = ['poison','magic missile','recharge','sheild','magic missile','poison','magic missile']
        while(self.p1.get_hp()>0 and self.boss.get_hp()>0):
            #print('stuck')
            if (poss_list != []):
                print('scores: ',self.p1.get_hp(),self.boss.get_hp(),curr_spells, self.p1.get_mana())
                print('armor',self.p1.get_a())
                print('turn: ',start)
                active = self.get_active()
                print('active spells: ',active)
                print('spent: ',self.p1.get_spent())
                print('--------------------------------')
                
                time.sleep(1)
            
            attempted_potion =[]
            has_gone_flag =False
            
            if (start%2==1):
                start = 2
                if (poss_list==[]):
                    potion = self.cast_potion()
                else:
                    potion = poss_list.pop(0)
                #attempted_potion.append(potion)
                #potion = list_of_potions.pop(0)
                self.p1.set_hp(self.p1.get_hp()-1)
                if (self.p1.get_hp()<=0):
                    pass
                #if (False):
                #    pass
                else:
                    cnt =1 
                    no_funds = False
                    #alue = 281
                    while( abs(self.spells[potion][0])>self.p1.get_mana() or (self.spells[potion][len(self.spells[potion])-1] != 0 and self.spells[potion][len(self.spells[potion])-1] != 1) ):
                        if (poss_list==[]):
                            potion = self.cast_potion()
                        else:
                            #print('poped_twice')
                            potion = poss_list.pop(0)
                        #attempted_potion.append(potion)
                        #print('new potion')
                        #print('new potion: ',potion,attempted_poti
                        no_funds = self.check_price()
                        if (no_funds):
                            break
                            #print('all tried')
                            #no_funds = True
                            #break
                        
                        cnt+=1
                    #no_funds = self.check_price()
                    if(no_funds or self.p1.get_mana()<=0):
                        #print('no funds')
                        #print(attempted_potion,list(self.spells.keys()))
                        self.p1.set_hp(0)
                    
                    else:
                        #print('pay',abs(self.spells[potion][0]),self.p1.get_mana())
                        #time.sleep(1)
                        
                        curr_spells.append(potion)
                        if (potion == 'magic missile' or potion == 'drain'):
                            
                            #self.p1.set_spent(self.p1.get_spent()+abs(self.spells[potion][0]))
                            self.boss.set_hp(self.boss.get_hp()-self.spells[potion][1])
                            self.p1.set_hp(self.p1.get_hp()+self.spells[potion][2])
                        else:
                            if (self.spells[potion][len(self.spells[potion])-1]==1):
                               # print('at ones')
                                self.update_spells_single(potion)
                                has_gone_flag = True
                            
                            if  (potion == 'sheild'):
                                self.spells[potion][len(self.spells[potion])-1] = self.spells[potion][3]
                            else:
                                self.spells[potion][len(self.spells[potion])-1] = self.spells[potion][3]
                            #self.p1.set_mana(self.p1.get_mana()+self.spells[potion][0])
                            
                        
                        #print('before_subtract: ',self.p1.get_mana())
                        self.p1.set_mana(self.p1.get_mana()-self.spells[potion][0])
                        #print('after_subtract: ',self.p1.get_mana())
                        
                        self.p1.set_spent(self.p1.get_spent()+abs(self.spells[potion][0]))
                        #if(has_gone_flag == False):
                        self.update_spells(potion)
                        #if (has_gone_flag):
                            
                    #damage
                    #attack = self.p1.get_d()-self.boss.get_a()
                    #amt = self.boss.get_hp()-attack
                    #if(attack<=0):
                    #    amt = self.boss.get_hp()-1
                        #print('ERROR')
                    #self.boss.set_hp(amt)
                    #print('me attack',amt)
                    #['poison', 'recharge', 'drain', 'poison', 'recharge', 'sheild', 'poison', 'drain', 'magic missile']
            else:
                start =1
                
                #self.boss.set_hp()
                attack = self.boss.get_d()-self.p1.get_a()
                #print(attack)
                amt = self.p1.get_hp()-attack
                if(attack<=0):
                    amt = self.p1.get_hp()-1
                self.p1.set_hp(amt)
                self.update_spells('')
                #print('boss attack',amt)
            #time.sleep(1)
            
        if (self.p1.get_hp()<=0 ):
            self.winner = 0
        else:
            self.winner = 1
        #print('winner: ',self.winner)
        return curr_spells
    def reset_p1(self):
        self.p1.set_hp(50)
        self.p1.set_d(0)
        self.p1.set_a(0)
        self.p1.set_spent(0)
        self.reset_spells()
        self.p1.set_mana(500)
        self.boss.set_hp(55)
        self.boss.set_d(8)
        self.boss.set_a(0)
    def reset_spells(self):
        for spell in list(self.spells.keys()):
            self.spells[spell][len(self.spells[spell])-1] = 0
    def run_game(self,plist):
        #while(plist != []):
        self.play(plist)
        print(self.winner)
        print(self.boss.get_hp())
    def run_games(self):
        
        #all_games = []
        #max_len_game = 20
        #all_comb = list(itertools.combinations(list(self.spells.keys()),max_len_game))
        #all_poss = list(itertools.permutations(all_comb,len(all_comb)))
        #print(all_comb)
        #random.shuffle(all_poss)
        
        
        all_games_won = []
        spells_for_games_one = []
        all_games_lost = []
        all_states = []
        all_manas = []
        all_scores=[]
        cnt = 0
        while(cnt<500000):
            cost = 0
                #print(x,thing)
            #print('before')
            spell = self.play([])
            #print(spell)
            #time.sleep(1)
            #print('after')
            #print(spell)
            #time.sleep(1)
            if (spell not in all_states):
                all_states.append(spell)
                cost = self.p1.get_spent()
                #print(cost)
                if(self.winner == 1):
                    #print('winnner',cost)
                    all_manas.append(self.p1.get_mana())
                    spells_for_games_one.append(spell)
                    all_games_won.append(cost)
                    all_scores.append([self.p1.get_hp(),self.boss.get_hp()])
                else:
                    #print('loser')
                    all_games_lost.append(cost)
                #print(cnt)
                cnt+=1
            if(cnt%10000==0):
                print(cnt)
                low = min(all_games_won)
                index = all_games_won.index(low)
                spells_casted = spells_for_games_one[index]
                mana_left = all_manas[index]
                scor = all_scores[index]
                print(low,spells_casted,mana_left,scor)
            self.reset_p1()
                #print(min(all_games_won))
        #print(min(all_games_won))
        low = min(all_games_won)
        index = all_games_won.index(low)
        spells_casted = spells_for_games_one[index]
        
        print(low,spells_casted)
        #print(max(all_games_lost))
        
        
        #self.play()
        #print(self.p1.get_spent())
            
                
    def get_all_poss(self):
        all_poss = []
        #potions_list = [i for i in list(self.spells.keys())]
        
        #all_poss = list(itertools.permutations(potions_list,len(potions_list)))
        return all_poss

Hit_Points = 55
Damage = 8
Armor = 0
                        
game_sim = game(Hit_Points,Damage,Armor)
game_sim.run_games()
#game_sim.run_game(['recharge', 'sheild', 'poison', 'recharge', 'magic missile', 'sheild', 'poison', 'magic missile', 'magic missile', 'magic missile', 'magic missile'])
#start = 1242
#top = 1295


    
  
