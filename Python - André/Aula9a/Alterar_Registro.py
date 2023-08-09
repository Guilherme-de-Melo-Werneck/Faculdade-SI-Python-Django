import sqlite3

conexao = sqlite3.connect('cliente.sqlite')
cursor = conexao.cursor()

a_nome = 'Lais'
a_idade = '20'

p_id = 2

sql = '''
    UPDATE clientes
    set nome = ?, idade = ?
    WHERE id = ?;
'''
# É possível não usar o parâmetro, pode utilizar direto no execute
parametro = [a_nome, a_idade, p_id]

cursor.execute(sql, parametro)
conexao.commit() # <- ROLLBACK - Função de proteção (salva os comandos)

print('> Alterado com sucesso!')

conexao.close()
