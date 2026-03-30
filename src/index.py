from tkinter import Tk, ttk
import gamethingy
import time


class UI:
    def __init__(self, root):
        self._root = root
        self.gamethng = gamethingy.Resource()

    def start(self):
        #good code alert
        global R1 
        R1 = ttk.Label(master=self._root, text=self.gamethng.R1)
        lable = ttk.Label(master=self._root, text="asdljlksakljdsalk")
        
        R1.grid(row=0, column=0)
        lable.grid(row=2, column=2)

    def update(self):
        self.gamethng.increase()
        R1.config(text=self.gamethng.R1)
        self._root.after(100,self.update)
        

window = Tk()
window.geometry("600x480")
window.title("ts peak")
ui = UI(window)
ui.start()
ui.update()
window.mainloop()
