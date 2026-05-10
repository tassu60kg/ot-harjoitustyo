class SaveLoad:
    """saves and loads
    Args:
        file (str) : filename to use for savedata
    """
    def __init__(self, file = "data/savedata.txt"):
        self.file = file

    def save(self, upgrade, resources, character, fighting):
        """saves the current state of objects to file
        Args:
            upgrade (upgrade type object):
            resources (resources type object):
            character (character type object):
            enemy (enemy type object):
            """
        with open(self.file, "w", encoding="utf-8") as save:
            save.write(f"{str(upgrade.upgrades)[1:-1]}\n{resources.r1}\n{resources.add_r1}\n{str(character.statblock)[1:-1]}\n{character.ap}\n{character.ap_cost}\n{fighting.name}\n{fighting.powerscale}\n{fighting.iteration}")

    def load(self, upgrade, resources, character, fighting):
        """loads the saved states to objects
        Args:
            upgrade (upgrade type object):
            resources (resources type object):
            character (character type object):
            enemy (enemy type object):
            """
        try:
            with open(self.file, encoding="utf-8") as save:
                temp = [i.rstrip() for i in save]
                _templist = []
                _x =  temp[0].split(", ")
                for i in range(0,len(_x)-2,3):
                    _templist.append([_x[i][2:-1],int(_x[i+1]),int(_x[i+2][:-1])])
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
                fighting.name = temp[6]
                fighting.powerscale = int(temp[7])
                fighting.iteration = int(temp[8])
        except FileNotFoundError:
            print("save file does not exist")
