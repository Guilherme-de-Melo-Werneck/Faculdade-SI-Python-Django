import sqlite3

conexao = sqlite3.connect('estudo.sqlite')
cursor = conexao.cursor()

#DELETE

deletar = input('Digite o ID a ser deletado: ')

sql = '''
    DELETE from estudos
    WHERE id = ?;
'''

cursor.execute(sql, deletar)
conexao.commit()
conexao.close()
