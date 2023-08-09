'''
 Elaborar um programa que apresente os resultados das potências do valor de base 3, elevado a um expoente que varie do valor 0 até o valor 15. 
 O programa deve apresentar os valores 1, 3, 9. 27, ..., 14.348.907. 
'''

base = 3
resultado = 1

for exp in range(0,16): #aqui o EXP funciona como CONT (contador)
    resultado = resultado * base 
    print(f'{base}^{exp} = {resultado}')