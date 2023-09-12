from page import Page
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *

import sys
sys.path.append("../")
from translate import Translate


class TranslatePage(Page):
    def __init__(self:Page, root, font):
        super().__init__(root, font)
        self._translator = Translate("en")
        self.word = ""
        self.font = font
        self.result = {"dic": [], "phrase": []}
        self._render()

    def _translate(self, word):
        self.result = self._translator.trans_from_youdaodic(word)
        self.word = word
        super()._clear_widget()
        self._render()
    
    def _saveWord(self):
        pass

    def _render(self):
        inputArea = super()._input_create()
        subToTrans = super()._button_create(text="翻译", bootstyle=SUCCESS,command = lambda : self._translate(inputArea.get()))
        inputArea.grid(row="1", column="0", padx='5', pady='5', sticky=NSEW)
        subToTrans.grid(row="2", column="0",padx='5', pady='5', sticky=NSEW)

        if self.word != "":
            wordText = super()._label_create(self.word)
            wordText.grid(row="3", column="0", padx='5', pady='5', sticky=N)
            saveWord = super()._button_create(text="保存", bootstyle=DANGER, command = self._saveWord)
            saveWord.grid(row="5", column="0", padx='5', pady='5', sticky=NSEW)

        if self.word != "" and len(self.result["dic"]) == 0 and len(self.result["phrase"]) == 0 :
            s = "<--没有找到解释捏~-->\n\n"
            noText = super()._label_create(s)
            noText.grid(row="4", column="0", padx='5', pady='5', sticky=N)
            return
        exprFrame = Page(self, self.font)
        exprFrame.grid(row="4", column="0", padx='5', pady='5', sticky=NSEW)

        if len(self.result["dic"]) > 0:
            s = "<--词典/翻译:-->\n\n"
            for idx, val in enumerate(self.result["dic"], start=0):
                s += "(" + str(idx+1) + ")\n"
                s += val + "\n"
            dicText = exprFrame._text_create(s)
            dicText.grid(row="1", column="1", padx='5', pady='5', sticky=N)

        if len(self.result["phrase"]) > 0:
            s = "<--短语（含网络派生）:-->\n\n"
            for idx, val in enumerate(self.result["phrase"], start=0):
                s += "(" + str(idx+1) + ")\n"
                s += val + "\n"
            phraseText = exprFrame._text_create(s)
            phraseText.grid(row="1", column="2", padx='5', pady='5', sticky=N)






