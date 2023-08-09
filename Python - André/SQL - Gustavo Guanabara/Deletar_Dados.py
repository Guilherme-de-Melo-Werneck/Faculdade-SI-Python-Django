import sqlite3

conexao = sqlite3.connect('pessoa.sqlite')
cursor = conexao.cursor()

delete_id = input('Digite o ID a ser deletado: ')

sql = '''
    DELETE FROM pessoas
    WHERE id =?;
'''

parametro = delete_id

cursor.execute(sql, parametro)

print('> Deletado com sucesso!')

conexao.commit()
conexao.close()