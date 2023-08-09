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

cursor.execute(sql)
#conexao.commit()

print('Tabela criada!')

conexao.close()
