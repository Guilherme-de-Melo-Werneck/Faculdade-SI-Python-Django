'''
Elaborar um programa que apresente os resultados das potências do valor de base 3, elevado a um expoente que varie do valor 0 até o valor 15. 
O programa deve apresentar os valores 1, 3, 9. 27, ..., 14.348.907.
'''

base = 3
cont = 0

while cont <= 15:
    resultado = base ** cont            
    print(f'{base} elevado a {cont} = {resultado}')      
    
    cont = cont + 1
