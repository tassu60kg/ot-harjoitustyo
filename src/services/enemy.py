class Enemy:
    def __init__(self, name, powerscale):
        self.name = name
        self.powerscale = powerscale
        self.iteration = 1

    def scale(self):
        self.iteration += 1
        self.name = f"enemy {self.iteration}"
        self.powerscale *= 10
