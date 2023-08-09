# Elaborar um programa que apresente todos os valores númericos divisíveis por 4 e menores que 200

num = 1 

while num < 200:    
    if num % 4 == 0:
        print(f'{num}')
    
    num = num + 1

print('\nOs números acima são divisíveis por 4')