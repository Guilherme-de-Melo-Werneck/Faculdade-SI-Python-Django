# Elaborar um programa que apresente a tabuada de um número qualquer, e deve ser representado de forma tradicional

num1 = int(input('Informe um número: '))
num2 = 1

while num2 <= 10:
    resultado = num1*num2      
    print(f'{num1} x {num2} = {resultado} ')    
    
    num2 = num2 + 1
