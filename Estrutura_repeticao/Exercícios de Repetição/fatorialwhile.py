#

num = int(input('Informe um número: '))
cont = 1
resultado = 1

while cont <= num:
    resultado = resultado * cont
    cont = cont + 1

print(f'{num}! = {resultado}')
