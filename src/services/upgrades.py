class Upgrade:
    def __init__(self, upgrades = [("example 1", 100, 1),
                                   ("example 2", 400, 2),
                                   ("example 3", 800, 1)]):
        self.upgrades = upgrades

    def buy(self, resources, x):
        if resources.R1  >= self.upgrades[x][1]:
            resources.R1 -= self.upgrades[x][1]
            resources.addR1 += self.upgrades[x][2]
            self.upgrades.pop(x)
