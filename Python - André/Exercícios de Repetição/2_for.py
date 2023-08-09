# Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.

soma = 0

for num in range(0,501,2):
    soma = soma + num
    
print(f'A soma dos valores pares é = {soma}')


'''
É possível fazer usando o IF:
    
    for num in range (1,501):
        if num % mod 2 == 0:
            soma = soma + num

'''

    
    

