import tkinter as tk
from dialog import Dialog
from ttkbootstrap import ttk
from ttkbootstrap.constants import *

class Table:
    def __init__(self, root, heading):
        self.root = root
        self.heading = heading
        self.table = ttk.Treeview(root, columns=tuple(map(str, [i[0] for i in heading])))
        for i in heading:
            self.table.heading(str(i[0]), text=i[1])
        self.table.bind("<Double-1>", self.on_item_double_click)
        
    def get_select_item(self):
        return self.table.item(self.table.selection(), "values")
    
    def on_item_double_click(self, event):
        item = self.get_select_item()
        dlog = Dialog(self.root, "更改",
            zip([heading[1] for heading in self.heading], list(item)),
            [("保存", lambda: self.change_item())])

    def insert_item(self, values):
        self.table.insert("", "end", values=values)

    def delete_item(self, item):
        self.table.delete(item)

    def change_item(self, item, values):
        self.table.item(item, values=values)
