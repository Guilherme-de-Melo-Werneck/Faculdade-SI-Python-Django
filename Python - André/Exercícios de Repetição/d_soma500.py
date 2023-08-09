# Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.

num = 2
soma = 0

while num <= 500:
    soma = soma + num
    num = num + 2

print(f'A soma dos valores pares é {soma}')