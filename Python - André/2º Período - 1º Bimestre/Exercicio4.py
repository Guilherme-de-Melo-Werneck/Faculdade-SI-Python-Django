'''Faça uma função que recebe um valor inteiro e verifica se o valor é
positivo ou negativo. A função deve retornar um valor booleano.'''

def positivoNegativo(valor):
    if valor < 0:
        return False
    elif valor > 0:
        return True
    else:
        return None

valores = [-1, 2, 3, 4, 5, 6]

for valor in valores:
    print(valor, positivoNegativo(valor))

positivonegativo = positivoNegativo(2)
print(positivonegativo)