import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *

class Menu(tk.Menu):
    def __init__(self, root, font, frames):
        super().__init__(root)
        for key, value in frames.items():
            value.grid(row=0, column=0, sticky="nsew")
        self.__font = font
        root.config(menu=self)
        (ttk.Menubutton(bootstyle="outline"))
        self.add_command(label="翻译", font=self.__font, command=lambda :self._change_frame(frames["translate_page"]))
        self.add_command(label="历史记录", font=self.__font, command=lambda :self._change_frame(frames["history_page"]))
        self.add_command(label="当前已保存", font=self.__font, command=lambda :self._change_frame(frames["saved_page"]))
        self.add_command(label="打开笔记本", font=self.__font, command=lambda :self._change_frame(frames["notebook_page"]))
        self.add_command(label="关于", font=self.__font, command=lambda :self._change_frame(frames["about_page"]))
    def _change_frame(self, frame):
        frame._render()
        frame.tkraise()
