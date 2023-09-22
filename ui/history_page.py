import tkinter as tk
import json
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from .page import Page
from .table import Table
class HistoryPage(Page):
    def __init__(self:Page, root, font, tools):
        super().__init__(root, font)
        self.db = tools["db"]
        self.font = font
        self._widgets = []

        self._render()

    def _update_item(self):
        word = self.tb.get_item_value(self.tb.get_item_value())[0]
        item = self.db.get_history_word(word)[0]


    def _delete_item(self):
        pass

    def _save_item(self):
        pass

    def _render(self):
        super()._clear_widget(self._widgets)
        historyWord = self.db.get_allhistory()[1]
        self.tb = Table(self, font=self.font, heading=[("word", "单词"),("saved", "是否保存")])
        self._widgets.append(self.tb.table)
        self.tb.table.grid(row="2", columnspan="12", padx='5', pady='5', sticky=NSEW)

        delWord = super()._button_create(text="删除", bootstyle=DANGER,command = lambda : self._delete_item(self.tb))
        self._widgets.append(delWord)
        delWord.grid(row="1", column="0", columnspan="4", padx='5', pady='5', sticky=NSEW)

        updateWord = super()._button_create(text="编辑", bootstyle=INFO,command = lambda : self._update_item(self.tb))
        self._widgets.append(updateWord)
        updateWord.grid(row="1",column="4", columnspan="4", padx='5', pady='5', sticky=NSEW)
        
        editWord = super()._button_create(text="保存", bootstyle=SUCCESS,command = lambda : self._save_item(self.tb))
        self._widgets.append(editWord)
        editWord.grid(row="1", column="8", columnspan="4", padx='5', pady='5', sticky=NSEW)


        if(len(historyWord) > 0):
            for i in historyWord:
                expr = json.loads(i[2])
                print(expr["phrase"])
                self.tb.insert_item((i[1], ("字典", expr["dic"]), ("词汇", expr["phrase"]), ("注释", expr["tip"]), "是" if i[5] == 1 else "否"))
