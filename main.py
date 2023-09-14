import sys
sys.path.append("./ui")
sys.path.append("./db")
from tools.translate import Translate
from ui import Ui   
from db import Db

class Dic:
    def __init__(self):
        db = Db()
        self.translator = Translate("en")
        self.tools = {
            "_translator": self.translator,
            "_db": db
        }
        ui = Ui(font=("微软雅黑", 14), size="600x600", tools = self.tools)


if __name__ == "__main__":
    dic = Dic()