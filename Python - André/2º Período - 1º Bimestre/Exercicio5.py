'''Faça uma função que recebe um valor inteiro e verifica se o valor é
par ou ímpar. A função deve retornar um valor booleano.'''

def parouimpar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

valores = [-1, 2, 3, 4, 5, 6]

for valor in valores:
    print(valor, parouimpar(valor))






