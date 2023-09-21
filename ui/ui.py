import tkinter as tk
from ttkbootstrap.constants import *
from menu import Menu
from page import Page
from translate_page import TranslatePage
from history_page import HistoryPage
class Ui:
    def __init__(self, font, size, tools):
        self.root = tk.Tk()
        self.root.title("Gerchart's Dic")
        self.root.geometry(size)
        self.font = font
        frames = {
            "translate_page": TranslatePage(self.root, self.font, tools),
            "history_page": HistoryPage(self.root, self.font, tools)
            # "saved_page": Page(self.root, self.font, tools["db"]),
            # "notebook_page": Page(self.root, self.font, tools["db"]),
            # "about_page": Page(self.root, self.font, tools["db"])
        }
        self.__menu = Menu(self.root, self.font, frames=frames)
        self.root.mainloop()

    
