import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

p_nome = 'Flávio'
p_idade = 20

sql = '''
    INSERT INTO clientes (nome, idade)
    VALUES (?, ?);
'''

parametro = (p_nome, p_idade)

cursor.execute(sql, parametro)
conexao.commit()

print('> Salvo com sucesso!')

conexao.close()