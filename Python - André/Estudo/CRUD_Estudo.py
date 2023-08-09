class MyCrud:
    def __init__(self, banco):
        import sqlite3

        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def criarTabela(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS moleza (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome CHARACTER(30),
            idade INTEGER NOT NULL
            );
        '''

        self.cursor.execute(sql)
        print('Tabela criada com sucesso!')

    def fecharDB(self):
        self.conexao.close()

    def lerTabela(self):
        sql = '''
            SELECT * FROM moleza;
        '''

        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    def inserirDados(self, nome, idade):
        sql = '''
            INSERT INTO moleza (nome, idade)
            VALUES (?, ?);
        '''
        
        self.cursor.execute(sql, [nome, idade])
        self.conexao.commit()
        print('Dados inseridos com sucesso!')

    def atualizarTabela(self, nome, idade, id):
        sql = '''
            UPDATE moleza
            SET nome = ?, idade = ?
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [nome, idade, id])
        self.conexao.commit()
        print('Dados atualizados!')


    def deletarTabela(self, id):
        sql = '''
            DELETE FROM moleza
            WHERE id = ?;
        '''

        self.cursor.execute(sql, id)
        self.conexao.commit()
        print('Deletado com sucesso!')

