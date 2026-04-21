from math import log

class Fighting:
    def __init__(self):
        pass

    def fight(self, character, enemy):
        x = 1
        for i in character.statblock:
            x*=(1+log(i[1]))
        if x > enemy.powerscale:
            return True
        else: return False
