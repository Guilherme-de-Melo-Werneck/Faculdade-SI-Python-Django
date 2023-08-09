cont = 1
soma = 0

while cont <= 10:
    num = int(input(f'Informe o {cont}º valor: '))
    
    soma = soma + num
    media = soma/10
    cont = cont + 1


print(f'A média dos valores informados é {media}')