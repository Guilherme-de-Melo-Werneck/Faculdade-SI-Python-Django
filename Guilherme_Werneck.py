#Construa um algoritmo de votação para a Prefeitura Municipal de Volta
#Redonda. Os votos serão computados da seguinte maneira:
#-1 - sair
#0 - branco
#1 - Samuca
#2 - Neto
#3 - Baltazar
#>=4 - Nulo
#A saída deverá ser:
# O número do candidato vencedor
# O número de votos em branco
# O número de votos nulos
# o número de eleitores

#Nome: Guilherme de Melo Werneck
#Matrícula: 2022101349

from rich import print

VOTOS_SAMUCA = 0 
VOTOS_NETO = 0
VOTOS_BALTAZAR = 0
VOTOS_NULO = 0
VOTOS_BRANCO = 0

while True:
    print('-'*30)
    print(f' [on white]TOTAL BRANCO:[/] {VOTOS_BRANCO} \n [on red]TOTAL NULO:[/] {VOTOS_NULO} \n [on blue]TOTAL SAMUCA:[/] {VOTOS_SAMUCA} \n [on yellow]TOTAL NETO:[/] {VOTOS_NETO} \n [on purple]TOTAL BALTAZAR:[/] {VOTOS_BALTAZAR} ')
    print('-'*30)

    voto = int (input(f'OPÇÕES DE VOTOS \n  0 - BRANCO \n >=4 - NULO \n  2 - SAMUCA \n  3 - NETO \n  4 - BALTAZAR \n -1 - PARA SAIR \n\nSEU VOTO: '))
    if voto == -1:
        break
    elif voto == 0:
        VOTOS_BRANCO = VOTOS_BRANCO + 1
    elif voto >=4:
        VOTOS_NULO = VOTOS_NULO + 1
    elif voto == 1:
        VOTOS_SAMUCA = VOTOS_SAMUCA + 1
    elif voto == 2:
        VOTOS_NETO = VOTOS_NETO + 1
    elif voto == 3:
        VOTOS_BALTAZAR = VOTOS_BALTAZAR +1
    else:
        pass
    
    

print('\nSão [on blue]3[/] candidatos participando dessa eleição')
print(f'\nNúmero de votos BRANCO: [on white]{VOTOS_BRANCO}[/] ')
print(f'\nNúmero de votos NULOS: [on red]{VOTOS_NULO}[/] ')

NT= VOTOS_BRANCO + VOTOS_NULO + VOTOS_SAMUCA + VOTOS_NETO + VOTOS_BALTAZAR
print(f'\nNúmero total de ELEITORES: [on blue]{NT}[/]')

vencedor=0
if VOTOS_SAMUCA > VOTOS_NETO and VOTOS_SAMUCA > VOTOS_BALTAZAR:
    vencedor = VOTOS_SAMUCA
    print(f'\n[on green]VENCEDOR FOI O CANDIDATO SAMUCA COM {vencedor} VOTOS[/]')
elif VOTOS_NETO > VOTOS_SAMUCA and VOTOS_NETO > VOTOS_BALTAZAR:
    vencedor = VOTOS_NETO
    print(f'\n[on green]VENCEDOR FOI O CANDIDATO NETO COM {vencedor} VOTOS[/]')
elif VOTOS_BALTAZAR > VOTOS_NETO and VOTOS_BALTAZAR > VOTOS_SAMUCA:
    vencedor = VOTOS_BALTAZAR
    print(f'\n[on green]VENCEDOR FOI CANDIDATO BALTAZAR COM {vencedor} VOTOS[/] ')
elif vencedor == vencedor:
    print(f'\nEMPATE ENTRE OS CANDIDATOS, PRECISARÁ DO [on green]SEGUNDO TURNO[/]')
else:
    print('\n[on red]MUITO VOTOS NULOS E BRANCO, REINICIE O CÓDIGO[/]')