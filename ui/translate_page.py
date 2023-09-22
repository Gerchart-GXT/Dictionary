from .page import Page
import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
import json

class TranslatePage(Page):
    def __init__(self:Page, root, font, tools):
        super().__init__(root, font)

        self.translator = tools["translator"]
        self.db = tools["db"]
        self.word = ""
        self.font = font
        self.result = {"dic": [], "phrase": []}
        self.isCN = 0
        self._tip_area = []

        self._widgets = []
        self._render()

    def _translate(self, word):
        if word == "":
            return
        result = self.translator.trans_from_youdaodic(word)
        self.isCN, self.result = result
        self.word = word
        self.tip = []
        expr = {
            "dic": self.result["dic"],
            "phrase": self.result["phrase"],
            "tip": []
        }
        self.db.insert_history(self.word, json.dumps(expr).replace("'", "''"), self.isCN, 0)
        self._render()
    
    def _saveWord(self):
        expr = {
            "dic": self.result["dic"],
            "phrase": self.result["phrase"],
            "tip": [tip[0].get() for tip in self._tip_area]
        }
        self.db.save_history(self.word, json.dumps(expr).replace("'", "''"))
        self.db.get_allhistory()

    def _tip_delete(self, tipInput, tipDelete):
        super()._remove_widget(tipInput)
        super()._remove_widget(tipDelete)
        self._tip_area.remove((tipInput, tipDelete))
        self._render()

    def _tip_input(self):
        tipInput = super()._input_create()
        tipDelete = super()._button_create(text="删除", bootstyle=SUCCESS,command = lambda : self._tip_delete(tipInput, tipDelete))
        self._tip_area.append((tipInput, tipDelete))
        self._render()


    def _render(self):
        super()._clear_widget(self._widgets)
        rowIdx = 1

        inputArea = super()._input_create()
        self._widgets.append(inputArea)
        inputArea.grid(row=rowIdx, columnspan="12", padx='5', pady='5', sticky=NSEW)

        subToTrans = super()._button_create(text="翻译", bootstyle=SUCCESS,command = lambda : self._translate(inputArea.get()))
        self._widgets.append(subToTrans)
        subToTrans.grid(row=rowIdx + 1, columnspan="12",padx='5', pady='5', sticky=NSEW)

        if self.word != "":
            wordText = super()._label_create(self.word)
            self._widgets.append(wordText)
            wordText.grid(row=rowIdx + 3, columnspan="12", padx='5', pady='5', sticky=N)

            if len(self.result["dic"]) == 0 and len(self.result["phrase"]) == 0 :
                s = "<--没有找到解释捏~-->\n\n"
                noText = super()._label_create(s)
                self._widgets.append(noText)
                noText.grid(row=rowIdx + 4, columnspan="12", padx='5', pady='5', sticky=N)
            else:
                exprFrame = Page(self, self.font)
                self._widgets.append(exprFrame)
                exprFrame.grid(row=rowIdx + 4, columnspan="12", padx='5', pady='5', sticky=NSEW)

                if len(self.result["dic"]) > 0:
                    s = "<--词典/翻译:-->\n\n"
                    for idx, val in enumerate(self.result["dic"], start=0):
                        s += "(" + str(idx+1) + ")\n"
                        s += str(val) + '\n'
                    dicText = exprFrame._text_create(s)
                    dicText.grid(row="1", column="0", columnspan="6", padx='5', pady='5', sticky=W)

                if len(self.result["phrase"]) > 0:
                    s = "<--短语（含网络派生）:-->\n\n"
                    for idx, val in enumerate(self.result["phrase"], start=0):
                        s += "(" + str(idx+1) + ")\n"
                        s += str(val) + "\n"
                    phraseText = exprFrame._text_create(s)
                    phraseText.grid(row="1", column="6", columnspan="6", padx='5', pady='5', sticky=E)

            for idx, tip in enumerate(self._tip_area, start = 0):
                tip[0].grid(row=rowIdx + 5 + idx, column="0",columnspan="10", padx='5', pady='5', sticky=NSEW)
                tip[1].grid(row=rowIdx + 5 + idx, column="10", columnspan="2", padx='5', pady='5', sticky=NSEW)
            print(len(self._tip_area))

            addTip = super()._button_create(text="新建注释", bootstyle=INFO, command = self._tip_input)
            self._widgets.append(addTip)
            addTip.grid(row=rowIdx + 5 + len(self._tip_area), columnspan="12", padx='5', pady='5', sticky=NSEW)

            saveWord = super()._button_create(text="保存", bootstyle=DANGER, command = self._saveWord)
            self._widgets.append(saveWord)
            saveWord.grid(row=rowIdx + 6 + len(self._tip_area), columnspan="12", padx='5', pady='5', sticky=NSEW)





