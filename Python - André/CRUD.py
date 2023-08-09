'''Bancos de dados ou bases de dados são conjuntos de arquivos relacionados entre si com registros sobre pessoas, lugares ou coisas. 
São coleções organizadas de dados que se relacionam de forma a criar algum sentido (Informação) e dá mais eficiência durante uma pesquisa ou estudo. 
Crie uma aplicação python que possa gerar um banco de dados em Sqlite3 com o nome de ‘moleza.sqlite’ e um CRUD em uma tabela 
com o nome de ‘pessoas’ com os seguintes campos abaixo:

Campo Tipo de dados

id Chave primária

nome texto

cpf caracter (11)
'''

class MyCrud:
    def __init__(self, banco):
        import sqlite3
        
        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()
    
    def criarTabela(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                CPF CHARACTER(11)
            );
        '''
        self.cursor.execute(sql)
        print('\n> Tabela criada com sucesso!')

    def lerTabela(self):
        sql = '''
            SELECT * FROM pessoas;
        '''

        resultado = self.cursor.execute(sql)
        return resultado.fetchall()
        
    def inserirDados(self, iNome, iCpf):
        sql = '''
            INSERT INTO pessoas (nome, cpf)
            VALUES (?, ?);
        '''
        self.cursor.execute(sql, [iNome, iCpf])
        self.conexao.commit()

        print('\n> Dados inseridos com sucesso!')

    def alterarDados(self, aNome, aCpf, aId):
        sql = '''
            UPDATE pessoas
            SET nome = ?, cpf = ?
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [aNome, aCpf, aId])
        self.conexao.commit()

        print('\n> Atualizado com sucesso!')

    def deletar(self, dId):
        sql = '''
            DELETE FROM pessoas
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [dId])
        self.conexao.commit()

        print('\n> Deletado com sucesso!')

