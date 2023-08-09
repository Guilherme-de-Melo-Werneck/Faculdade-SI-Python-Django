class MyCrud:
    def __init__(self, banco):
        import sqlite3

        self.conexao = sqlite3.connect(banco)
        self.cursor = self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close()

    def criarTabela(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                cpf TEXT NOT NULL
            );
        '''
        
        self.cursor.execute(sql)

        print('\n> Tabela criada\n')
    
    def selecionar(self):
        sql = '''
            SELECT * FROM clientes;
        '''
        
        resultados = self.cursor.execute(sql)
        return resultados.fetchall()

    def inserir(self, dados):
        print('Dados: ', dados)
        
        valores = '('
        campos = '('
        for i in dados['campos']:
            campos = campos + f'{i}, '
            valores = valores + '?, '
            
        valores = f'{valores[:-2]})'
        campos = f'{campos[:-2]})'
        print(f'Campos: {campos}')       

        sql = f'''
            INSERT INTO {dados['tabela']} {campos}
            VALUES {valores};
        '''

        print(f'SQL: {sql}')
        self.cursor.execute(sql, dados['valores'])

        # sql = '''
        #     INSERT INTO clientes (nome, idade, cpf)
        #     VALUES (?, ?, ?);
        # '''

        # self.cursor.execute(sql, [iNome, iIdade, iCpf])
        self.conexao.commit()

        print('> Salvo com sucesso!')

    def alterar(self, aNome, aCpf, aIdade, aId):
        sql = '''
            UPDATE clientes
            SET nome = ?, cpf = ?, idade = ?
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [aNome, aCpf, aIdade, aId])
        self.conexao.commit()

        print('\n> Alterado com sucesso!')

    def deletar(self, dId):
        sql = '''
            DELETE FROM clientes
            WHERE id = ?;
        '''

        self.cursor.execute(sql, [dId])
        self.conexao.commit()
        
        print('\n> Deletado com sucesso!')

# results = MyCrud.selecionar()
# print(f'\n> Resultado: {results}')
# MyCrud.deletar(3)



