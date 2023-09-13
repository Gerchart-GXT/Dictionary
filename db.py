import sqlite3
from sql import *

class Db:
    def __init__(self):
        try:
            self.dbConnect = sqlite3.connect('dics.db')  # 创建或连接到名为mydatabase.db的SQLite数据库文件
            self.dbConnect.execute("PRAGMA foreign_keys = ON")
            self.cursor = self.dbConnect.cursor()
            self.cursor.execute(dropTmpDic),
            self.cursor.execute(createTmpDic),
            self.cursor.execute(tmpDicTimeStampTrigger),
            self.cursor.execute(createWordListMenu),
            self.cursor.execute(wordListMenuTimeStampTrigger)
            self.cursor.execute(createWordList),
            self.cursor.execute(wordListTimeStampTrigger),
        except Exception as e:
            print(e)
            return
        self.cursor.execute("SELECT * FROM WordListMenu")
        rows = self.cursor.fetchall()  # 获取所有查询结果
        print(rows)
        self.cursor.execute("SELECT * FROM WordList WHERE listId = 100")
        rows = self.cursor.fetchall()  # 获取所有查询结果
        print(rows)
        self.cursor.execute("SELECT * FROM TmpDic")
        rows = self.cursor.fetchall()  # 获取所有查询结果
        print(rows)
    def getWord
    def getWordListMenu(self):
        try:
            self.cursor.execute("SELECT listName, listDiscribe FROM WordListMenu")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return
    def getWordList(self, listName, listDescribe):
        listId = None
        self.cursor.execute(f'''
            SELECT * FROM WordListMenu 
            WHERE listName = {listName}
        ''')
        res = self.cursor.fetchall()
        if len(res) == 0:
            try:
                self.cursor.execute(f'''
                    INSERT INTO WordListMenu (listName, listDiscribe)
                    VALUES ({listName}, {listDescribe});
                '''
                )
            except Exception as e:
                print(e)
                return
        self.cursor.execute(f'''
            SELECT * FROM WordListMenu 
            WHERE listName = {listName}
        ''')
        res = self.cursor.fetchall()
        return res

if __name__ == "__main__":
    db = Db()
    print(db.getWordList("11", "111"))
    print(db.getWordList("22", "111"))
