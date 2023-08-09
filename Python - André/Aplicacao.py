from CRUD import MyCrud

My_Crud = MyCrud('moleza.sqlite')
My_Crud.criarTabela()

while True:
    opcoes = input('''
> Digite uma das opções abaixo:
1 - INSERIR DADOS
2 - LER TABELA
3 - ALTERAR DADOS
4 - DELETAR DADOS
5 - SAIR
> ''')

    if opcoes == '1':
        inserir_nome = input('\n> Digite o nome: ')
        inserir_cpf = input('> Digite o CPF: ')
        
        My_Crud.inserirDados(iNome = inserir_nome, iCpf = inserir_cpf)
   
    elif opcoes == '2':
        ler_tabela = (f'\nDados da Tabela: {My_Crud.lerTabela()}')
        print(ler_tabela)
    
    elif opcoes == '3':
        alterar_id = input('\n> Digite o ID a ser alterado: ')
        alterar_nome = input('> Digite o nome: ')
        alterar_cpf = input('> Digite o CPF: ')
        
        My_Crud.alterarDados(aNome = alterar_nome, aCpf = alterar_cpf, aId= alterar_id)
    
    elif opcoes == '4':
        delete_id = input('\n> Digite o ID a ser deletado: ')

        My_Crud.deletar(dId = delete_id)
    
    else:
        print('> Finalizando...')
        My_Crud.fecharDB()
        break




