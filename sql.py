dropTmpDic = '''
    DROP TABLE IF EXISTS TmpDic
'''
createTmpDic = ''' 
    CREATE TABLE IF NOT EXISTS TmpDic(
        wordId INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE,
        expr TEXT,
        saveTime DATETIME,
        isCN TEXT
    )
'''

tmpDicTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS tmpDicTimeStamp
    AFTER INSERT ON tmpDic
    BEGIN
        UPDATE tmpDic SET saveTime = DATETIME('NOW') WHERE wordId = new.wordId;
    END;
'''

createWordListMenu= '''
    CREATE TABLE IF NOT EXISTS WordListMenu(
        listId INTEGER PRIMARY KEY AUTOINCREMENT,
        listName TEXT UNIQUE,
        saveTime DATETIME,
        listDiscribe TEXT
    )
'''
wordListMenuTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS wordListMenuTimeStampTrigger
    AFTER INSERT ON WordListMenu
    BEGIN
        UPDATE WordListMenu SET saveTime = DATETIME('NOW') WHERE listId = new.listId;
    END;
'''

createWordList = '''
    CREATE TABLE IF NOT EXISTS WordList(
        wordId INTEGER PRIMARY KEY AUTOINCREMENT,
        listId INTEGER,
        word TEXT UNIQUE,
        expr TEXT,
        saveTime DATETIME,
        isCN TEXT,

        FOREIGN KEY (listId) REFERENCES WordListMenu(listId)
        ON DELETE CASCADE
        ON UPDATE NO ACTION
    )
'''
wordListTimeStampTrigger = '''
    CREATE TRIGGER IF NOT EXISTS wordListTimeStampTrigger
    AFTER INSERT ON WordList
    BEGIN
        UPDATE WordList SET saveTime = DATETIME('NOW') WHERE wordId = new.wordId;
    END;
'''