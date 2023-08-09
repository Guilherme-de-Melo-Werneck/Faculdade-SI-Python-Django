import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

sql = '''
    SELECT * FROM clientes;
'''

cursor.execute(sql)

resultado = cursor.fetchall()

for i in resultado:
    print(i)

conexao.close()
