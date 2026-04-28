from math import log

class Fighting:
    def __init__(self):
        self.character_power = 1

    def get_power(self, statblock):
        self.character_power = ((log(statblock[0][1]*statblock[1][1])+statblock[4][1])*(log(statblock[2][1]*statblock[3][1]))/statblock[5][1])

    def fight(self, character, enemy):
        x = 1
        for i in character.statblock:
            x*=(1+log(i[1]))
        if x > enemy.powerscale:
            return True
        else: return False
