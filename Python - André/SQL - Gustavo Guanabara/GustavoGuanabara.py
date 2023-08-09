import sqlite3

#Criando uma Tabela

conexao = sqlite3.connect('pessoa.sqlite')
cursor = conexao.cursor()

sql = '''
    CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    sexo TEXT,
    peso FLOAT,
    altura FLOAT,
    nacionalidade TEXT DEFAULT 'Brasil'
    );
'''
#Adicionando Itens à Tabela

p_nome = 'Flávio'
p_idade = 20
p_sexo = 'Masculino'
p_peso = 70.0
p_altura = 1.83
p_nacionalidade = 'Brasil'

sql = '''
    INSERT INTO pessoas (nome, idade, sexo, peso, altura, nacionalidade)
    VALUES (?, ?, ?, ?, ?, ?);
'''
#Posso também colocar os valores diretamente: VALUES('Flávio', '20', 'Masculino'...)

parametro = (p_nome, p_idade, p_sexo, p_peso, p_altura, p_nacionalidade)

cursor.execute(sql, parametro)
conexao.commit()
print('Tabela criada!')
print('Dados inseridos na tabela')

conexao.close()

