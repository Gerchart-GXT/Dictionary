import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
class Dialog:
    def __init__(self, root, title, inputItems, buttonItems):
        self.dialog = tk.Toplevel(root)
        self.dialog.title(title)
        self.inputs = []
        for item in inputItems:
            ttk.Label(self.dialog, text=f"{item[0]}:").pack()
            input = ttk.Entry(self.dialog)
            input.insert(0, item[1])
            input.pack()
            self.inputs.append(input)
        for button in buttonItems:
            tk.Button(self.dialog, text=button[0], command=button[1]).pack()
        
    def get_input(self):
        return [i.get() for i in self.inputs]
