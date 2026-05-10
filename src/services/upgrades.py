class Upgrade:
    def __init__(self, upgrades = None):
        if upgrades is None:
            self.upgrades =  [["upgrade 1", 100, 1],
                                   ["upgrade 2", 200, 2],
                                   ["upgrade 3", 400, 3],
                                   ["upgrade 4", 800, 4],
                                   ["upgrade 5", 1600, 5],
                                   ["upgrade 6", 3200, 6]]
        else:
            self.upgrades = upgrades

    def buy(self, resources, x):
        if resources.r1  >= self.upgrades[x][1]:
            resources.r1 -= self.upgrades[x][1]
            resources.add_r1 += self.upgrades[x][2]
            self.upgrades.pop(x)
