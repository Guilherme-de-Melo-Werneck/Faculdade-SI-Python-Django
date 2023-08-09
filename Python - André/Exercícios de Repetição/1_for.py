#1) Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+...+98+99+100)

soma = 0
num = 1

for num in range (1,101):
    soma = soma + num

print(f'O resultado da soma é {soma}')