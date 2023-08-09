import sqlite3

conexao = sqlite3.connect('pessoa.sqlite')
cursor = conexao.cursor()

sql = '''
    SELECT * FROM pessoas
'''

cursor.execute(sql)

resultado = cursor.fetchall()

for i in resultado:
    print(i)

conexao.commit()
conexao.close()