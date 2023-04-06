import random
import itertools
import time

class player:
    def __init__(self,hp,d,a):
        self.set_hp(hp)
        self.set_d(d)
        self.set_a(a)

    def set_a(self,a):
        self.a = a
    def set_hp(self,hp):
        self.hp = hp
    def set_d(self,d):
        self.d = d
        
    def get_a(self):
        return self.a
    def get_hp(self):
        return self.hp
    def get_d(self):
        return self.d
    
class game:
    def __init__(self,boss_hp,boss_d,boss_a):
        self.boss = player(boss_hp,boss_d,boss_a)
        self.winner = None
        self.store = {'w':{'dagger':[8,4,0],'shortsword':[10,5,0],'warhammer':[25,6,0],'longsword':[40,7,0],'greataxe':[74,8,0]},'a':{'leather':[13,0,1],'chainmail':[31,0,2],'splitmail':[53,0,3],'bandedmail':[75,0,4],'platemail':[102,0,5],'none':[0,0,0]},'r':{'none':[0,0,0],'damage +1':[25,1,0],'damage +2':[50,2,0],'damage +3':[100,3,0],'defense +1':[20,0,1],'defence +2':[40,0,2],'defence +3':[80,0,3]}}
        self.p1 = player(100,0,0)
    def play(self):
        
        start = 1
        while(self.p1.get_hp()>0 and self.boss.get_hp()>0):
            if (start%2==1):
                start = 2
                #damage
                attack = self.p1.get_d()-self.boss.get_a()
                amt = self.boss.get_hp()-attack
                if(attack<=0):
                    amt = self.boss.get_hp()-1
                    #print('ERROR')
                self.boss.set_hp(amt)
                #print('me attack',amt)
            else:
                start =1
                attack = self.boss.get_d()-self.p1.get_a()
                #print(attack)
                amt = self.p1.get_hp()-attack
                if(attack<=0):
                    amt = self.p1.get_hp()-1
                self.p1.set_hp(amt)
                #print('boss attack',amt)
            #time.sleep(1)
            
        if (self.p1.get_hp()<=0 ):
            self.winner = 0
        else:
            self.winner = 1
        
    def reset_p1(self):
        self.p1.set_hp(100)
        self.p1.set_d(0)
        self.p1.set_a(0)
        self.boss.set_hp(104)
        self.boss.set_d(8)
        self.boss.set_a(1)
    def run_games(self):
        all_poss  = self.get_all_poss()
        print(len(all_poss))
        random.shuffle(all_poss)
        all_games_won = []
        all_games_lost = []
        for x in all_poss:
            print(x)
            cost = 0
            for thing in x:
                #print(x,thing)
                
                self.p1.set_d(self.p1.get_d()+thing[1])
                self.p1.set_a(self.p1.get_a()+thing[2])
                cost +=thing[0]
            self.play()
            self.reset_p1()
            if(self.winner == 1):
                print('winnner',cost)
                all_games_won.append(cost)
            else:
                all_games_lost.append(cost)
                
        print(min(all_games_won))
        print(max(all_games_lost))
            
            
                
    def get_all_poss(self):
        all_poss = []
        weapons_list = [i for i in list(self.store['w'].keys())]
        
        all_rings = list(itertools.combinations(range(7),2))
        all_rings.append([0,0])
        armor_list = [i for i in list(self.store['a'].keys())]
        
        for weap in weapons_list:
            for arm in armor_list:
               
                for rings_pair in all_rings:
                    rings_key1 = list(self.store['r'].keys())[rings_pair[0]]
                    rings_key2 = list(self.store['r'].keys())[rings_pair[1]]
                    
                    
                    all_poss.append([self.store['w'][weap],self.store['a'][arm],self.store['r'][rings_key1],self.store['r'][rings_key2]])
        print(all_poss)            
        return all_poss

Hit_Points = 104
Damage = 8
Armor = 1
                        
game_sim = game(Hit_Points,Damage,Armor)
game_sim.run_games()


  
