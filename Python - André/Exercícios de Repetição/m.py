# Elaborar um programa que leia 10 valores númericos reais e apresente no final o somatório e a média dos valores lidos.

cont = 0
soma = 0

for n in range(1,11):
    cont = cont + 1       
    n = float(input(f'Informe o {cont}º número: '))   
    
    soma = soma + n
    media = (soma)/10

# Para pular linha, pode-se usar o \n antes do início, ou simplesmente usar um print() na linha de cima

print(f'\nA soma dos valores informados é {soma} \nA média é {media}')

