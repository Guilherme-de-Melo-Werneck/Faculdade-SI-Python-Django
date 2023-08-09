'''Construa um algoritmo de votação para a Prefeitura Municipal de Volta
Redonda. Os votos serão computados da seguinte maneira:
-1 - sair
0 - branco
1 - Samuca
2 - Neto
3 - Baltazar
>=4 - Nulo
A saída deverá ser:
+ O número do candidato vencedor
+ O número de votos em branco
+ O número de votos nulos
+ o número de eleitores
'''

votos = []
cont_eleitores = 0
cont_nulos = 0

while True:
    opcoes = int(input('''
Informe o número do seu candidato:
0 - Branco  
1 - Samuca  
2 - Neto  
3 - Baltazar  
4 - Nulo 
-1 - Sair
> '''))

    if opcoes <= -1:
        break
    elif opcoes >= 4:
        cont_nulos = cont_nulos + 1

    votos.append(opcoes)
    print(f'Votos: {votos}')

    Samuca = (votos.count(1))
    Neto = (votos.count(2))
    Baltazar = (votos.count(3))
    brancos = (votos.count(0))
    nulos = cont_nulos
    cont_eleitores = cont_eleitores + 1

print('-' * len(votos * 4))
print(f'\nVotos: {votos}')
print(f'''
Votos em branco: {brancos}
Votos nulos: {nulos}
Total de eleitores: {cont_eleitores}
''')
print('-'*len(votos*4))

#print(f'A quantidade de eleitores foi {len(votos)}')

if Samuca > Neto and Samuca > Baltazar:
    print('O vencedor é o candidato 1 (Samuca)!')

elif Neto > Samuca and Neto > Baltazar:
    print('O vencedor é o candidato 2 (Neto)!')

elif Baltazar > Neto and Baltazar > Samuca:
    print('O vencedor é o candidato 3 (Baltazar)!')

elif nulos > Samuca and nulos > Neto and nulos > Baltazar and nulos > brancos:
    print('Todos os votos foram nulos, portanto não houve vencedor.')

elif brancos > Samuca and brancos > Neto and brancos > Baltazar and brancos > nulos:
    print('Todos os votos foram brancos, portanto não houve vencedor.')
    
else:
    print('Houve um empate nas eleições! Necessário segundo turno.')