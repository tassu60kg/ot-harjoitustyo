class SaveLoad:
    """saves and loads
    Args:
        file (str) : filename to use for savedata
    """
    def __init__(self, file = "savedata.txt"):
        self.file = file

    def save(self, upgrade, resources, character, enemy):
        with open(self.file, "w") as save:
            save.write(f"({str(upgrade.upgrades).strip("[]")[1:-1]})\n{resources.r1}\n{resources.add_r1}\n{str(character.statblock)[1:-1]}\n{character.ap}\n{character.ap_cost}\n{enemy.name}\n{enemy.powerscale}\n{enemy.iteration}")

    def load(self, upgrade, resources, character, enemy):
        """loads the save file; horrible method, should've been split into parts"""
        with open(self.file) as save:
            temp = [i.rstrip() for i in save]
            _templist = []
            _x =  temp[0].split(", ")
            for i in range(0,len(_x)-2,3):
                #if i != 0:
                #    _x[i] = _x[i][1:]
                _templist.append((_x[i][2:-1],int(_x[i+1]),int(_x[i+2].strip("()"))))
            upgrade.upgrades = _templist
            resources.r1 = int(temp[1])
            resources.add_r1 = int(temp[2])
            _templist = []
            _x =  temp[3].split(", ")
            for i in range(0,len(_x)-1,2):
                _templist.append([_x[i][2:-1],int(_x[i+1][:-1])])
            character.statblock = _templist
            character.ap = int(temp[4])
            character.ap_cost = int(temp[5])
            enemy.name = temp[6]
            enemy.powerscale = int(temp[7])
            enemy.iteration = int(temp[8])
