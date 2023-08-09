import sqlite3

conexao = sqlite3.connect('estudo.sqlite')
cursor = conexao.cursor()

#ALTERAR

id = input('Digite o ID: ')
nome = input('Digite o nome: ')
idade = input('Digite a idade: ')

sql = '''
    UPDATE estudos
    SET nome = ?, idade = ?
    WHERE id = ?;
'''
cursor.execute(sql, [nome, idade, id])
conexao.commit()
conexao.close()