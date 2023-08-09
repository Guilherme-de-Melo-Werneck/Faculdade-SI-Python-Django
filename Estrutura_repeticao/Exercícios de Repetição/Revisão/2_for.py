#2) Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.

resultado = 0 #soma ou resultado, tanto faz, você que decide o nome da variável

for num in range(2,501,2):
    resultado = resultado + num

print(f'O resultado da soma dos valores pares é {resultado}')