'''
Escrever um programa que apresente como resultado a potência de uma base qualquer elevada a um expoente qualquer
'''

base = int(input('Digite o número da base: ')) 
exp = int(input('Digite o número do expoente: '))
cont = 0

while base <= exp:
    resultado = base ** exp  
    print(f'{base}^{exp} = {resultado}')           
    
    base = base + 1






