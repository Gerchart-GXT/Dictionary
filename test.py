import sqlite3
conn = sqlite3.connect('mydatabase.db')  # 创建或连接到名为mydatabase.db的SQLite数据库文件
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT)''')
cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", ('John Doe', 'HR'))
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()  # 获取所有查询结果
for row in rows:
    print(row)
