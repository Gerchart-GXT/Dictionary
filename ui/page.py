import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext

class Page(ttk.Frame):
    def __init__(self:tk.Frame, root, font):
        super().__init__(root)
        self.__font = font

    def _open_file(self):
        file_path = filedialog.askopenfilename(title="选择文件")  # 打开文件选择对话框
        if(file_path):
            return file_path
        return None
    
    def _label_create(self, text):
        label = ttk.Label(self, text = text, font = self.__font, wraplength=800, justify='left')
        return label
    
    def _button_create(self, text, command, bootstyle):
        button = ttk.Button(master=self, text=text, command = command, bootstyle=bootstyle)
        return button
    
    def _input_create(self):
        input = ttk.Entry(self, font=self.__font, width=100)
        return input
    
    def _text_create(self, expr):
        text = scrolledtext.ScrolledText(self, font=self.__font, wrap=WORD, width=50, height=10)

        text.delete(1.0, tk.END)
        text.insert(tk.END, expr)
        text.config(state="disabled")

        return text

    def _add_widget(self, widget, row, col):
        widget.grid(row = row, col = col)

    def _remove_widget(self, widget):
        widget.destroy()

    def _clear_widget(self, widgets):
        for widget in widgets:
            widget.destroy()

    def quit(self):
        self.quit()
    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("2000X2000")
    page = Page(root)
    page.pack()
    root.mainloop()