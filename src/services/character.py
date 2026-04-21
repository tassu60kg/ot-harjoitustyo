from math import ceil

class Character:
    def __init__(self,
                 statblock = [["power",1],
                              ["agility",1],
                              ["tuffness",1],
                              ["brain",1],
                              ["cerebellum",1],
                              ["skill6",1] ],
                 ap=0,ap_cost = 100):
        self.statblock = statblock
        self.ap = ap
        self.ap_cost = ap_cost

    def buy_ap(self, resources):
        if resources.r1 >= self.ap_cost:
            self.ap += 1
            resources.r1 -= self.ap_cost
            self.ap_cost = ceil(self.ap_cost * 1.4)

    def upgrade(self, x):
        if self.ap > 0:
            self.statblock[x][1] += 1
            self.ap -= 1
