class Upgrade:
    def __init__(self):
        self.upgrades = [("example 1", 100, 1), ("example 2", 400, 2), ("example 3", 800, 1)]

    def buy(self, resources, upgrade, x):
        if resources.R1  >= upgrade[1]:
            resources.R1 -= upgrade[1]
            resources.addR1 += upgrade[2]
            self.upgrades.pop(x)