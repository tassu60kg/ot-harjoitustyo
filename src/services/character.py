from math import ceil

class Character:
    """Responsible for stats and AP
    Attributes:
        statblock  : skills and their level, there should be 6 or something breaks
        ap : current ap
        ap_cost : current cost of buying ap
    """
    def __init__(self, statblock=None, ap=0,ap_cost = 100):
        if statblock is None:
            self.statblock = [["power",1],
                              ["agility",1],
                              ["tuffness",1],
                              ["brain",1],
                              ["cerebellum",1],
                              ["skill6",1] ]
        else:
            self.statblock = statblock
        self.ap = ap
        self.ap_cost = ap_cost

    def buy_ap(self, resources):
        """
        Args:
            resources (resources type object): resources to use for buying ap
        """
        if resources.r1 >= self.ap_cost:
            self.ap += 1
            resources.r1 -= self.ap_cost
            self.ap_cost = ceil(self.ap_cost * 1.4)

    def upgrade(self, x):
        """
        Args:
            x (int): index of the skill in statblock to upgrade
        """
        if self.ap > 0:
            self.statblock[x][1] += 1
            self.ap -= 1

    def unupgrade(self, x):
        """
        Args:
            x (int): index of the skill in statblock to unupgrade
        """
        if self.statblock[x][1] > 1:
            self.statblock[x][1] -= 1
            self.ap += 1
