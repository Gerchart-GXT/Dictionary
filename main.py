from translate import Translate
from excelModel import HandleExcel

class Dic:
    def __init__(self, lang, fileName):
        self.translator = Translate(lang)
        # self.filePath = input()
        self.data = HandleExcel(fileName)
        self.nowSheet = "Sheet1"
    def search(self, word):
        return self.translator.trans_from_youdaodic(word)
    
    def add_item(self, word, result):
        self.data._write_sheet(self.nowSheet, [word])
        self.data._write_sheet(self.nowSheet, result["dic"])
        self.data._write_sheet(self.nowSheet, result["phrase"])


def main():
    dic = Dic("en", "test.xlsx")
    word = input()
    res = dic.search(word)
    for r in res:
        dic.add_item(word, res)
    # dic.data._save()
    # print(dic.data._read_sheet("Sheet1"))

if __name__ == "__main__":
    main()
    
    