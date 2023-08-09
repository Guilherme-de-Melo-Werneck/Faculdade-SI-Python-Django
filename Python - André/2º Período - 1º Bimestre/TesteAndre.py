# faturamento=0
# lista= []
# while True:
#     print("para sair, digite sair")
#     produtos= input('Insira o nome do produto: ')      
#     if produtos.upper()=='SAIR':
#         break
#     preços= []
#     quantidades= []
#     preço = float(input('Insira o preço do produto: '))
#     print(f'{preço} reais')
#     quantidade = int(input("Insira a quantidade de produtos: "))
#     print(f'{quantidade}')

    
#     preços.append(preço)
#     quantidades.append(quantidade)
#     registro = (produtos, preço, quantidade)
#     lista.append(registro)
    

# if 'sair':
#    print(f'Os produtos, seus respectivos preços e quantidades são  {lista}')

# faturamento = 0 

# for i in lista:
#  faturamento = faturamento+ (i[1] * i[2])
# print(f' O faturamento dos produtos foi {faturamento}')

num = float(input('Digite um valor: '))

if num == 1:
    print('Número par!')
elif num == 0:
    print('Zero!')
else:
    print('Número ímpar')