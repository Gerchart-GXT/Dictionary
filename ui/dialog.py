import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
class Dialog:
    def __init__(self, root, title, inputItems, tools):
        self.dialog = tk.Toplevel(root)
        self.dialog.title(title)
        self.tools = tools
        self.inputs = []
        for item in inputItems:
            ttk.Label(self.dialog, text=f"{item[0]}:").pack()
            input = ttk.Entry(self.dialog)
            input.insert(0, item[1])
            input.pack()
            self.inputs.append(input)
        button = ttk.Button(master=self, text="保存", command=self.get_input(), bootstyle=SUCCESS)
        button = ttk.Button(master=self, text="取消", command=self.dialog.destroy(), bootstyle=SUCCESS)
        
    def get_input(self):
        self.tools["dialogValue"] = [i.get() for i in self.inputs]

