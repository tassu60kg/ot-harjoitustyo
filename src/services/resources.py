class Resource:
    def __init__(self, r1=1, addr1=1):
        self.R1 = r1
        self.addR1 = addr1
    
    def increase(self):
        self.R1 += self.addR1