import sqlite3

conexao = sqlite3.connect('pessoa.sqlite')
cursor = conexao.cursor()

#Adicionando Itens à Tabela

p_nome = 'Lais'
p_idade = 21
p_sexo = 'Feminino'
p_peso = 73.0
p_altura = 1.76
p_nacionalidade = 'Brasil'

sql = '''
    INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade)
    VALUES (?, ?, ?, ?, ?, ?);

'''
#Posso também colocar os valores diretamente: VALUES('Flávio', '20', 'Masculino'...)

parametro = (p_nome, p_idade, p_sexo, p_peso, p_altura, p_nacionalidade)

cursor.execute(sql, parametro)
conexao.commit()

print('Dados inseridos na tabela')

conexao.close()