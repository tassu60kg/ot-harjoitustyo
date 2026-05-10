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
        self._upgradelist = Variable(value=self.upgrade.upgrades)
        self.character = character.Character()
        self._character_stats = Variable(value=self.character.statblock)
        self._upgrade_selector = 0
        self._apgrade_selector = 0
        self.fighting = fighting.Fighting("enemy", 1)
        self.saveload = saveload.SaveLoad()
        self._upgrade_box = Listbox(master=self._root, listvariable=self._upgradelist)
        self._character_box = Listbox(master=self._root, listvariable=self._character_stats)
        self._r1 = ttk.Label(master=self._root, text=self.resource.r1)
        self._persec_r1 = ttk.Label(master=self._root,
                                   text=f"{self.resource.add_r1*10} swag per second")
        self._ap = ttk.Label(master=self._root, text=self.character.ap)
        self._enemy_text = ttk.Label(master=self._root,
                              text=f"{self.fighting.name}: {self.fighting.powerscale} power")
        self._powerlevel = ttk.Label(master=self._root, text=self.fighting.character_power)

    def start(self):
        def _buy_ap_button():
            self.character.buy_ap(self.resource)
        def _upgrade_action():
            self.upgrade.buy(self.resource, self._upgrade_selector)
        def _apgrade_action():
            self.character.upgrade(self._apgrade_selector)
        def _unapgrade_action():
            self.character.unupgrade(self._apgrade_selector)
        def _fight_action():
            if self.fighting.fight():
                self.fighting.scale()
        def _save_action():
            self.saveload.save(self.upgrade,
                               self.resource,
                               self.character,
                               self.fighting)
        def _load_action():
            self.saveload.load(self.upgrade,
                               self.resource,
                               self.character,
                               self.fighting)

        buyap = ttk.Button(master=self._root, text ="buy ap", command=_buy_ap_button)
        upgrade_button = ttk.Button(master=self._root, text="buy upgrade", command=_upgrade_action)
        apgrade_button = ttk.Button(master=self._root, text="buy apgrade", command=_apgrade_action)
        unapgrade_button = ttk.Button(
            master=self._root, text="unapgrade", command=_unapgrade_action)
        enemy_button = ttk.Button(master=self._root, text="fight",command=_fight_action)
        save_button = ttk.Button(master=self._root, text="save", command=_save_action)
        load_button = ttk.Button(master=self._root, text="load", command=_load_action)

        warningthing = ttk.Label(master=self._root,
                                 text="if something goes out of the window resize it")
        self._r1.grid(row=0, column=0)
        self._ap.grid(row=1, column=0)
        buyap.grid(row=1,column=1)
        self._persec_r1.grid(row=0, column=1)
        self._upgrade_box.grid(row=2,column=0)
        self._character_box.grid(row=2, column=1)
        upgrade_button.grid(row=3,column=0)
        apgrade_button.grid(row=3,column=1)
        unapgrade_button.grid(row=4, column=1)
        self._enemy_text.grid(row=5, column=1)
        enemy_button.grid(row=6, column=1)
        self._powerlevel.grid(row=0, column=2)
        save_button.grid(row=5,column=0)
        load_button.grid(row=6,column=0)
        warningthing.grid(row=4, column=0)

        def _upgrade_box_handler(_event):
            try: #tkinter problem, not my fault
                self._upgrade_selector = int(self._upgrade_box.curselection()[0])
            except IndexError:
                pass
        def _character_box_handler(_event):
            try:
                self._apgrade_selector = int(self._character_box.curselection()[0])
            except IndexError:
                pass
        self._upgrade_box.bind("<<ListboxSelect>>", _upgrade_box_handler)
        self._character_box.bind("<<ListboxSelect>>", _character_box_handler)

    def update(self):
        self.resource.increase()
        self._r1.config(text=f"swag {self.resource.r1}")
        self._ap.config(text=f"apgrade points {self.character.ap} ap cost {self.character.ap_cost}")
        self._persec_r1.config(text=f"{self.resource.add_r1*10} swag per second")
        self._upgradelist = Variable(value=self.upgrade.upgrades)
        self._upgrade_box.config(listvariable=self._upgradelist)
        self._character_stats = Variable(value=self.character.statblock)
        self._character_box.config(listvariable=self._character_stats)
        self._enemy_text.config(text=f"{self.fighting.name}: {self.fighting.powerscale} power")
        self.fighting.get_power(self.character.statblock)
        self._powerlevel.config(text=f"power: {self.fighting.character_power}")
        self._root.after(100,self.update)
