import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("分割窗格示例")

# 创建一个分割窗格
paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)  # 水平分割窗格
paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)  # 垂直分割窗格

# 创建两个子窗格（面板）
frame1 = ttk.Frame(paned_window, width=200, height=300, relief="sunken")
frame2 = ttk.Frame(paned_window, width=200, height=300, relief="sunken")

# 将子窗格添加到分割窗格中
paned_window.add(frame1)
paned_window.add(frame2)

# 设置分割窗格的分隔条位置
paned_window.paneconfig(frame1, minsize=100)  # 设置frame1的最小大小
paned_window.paneconfig(frame2, minsize=100)  # 设置frame2的最小大小

paned_window.pack(fill=tk.BOTH, expand=True)

root.mainloop()
