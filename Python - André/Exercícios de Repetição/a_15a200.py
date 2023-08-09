# Elaborar um programa que apresente como resultado os quadrados dos números inteiros existentes na faixa de 15 a 200

num1 = 15

while num1 <= 200:
    resultado = num1*num1         
    print(f'{num1}² = {resultado}')    
    
    num1 = num1 + 1

# Utilizando For:

for num in range(15, 201):
    resultado = num*num   
    print(f'{num}² = {resultado}')