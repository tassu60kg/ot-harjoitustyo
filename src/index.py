from tkinter import Tk, ttk, Listbox, Variable
from services import resources
from services import upgrades
from services import character
from services import enemy
from services import fighting

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
        self.enemy = enemy.Enemy("enemy 1", 1)
        self.fighting = fighting.Fighting()

    def start(self):
        def buy_ap_button():
            self.character.buy_ap(self.resource)
        def upgrade_action():
            self.upgrade.buy(self.resource, self.upgrade_selector)
        def apgrade_action():
            self.character.upgrade(self.apgrade_selector)
        def fight_action():
            if self.fighting.fight(self.character, self.enemy):
                self.enemy.scale()
        global r1
        r1 = ttk.Label(master=self._root, text=self.resource.r1)
        global persec_r1
        persec_r1 = ttk.Label(master=self._root, text=f"{self.resource.add_r1*10} swag per second")
        global upgrade_box
        upgrade_box = Listbox(master=self._root, listvariable=self.upgradelist)
        global character_box
        character_box = Listbox(master=self._root, listvariable=self.character_stats)
        global ap 
        ap = ttk.Label(master=self._root, text=self.character.ap)
        buyap = ttk.Button(master=self._root, text ="buy ap", command=buy_ap_button)
        upgrade_button = ttk.Button(master=self._root, text="buy upgrade", command=upgrade_action)
        apgrade_button = ttk.Button(master=self._root, text="buy apgrade", command=apgrade_action)
        global enemy_text
        enemy_text = ttk.Label(master=self._root, 
                              text=f"{self.enemy.name}: {self.enemy.powerscale} power")
        enemy_button = ttk.Button(master=self._root, text="fight",command=fight_action)

        r1.grid(row=0, column=0)
        ap.grid(row=1, column=0)
        buyap.grid(row=1,column=1)
        persec_r1.grid(row=0, column=1)
        upgrade_box.grid(row=2,column=0)
        character_box.grid(row=2, column=1)
        upgrade_button.grid(row=3,column=0)
        apgrade_button.grid(row=3,column=1)
        enemy_text.grid(row=2, column=2)
        enemy_button.grid(row=2, column=3)

        def upgrade_box_handler(_event):
            self.upgrade_selector = int(upgrade_box.curselection()[0])

        def character_box_handler(_event):
            self.apgrade_selector = int(character_box.curselection()[0])

        upgrade_box.bind("<<ListboxSelect>>", upgrade_box_handler)
        character_box.bind("<<ListboxSelect>>", character_box_handler)


    def update(self):
        self.resource.increase()
        r1.config(text=f"swag {self.resource.r1}")
        ap.config(text=f"apgrade points {self.character.ap} ap cost {self.character.ap_cost}")
        persec_r1.config(text=f"{self.resource.add_r1*10} swag per second")
        #10x per sec I think
        self.upgradelist = Variable(value=self.upgrade.upgrades)
        upgrade_box.config(listvariable=self.upgradelist)
        self.character_stats = Variable(value=self.character.statblock)
        character_box.config(listvariable=self.character_stats)
        enemy_text.config(text=f"{self.enemy.name}: {self.enemy.powerscale} power")
        self._root.after(100,self.update)


window = Tk()
window.geometry("600x480")
window.title("ts peak")
ui = UI(window)
ui.start()
ui.update()
window.mainloop()
