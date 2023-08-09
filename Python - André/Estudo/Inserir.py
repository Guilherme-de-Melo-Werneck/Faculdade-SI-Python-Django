import sqlite3

conexao = sqlite3.connect('estudo.sqlite')
cursor = conexao.cursor()

#INSERIR

nome = input('Digite o nome: ')
idade = input('Digite a idade: ')

sql = '''
    INSERT INTO estudos (nome, idade)
    VALUES (?, ?);
'''
parametro = nome, idade

cursor.execute(sql, parametro)
conexao.commit()
conexao.close()
