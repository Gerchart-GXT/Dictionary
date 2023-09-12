import tkinter as tk
from tkinter import filedialog
class Ui:
    def __init__(self, font, size):
        self.__root = tk.Tk()
        self.__root.geometry(size)
        self.__font = font
        self.removedWidget = {}

    def _change_title(self, title):
        self.__root.title(title)

    def show(self):
        self.__root.mainloop()

    def _open_file(self):
        file_path = filedialog.askopenfilename(title="选择文件")  # 打开文件选择对话框
        if(file_path):
            return file_path
        return None
    
    def _label_create(self, text):
        label = tk.Label(self.__root, text = text, font = self.__font)
        return label
    def _button_create(self, text, command):
        button = tk.Button(self.__root, text="选择文件", font = self.__font, command = command)
        return button
    def _text_display_create(self, height, width):
        textDisplay = tk.Text(self.__root, height = height, width = width)
        return textDisplay
    def _add_widget(self, widget, row, col):
        widget.grid(row = row, col = col)
    def _remove_widget(self, widget):
        self.removedWidget.add(widget)
        widget.grid_forget()
def main():
    ui = Ui()
    ui.show()

if __name__ == "__main__":
    main()
# font=("微软雅黑", 17)

# def on_submit():
#     input_text = entry.get()  # 获取文本输入框中的文本
#     output_label.config(text=f"你输入的文本是：{input_text}")

# root = tk.Tk()
# root.title("Gerchart's Dic!")

# # 创建文本输入框
# entry = tk.Entry(root, width=30)
# entry.pack()

# # 创建按钮用于提交文本
# submit_button = tk.Button(root, text="提交", command=on_submit, font=font)
# submit_button.pack()

# # 创建标签用于显示文本
# output_label = tk.Label(root, text="")
# output_label.pack()

# root.mainloop()
