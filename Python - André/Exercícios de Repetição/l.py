# Elaborar um programa que leia 15 valores inteiros e no final apresente o somatório da fatorial de cada valor lido

cont = 0
resultado = 1
soma = 0

for n in range(1, 16):
    cont = cont + 1   
    
    num = int(input(f'Informe o {cont}º número: '))   
    
    resultado = resultado * cont
    soma = soma + resultado

print(f'Resultado é = {soma:,}')

#While

cont = 1
resultado = 1
cont2 = 0

while cont <= 15:
    resultado = resultado * cont
    cont2 = cont2 + 1

    num = int(input(f'Informe o {cont2}º número: '))    
    
    soma = resultado + resultado    
    cont = cont + 1
    
print(f'A soma das fatoriais é = {soma:.1f}')