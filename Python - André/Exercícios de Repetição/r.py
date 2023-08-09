# Elaborar um programa que leia valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser apresentados o maior e menor valor informados pelo usuário.

num = 0
cont = 0
maior = 0
menor = 0

while num >= 0:
    cont = cont + 1
    num2 = int(input(f'Digite o {cont}º valor: '))           
    
    num = num + 1
    
    if num2 > maior:
        maior = num2
    elif num2 < 0:
        menor = num2
        break

print(f'O maior número é {maior} e o menor é {menor}')