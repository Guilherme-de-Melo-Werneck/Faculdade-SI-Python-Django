import sqlite3

conexao = sqlite3.connect('estudo.sqlite')
cursor = conexao.cursor()

#CRIAR

sql = '''
    CREATE TABLE IF NOT EXISTS estudos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome CHAR(30) NOT NULL,
        idade INTEGER NOT NULL
    );
'''

cursor.execute(sql)
conexao.close()

