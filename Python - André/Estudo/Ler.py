import sqlite3

conexao = sqlite3.connect('estudo.sqlite')
cursor = conexao.cursor()

#LER

sql = '''
    SELECT * FROM estudos;
'''
cursor.execute(sql)

resultado = cursor.fetchall()

print(resultado)


conexao.commit()
conexao.close()