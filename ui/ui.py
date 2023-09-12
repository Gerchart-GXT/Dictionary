import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from menu import Menu
from page import Page
from translate_page import TranslatePage
class Ui:
    def __init__(self, font, size):
        self.root = tk.Tk()
        self.root.title("Gerchart's Dic")
        self.root.geometry(size)
        self.font = font
        frames = {
            "translate_page": TranslatePage(self.root, self.font),
            "history_page": Page(self.root, self.font),
            "saved_page": Page(self.root, self.font),
            "notebook_page": Page(self.root, self.font),
            "about_page": Page(self.root, self.font)
        }
        self.__menu = Menu(self.root, self.font, frames=frames)
        self.root.mainloop()

if __name__ == "__main__":
    ui = Ui(font=("微软雅黑", 14), size="600x600")
    
