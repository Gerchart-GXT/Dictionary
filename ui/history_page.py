import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from page import Page
from table import Table
class HistoryPage(Page):
    def __init__(self:Page, root, font, db):
        super().__init__(root, font)
        self.db = db
        self.font = font
        self._historyWord = db.get_allhistory()[1]
        self._widgets = []

        self._render()

    def _change_item(self):
        curSelect = self.

    def _render(self):
        super()._clear_widget(self._widgets)

        tb = Table(self, [("word", "单词"), ("dic", "字典"), ("phrase", "词汇"), ("tips", "注释"), ("saved", "是否保存")], )
