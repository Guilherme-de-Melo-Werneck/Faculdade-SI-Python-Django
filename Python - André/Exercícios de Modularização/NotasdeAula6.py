'''
Altere o programa anterior para que o usuário informe a temperatura e a escala que deseja converter. 
O valor será calculado pela função convTemp(temp, escala). Dica: a escala informada deverá ser uma letra 'c' – Celsius / 'f' – fahrenheit.

'''

def convTemp(temp, escala):
    if escala == 'C':
        return temp * 1.8 + 32
    elif escala == 'F':
        return (temp - 32)/ 1.8

escala = str(input('Digite a escala desejada (C ou F): '))
temp = float(input('Digite a temperatura desejada: '))

print(f'A temperatura {temp}° convertida para {escala} é {convTemp(temp, escala)}') 



