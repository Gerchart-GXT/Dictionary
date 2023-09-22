import tkinter as tk
from .dialog import Dialog
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
class Table:
    def __init__(self, root, font, heading):
        self.root = root
        self._font = font
        self.heading = heading
        self.table = ttk.Treeview(root, columns=tuple(map(str, [i[0] for i in heading])), height=30)
        for i in heading:
            self.table.heading(str(i[0]), text=i[1])
            self.table.column(str(i[0]), width=500, stretch=NO)
        self.popup_menu = None
        # self.table.bind("<Button-3>", self.on_right_click)
        
    def get_select_item(self):
        return self.table.selection()
    
    def get_item_value(self, item):
        return self.table.item(item, "value")
    
    def on_right_click(self, event):
        if self.popup_menu != None:
            self.popup_menu.destroy()
        if len(self.get_select_item()) == 1:
            self.popup_menu = tk.Menu(self.root, tearoff=0, font=self._font)
            self.popup_menu.add_command(label="编辑", command=self.edit_item, )
            self.popup_menu.add_command(label="删除", command=self.delete_item)
            self.popup_menu.add_command(label="展开", command=self.expand_item)
            self.popup_menu.add_command(label="关闭", command=self.popup_menu)
            self.popup_menu.post(event.x_root, event.y_root)
        elif len(self.get_select_item()) > 1:
            pass

    def insert_item(self, values):
        row = self.table.insert("", "end", values=[i for i in values if isinstance(i, str)]) 
        for i in values:
            if type(i) == str:
                continue
            subRow = self.table.insert(row, "end", text=i[0], values=("英", "汉"))
            for j, text in enumerate(i[1], start=0):
                self.table.insert(subRow, "end", text=str(j + 1), values=text)
        

    def delete_item(self):
        self.table.delete(self.get_select_item())
    
    def edit_item(self):
        item = self.get_item_value(self.get_select_item())
        dlg = Dialog(root=self.root, title="更改", inputItems=zip([i[1] for i in self.heading], list(item)), buttonItems=None)
        dlg.pack()
    
    def expand_item(self):
        pass

    def change_item(self, item, values):
        self.table.item(item, values=values, )

    def destory(self):
        self.table.destroy()
        del self
