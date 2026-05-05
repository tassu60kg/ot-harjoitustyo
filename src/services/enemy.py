class Enemy:
    def __init__(self, name, powerscale):
        self.iteration = 1
        self.name = f"{name} {self.iteration}"
        self.powerscale = powerscale

    def scale(self):
        self.iteration += 1
        self.name = f"{self.name[:-2]} {self.iteration}"
        self.powerscale *= 2
