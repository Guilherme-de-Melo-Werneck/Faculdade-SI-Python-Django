'''Criar um algoritmo capaz de calcular o faturamento de uma lista de 
produtos com suas respectivas quantidades e preço.
Verifique a entrada dos produtos, ao digitar sair a captação se encerra.
Calcular o faturamento com a equação: 
 faturamento = faturamento + (quantidade * preço)
Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis 
quantidade e preço'''

lst_produtos = []

while True:
    produto = input('Para sair, digite sair \nDigite o produto: ')
    print() #Print vazio para pular linha
    if produto.upper() == 'SAIR':
        break
    
    lst_preco = []
    preco = float(input('Para sair, digite -1 \nDigite o preço do produto: R$ '))
    print() #Print vazio para pular linha
    if preco == -1:
        break  
    lst_preco.append(preco)

    lst_quantidade = []
    qtd = int(input(f'Para sair, digite -1 \nDigite a quantidade desejada do produto: '))
    print() #Print vazio para pular linha
    if qtd == -1:
        break
    lst_quantidade.append(qtd)

    registro = (produto, preco, qtd)
    lst_produtos.append(registro)

print(f'Lista de Produtos: {lst_produtos}')

faturamento = 0

for produtos in lst_produtos:
    print(f'''
Produto: {produtos[0]}
Valor: R$: {produtos[1]}
Quantidade: {produtos[2]} unidades
''')

    faturamento = faturamento + (produtos[1] * produtos[2])

print(f'O faturamento dos produtos foi R${faturamento}')
    
