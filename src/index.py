from tkinter import Tk, ttk, Listbox
import tkinter
from services import resources
from services import upgrades


class UI:
    def __init__(self, root):
        self._root = root
        self.gamethng = resources.Resource()
        self.upgrade = upgrades.Upgrade()
        self.upgradelist = tkinter.Variable(value=self.upgrade.upgrades)

    def start(self):
        #good code alert
        global R1 
        R1 = ttk.Label(master=self._root, text=self.gamethng.R1)
        global persecR1
        R1name = ttk.Label(master=self._root, text="swag")
        persecR1 = ttk.Label(master=self._root, text=f"{self.gamethng.addR1*10} swag per second")
        global upgradeBox
        upgradeBox = Listbox(master=self._root, listvariable=self.upgradelist)
        


        R1.grid(row=0, column=0)
        R1name.grid(row=0, column=1)
        persecR1.grid(row=4, column=0)
        upgradeBox.grid(row=6,column=0)

        def boxHandler(event):
            selected = int(upgradeBox.curselection()[0])
            print(selected)
            self.upgrade.buy(self.gamethng, self.upgrade.upgrades[selected], selected)

        upgradeBox.bind("<<ListboxSelect>>", boxHandler)

    


    def update(self):
        self.gamethng.increase()
        R1.config(text=self.gamethng.R1)
        persecR1.config(text=f"{self.gamethng.addR1*10} swag per second")
        #10x per sec I think
        self.upgradelist = tkinter.Variable(value=self.upgrade.upgrades)
        upgradeBox.config(listvariable=self.upgradelist)
        self._root.after(100,self.update)
        

window = Tk()
window.geometry("600x480")
window.title("ts peak")
ui = UI(window)
ui.start()
ui.update()
window.mainloop()
