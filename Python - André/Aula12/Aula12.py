from CRUD_FireBase import CrudFirebase

crud = CrudFirebase()

while True:
    print('''
    Escolha uma opção:
    1 - Incluir
    2 - Ler
    3 - Alterar
    4 - Deletar
    5 - Sair
    ''')

    valor = input('> ')
    if valor == '1':
        chave = input('Digite a chave: ')
        nome = input('Digite o seu nome: ')
        comida = input('Digite a sua comida preferida: ')
        dados = {
            'Nome': nome,
            'Comida': comida
        }
        crud.incluirDB(chave, dados)
    
    elif valor == '2':
        chave = input('Qual o valor da chave: ')
        resultados = crud.lerDB(chave)

        for resultado in resultados:
            print(resultado.key())
            print(resultado.val())

    elif valor == '3':
        chave = input('Qual o valor da chave: ')
        nome = input('Digite o seu nome: ')
        comida = input('Digite a sua comida preferida: ')
        dados = {
            'Nome': nome,
            'Comida': comida
        }
        crud.alterarDB(chave, dados)

    elif valor == '4':
        chave = input('Qual o valor da chave: ')
        crud.deleteDB(chave)
    
    else:
        break
