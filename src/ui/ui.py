from tkinter import ttk, Listbox, Variable
from services import resources
from services import upgrades
from services import character
from services import fighting
from data import saveload

class UI:
    def __init__(self, root):
        self._root = root
        self.resource = resources.Resource()
        self.upgrade = upgrades.Upgrade()
        self.upgradelist = Variable(value=self.upgrade.upgrades)
        self.character = character.Character()
        self.character_stats = Variable(value=self.character.statblock)
        self.upgrade_selector = 0
        self.apgrade_selector = 0
        self.fighting = fighting.Fighting("enemy", 1)
        self.saveload = saveload.SaveLoad()
        self.upgrade_box = Listbox(master=self._root, listvariable=self.upgradelist)
        self.character_box = Listbox(master=self._root, listvariable=self.character_stats)

    def start(self):
        def buy_ap_button():
            self.character.buy_ap(self.resource)
        def upgrade_action():
            self.upgrade.buy(self.resource, self.upgrade_selector)
        def apgrade_action():
            self.character.upgrade(self.apgrade_selector)
        def unapgrade_action():
            self.character.unupgrade(self.apgrade_selector)
        def fight_action():
            if self.fighting.fight():
                self.fighting.scale()
        def save_action():
            self.saveload.save(self.upgrade,
                               self.resource,
                               self.character,
                               self.fighting)
        def load_action():
            self.saveload.load(self.upgrade,
                               self.resource,
                               self.character,
                               self.fighting)

        global r1
        r1 = ttk.Label(master=self._root, text=self.resource.r1)
        global persec_r1
        persec_r1 = ttk.Label(master=self._root, text=f"{self.resource.add_r1*10} swag per second")
        global ap 
        ap = ttk.Label(master=self._root, text=self.character.ap)
        buyap = ttk.Button(master=self._root, text ="buy ap", command=buy_ap_button)
        upgrade_button = ttk.Button(master=self._root, text="buy upgrade", command=upgrade_action)
        apgrade_button = ttk.Button(master=self._root, text="buy apgrade", command=apgrade_action)
        unapgrade_button = ttk.Button(master=self._root, text="unapgrade", command=unapgrade_action)
        global enemy_text
        enemy_text = ttk.Label(master=self._root,
                              text=f"{self.fighting.name}: {self.fighting.powerscale} power")
        enemy_button = ttk.Button(master=self._root, text="fight",command=fight_action)
        global powerlevel
        powerlevel = ttk.Label(master=self._root, text=self.fighting.character_power)
        save_button = ttk.Button(master=self._root, text="save", command=save_action)
        load_button = ttk.Button(master=self._root, text="load", command=load_action)

        warningthing = ttk.Label(master=self._root,
                                 text="if something goes out of the window resize it")
        r1.grid(row=0, column=0)
        ap.grid(row=1, column=0)
        buyap.grid(row=1,column=1)
        persec_r1.grid(row=0, column=1)
        self.upgrade_box.grid(row=2,column=0)
        self.character_box.grid(row=2, column=1)
        upgrade_button.grid(row=3,column=0)
        apgrade_button.grid(row=3,column=1)
        unapgrade_button.grid(row=4, column=1)
        enemy_text.grid(row=5, column=1)
        enemy_button.grid(row=6, column=1)
        powerlevel.grid(row=0, column=2)
        save_button.grid(row=5,column=0)
        load_button.grid(row=6,column=0)
        warningthing.grid(row=4, column=0)

        def upgrade_box_handler(_event):
            try: #tkinter problem, not my fault
                self.upgrade_selector = int(self.upgrade_box.curselection()[0])
            except IndexError:
                pass
        def character_box_handler(_event):
            try:
                self.apgrade_selector = int(self.character_box.curselection()[0])
            except IndexError:
                pass
        self.upgrade_box.bind("<<ListboxSelect>>", upgrade_box_handler)
        self.character_box.bind("<<ListboxSelect>>", character_box_handler)


    def update(self):
        self.resource.increase()
        r1.config(text=f"swag {self.resource.r1}")
        ap.config(text=f"apgrade points {self.character.ap} ap cost {self.character.ap_cost}")
        persec_r1.config(text=f"{self.resource.add_r1*10} swag per second")
        #10x per sec I think
        self.upgradelist = Variable(value=self.upgrade.upgrades)
        self.upgrade_box.config(listvariable=self.upgradelist)
        self.character_stats = Variable(value=self.character.statblock)
        self.character_box.config(listvariable=self.character_stats)
        enemy_text.config(text=f"{self.fighting.name}: {self.fighting.powerscale} power")
        self.fighting.get_power(self.character.statblock)
        powerlevel.config(text=f"power: {self.fighting.character_power}")
        #print(self.saveload.data)
        self._root.after(100,self.update)
