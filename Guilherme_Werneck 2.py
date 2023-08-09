#Criar um algoritmo capaz de calcular o faturamento de uma lista de
#produtos com suas respectivas quantidades e preço.
#Verifique a entrada dos produtos, ao digitar sair a captação se encerra.
#Calcular o faturamento com a equação:
#faturamento = faturamento + (quantidade * preço)
#Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis
#quantidade e preço

#Guilherme de melo Werneck
#2022101349

from rich import print

faturamento = 0
lst= []
while True:
    print('\n[on red] PARA FINALIZAR, DIGITE "SAIR"[/]')
    produtos= input('\nDIGITE O NOME DO PRODUTO: ')      
    if produtos.upper()=='SAIR':
        break
    
    quantidades= []
    quantidade = int(input('\nDIGITE A QUANTIDADE DE PRODUTOS: '))
    print(f'[on blue]{quantidade} UN[/]')
    quantidades.append(quantidade)

    valores= []
    valor = float(input(f'\nDIGITE O PREÇO DO PRODUTO: '))
    print(f'[on green]R${valor}[/]')
    valores.append(valor)
   
    registro = (produtos, valor, quantidade)
    lst.append(registro)
    

for i in lst:
 faturamento = faturamento + ((i[1]) * (i[2]))
print(f'\nPRODUTO, VALOR E SUAS QUANTIDADES RESPECTIVAMENTE SÃO: [on white]{lst}[/]')

print(f'\nO FATURAMENTOS DOS PRODUTOS FOI: [on green]R${faturamento}[/]')