# Elaborar um programa que apresente todos os valores númericos ímpares na faixa de 0 a 20

num = 1

while num <= 20:    
    if num % 2 == 0:
        pass   
    else:
        print(f'{num}')
 
    num = num + 1

print ('\nOs números acima são ímpares e estão na faixa de 1 até 20')