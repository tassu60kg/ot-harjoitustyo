from copy import deepcopy


class SaveLoad:
    def __init__(self, file = "savedata.txt"):
        self.file = file

    def save(self, upgrade, resources, character):
        with open(self.file, "w") as save:
            save.write(f"({str(upgrade.upgrades).strip("[]")[1:-1]})\n{resources.r1}\n{resources.add_r1}\n{str(character.statblock)[1:-1]}\n{character.ap}\n{character.ap_cost}")

    def load(self, upgrade, resources, character):
        with open(self.file) as save:
            temp = [i.rstrip() for i in save]
            print(temp)
            print(type(temp[0]))
            _templist = []
            _x =  temp[0].split(",")
            for i in range(0,len(_x)-2,3):
                print(_x[i])
                _templist.append((_x[i],int(_x[i+1]),int(_x[i+2].strip("()"))))
            print(_templist)
            upgrade.upgrades = _templist