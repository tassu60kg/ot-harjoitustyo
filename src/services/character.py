from math import ceil

class Character:
    def __init__(self,
                 statblock = [["power",0],
                              ["agility",0],
                              ["tuffness",0],
                              ["brain",0],
                              ["cerebellum",0],
                              ["skill6",0] ],
                 ap=0,ap_cost = 100):
        self.statblock = statblock
        self.ap = ap
        self.ap_cost = ap_cost

    def buy_ap(self, resources):
        if resources.R1 >= self.ap_cost:
            self.ap += 1
            resources.R1 -= self.ap_cost
            self.ap_cost = ceil(self.ap_cost * 1.4)

    def upgrade(self, x):
        if self.ap > 0:
            self.statblock[x][1] += 1
            self.ap -= 1
