import tkinter as tk
from tkinter import ttk

def expand_item():
    selected_item = treeview.selection()
    if selected_item:
        treeview.item(selected_item, open=True)

def collapse_item():
    selected_item = treeview.selection()
    if selected_item:
        treeview.item(selected_item, open=False)

root = tk.Tk()
root.title("Multi-Level Treeview")

# 创建 Treeview
treeview = ttk.Treeview(root)
treeview.pack()

# 添加根节点
root_node = treeview.insert("", "end", text="Root", open=True)

# 添加子节点
child1 = treeview.insert(root_node, "end", text="Child 1", open=True)
child2 = treeview.insert(root_node, "end", text="Child 2")

# 添加孙子节点
grandchild1 = treeview.insert(child1, "end", text="Grandchild 1")
grandchild2 = treeview.insert(child1, "end", text="Grandchild 2")

# 添加按钮来展开和折叠选定项
expand_button = tk.Button(root, text="Expand", command=expand_item)
expand_button.pack()

collapse_button = tk.Button(root, text="Collapse", command=collapse_item)
collapse_button.pack()

root.mainloop()
