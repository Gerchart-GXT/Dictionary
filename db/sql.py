DropHistoryWord = '''
    DROP TABLE IF EXISTS HistoryWord
'''
CreateHistoryWord = ''' 
    CREATE TABLE IF NOT EXISTS HistoryWord(
        wordId INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        expr TEXT,
        saveTime DATETIME,
        isCN INTEGER CHECK (isCN IN (0, 1)),
        isSaved INTEGER CHECK (isCN IN (0, 1))
    )
'''

HistoryWordTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS HistoryWordTimeStamp
    AFTER INSERT ON HistoryWord
    BEGIN
        UPDATE HistoryWord SET saveTime = DATETIME('NOW') WHERE wordId = new.wordId;
    END;
'''

CreateListMenu= '''
    CREATE TABLE IF NOT EXISTS ListMenu(
        listId INTEGER PRIMARY KEY AUTOINCREMENT,
        listName TEXT UNIQUE,
        saveTime DATETIME,
        listDescribe TEXT
    )
'''
ListMenuTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS ListMenuTimeStampTrigger
    AFTER INSERT ON ListMenu
    BEGIN
        UPDATE ListMenu SET saveTime = DATETIME('NOW') WHERE listId = new.listId;
    END;
'''

CreateAllWords = '''
    CREATE TABLE IF NOT EXISTS AllWords(
        wordId INTEGER PRIMARY KEY AUTOINCREMENT,
        listId INTEGER,
        word TEXT UNIQUE,
        expr TEXT,
        saveTime DATETIME,
        isCN INTEGER CHECK (isCN IN (0, 1)),

        FOREIGN KEY (listId) REFERENCES ListMenu(listId)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    )
'''
AllWordsTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS AllWordsTimeStampTrigger
    AFTER INSERT ON AllWords
    BEGIN
        UPDATE AllWords SET saveTime = DATETIME('NOW') WHERE wordId = new.wordId;
    END;
'''