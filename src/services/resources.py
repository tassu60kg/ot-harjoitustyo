class Resource:
    def __init__(self, r1=1, add_r1=1):
        self.r1 = r1
        self.add_r1 = add_r1
    
    def increase(self):
        self.r1 += self.add_r1
