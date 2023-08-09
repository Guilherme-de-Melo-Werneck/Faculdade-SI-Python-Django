from CRUD import MyCrud

my_crud = MyCrud('cliente.sqlite')
my_crud.criarTabela()

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
idade = input('Digite a idade: ')

dados = {
    'tabela': 'clientes',
    'campos': ['nome', 'idade', 'cpf'],
    'valores': [nome, idade, cpf]
}

# dados = {
#     'tabela': 'clientes',
#     'campos': ['nome', 'idade', 'cpf'],
#     'valores': ['ugb', '3333399999-12']
# }

my_crud.inserir(dados)

# my_crud.inserir('Flávio', 20, '197.947.427-32')
# my_crud.alterar('Jose', 32, '222.333.444-32', 1)

# results = my_crud.selecionar()
# for i in results:
#     print(f'Resultados: {i}')

# my_crud.deletar(1)

# results = my_crud.selecionar()
# for i in results:
#     print(f'\nResultados: {i}')

my_crud.fecharDB()
