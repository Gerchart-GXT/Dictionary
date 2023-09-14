import sqlite3
from sql import *

class Db:
    def __init__(self):
        try:
            self.dbConnect = sqlite3.connect('./dics.db')
            self.dbConnect.execute("PRAGMA foreign_keys = ON")
            self.cursor = self.dbConnect.cursor()
            self.cursor.execute(DropHistoryWord),
            self.cursor.execute(CreateHistoryWord),
            self.cursor.execute(HistoryWordTimeStampTrigger),
            self.cursor.execute(CreateListMenu),
            self.cursor.execute(ListMenuTimeStampTrigger)
            self.cursor.execute(CreateAllWords),
            self.cursor.execute(AllWordsTimeStampTrigger),
        except Exception as e:
            print(e)
            return
        
    def runSQL(self, sql):
        try:

            self.cursor.execute(sql)
            return (True, self.cursor.fetchall())
        except Exception as e:
            return (False, e)
        
    def get_word(self, word):
        return self.runSQL(f'''SELECT * FROM AllWords WHERE word = "{word}"''')

    def get_allwords(self):
        return self.runSQL(f'''SELECT * FROM AllWords''')
    
    def insert_word(self, listId, word, expr, isCN):
        return self.runSQL(f'''INSERT INTO AllWords (listId, word, expr, isCN) VALUES("{listId}", "{word}", "{expr}", "{isCN}")''')

    def delete_word(self, wordId):
        return self.runSQL(f'''DELETE FROM AllWords WHERE wordId = "{wordId}"''')

    def get_list(self, listName, listDescribe):
        return self.runSQL(f'''SELECT * FROM ListMenu WHERE listName = "{listName}"''')

    def create_list(self, listName, listDescribe):
        return self.runSQL(f'''INSERT INTO ListMenu (listName, listDescribe) VALUES ("{listName}", "{listDescribe}")''')
    
    def delete_list(self, listId):
        return self.runSQL(f'''DELETE FROM ListMenu WHERE listId = "{listId}"''')
    
    def get_listMenu(self):
        return self.runSQL(f'''SELECT * FROM ListMenu''')
    
    def get_listword(self, listId):
        return self.runSQL(f'''SELECT * FROM AllWords WHERE listId = "{listId}"''')

    def insert_history(self, word, expr, isCN, isSave):
        return self.runSQL(f'''INSERT INTO HistoryWord (word, expr, isCN, isSaved) VALUES("{word}", "{expr}", "{isCN}", "{isSave}")''')

    def delete_history(self, word):
        return self.runSQL(f'''DELETE FROM HistoryWord WHERE word = "{word}"''')

    def get_allhistory(self):
        return self.runSQL(f'''SELECT * FROM HistoryWord''')

    def get_history_word(self, word):
        return self.runSQL(f'''SELECT * FROM HistoryWord WHERE word = "{word}"''')

    def get_history_saved(self):
        return self.runSQL('''SELECT * FROM HistoryWord WHERE isSaved = "1"''')

    