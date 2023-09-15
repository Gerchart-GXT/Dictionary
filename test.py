import tkinter as tk

def custom_dialog(title, root):
    dialog = tk.Toplevel(root)  # 创建一个新的顶级窗口
    dialog.title(title)
    
    # 创建文本框
    label = tk.Label(dialog, text=f"{title} 输入:")
    label.pack()
    entry = tk.Entry(dialog)
    entry.pack()

    # 创建确定按钮
    def on_ok():
        input_text = entry.get()
        print(f"{title} 输入:", input_text)
        dialog.destroy()
    
    ok_button = tk.Button(dialog, text="确定", command=on_ok)
    ok_button.pack()

root = tk.Tk()
root.title("多个自定义对话框示例")

# 创建多个自定义对话框
custom_dialog("对话框 1", root)
custom_dialog("对话框 2", root)
custom_dialog("对话框 3", root)

root.mainloop()
