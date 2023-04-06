class ingredient:
    def __init__(self,name,c,d,f,t,ca):
        self.capacity = c
        self.durability = d
        self.flavor = f
        self.texture = t
        self.calories = ca
        self.name = name
        self.curr_amount = 0
    def set_amount(self,a):
        self.curr_amount = a
    def get_amount(self):
        return self.curr_amount
