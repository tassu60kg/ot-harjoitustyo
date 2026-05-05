from tkinter import Tk
from ui import ui

window = Tk()
window.geometry("600x480")
window.title("ts peak")
ui = ui.UI(window)
ui.start()
ui.update()
window.mainloop()
