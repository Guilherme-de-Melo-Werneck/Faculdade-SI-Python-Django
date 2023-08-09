# 4) Escreva um algoritmo que solicite ao usuário informar um número e retorne o quadrado deste número calculado em uma função chamada quadrado(numero).

def quadrado(numero):
    return numero ** 2 #ou num * num

numero = int(input('Informe um número: '))
print(f'{numero}² = {quadrado(numero)}')

