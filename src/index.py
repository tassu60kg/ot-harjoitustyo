from tkinter import Tk, ttk, Listbox, Variable
from services import resources
from services import upgrades
from services import character

class UI:
    def __init__(self, root):
        self._root = root
        self.resource = resources.Resource()
        self.upgrade = upgrades.Upgrade()
        self.upgradelist = Variable(value=self.upgrade.upgrades)
        self.character = character.Character()
        self.character_stats = Variable(value=self.character.statblock)


    def start(self):
        def buy_ap_button():
            self.character.buy_ap(self.resource)
        #good code alert
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


        r1.grid(row=0, column=0)
        ap.grid(row=1, column=0)
        buyap.grid(row=1,column=1)
        persec_r1.grid(row=0, column=1)
        upgrade_box.grid(row=4,column=0)
        character_box.grid(row=4, column=1)


        def upgrade_box_handler(event):
            selected = int(upgrade_box.curselection()[0])
            self.upgrade.buy(self.resource, selected)

        def character_box_handler(event):
            selected = int(character_box.curselection()[0])
            self.character.upgrade(selected)

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
        self._root.after(100,self.update)


window = Tk()
window.geometry("600x480")
window.title("ts peak")
ui = UI(window)
ui.start()
ui.update()
window.mainloop()
