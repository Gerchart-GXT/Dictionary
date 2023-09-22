from tools.translate import Translate
from ui.ui import Ui   
from db.db import Db
class Dic:
    def __init__(self):
        self.translator = Translate("en")
        db = Db()
        self.tools = {
            "translator": self.translator,
            "db": db, 
            "tableValue":[]
        }
        ui = Ui(font=("微软雅黑", 14), size="1280x768", tools=self.tools)


if __name__ == "__main__":
    dic = Dic()