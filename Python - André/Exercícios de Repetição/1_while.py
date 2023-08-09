#1) Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+...+98+99+100)

num = 1
soma = 0

while num <= 100:
    soma = soma + num
    num = num + 1

print(f'O resultado da soma é {soma}')