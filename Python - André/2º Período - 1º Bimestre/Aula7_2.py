# notas_alunos = [
#     [3, 5, 6],
#     [4, 2, 9],
#     [9, 7, 5],
#     [1, 1, 1]
# ]

# for notas in notas_alunos:
#     print(notas)
#     for nota in notas:
#         print(nota)

# matriz = [
#     [3, 5, 6],
#     [4, 2, 9],
#     [9, 7, 5],
#     [1, 1, 1]
# ]

# soma = 0

# for linhas in matriz:
#     print(linhas)
#     soma_linha = 0

#     for colunas in linhas:
#         print(colunas)
#         soma_linha = soma_linha + colunas
#         soma = soma + colunas

#     print(f'Soma linha é: {soma_linha}')

# print(f'Soma é: {soma}')

# matriz = [
#     [3, 5, 6],
#     [4, 2, 9],
#     [9, 7, 5],
#     [1, 1, 1]
# ]

# for l in range(len(matriz)):
#     for c in range(len(matriz[l])):
#         print(matriz[l][c])

# print(matriz[1][0])

# print()

# for i in range(4):
#     for j in range(3):
#         print(i, j)

matriz = [
    ['Andre', 3, 5, 6],
    ['Joao', 4, 2, 9],
    ['Pedro', 9, 7, 5],
    ['Jose', 1, 1, 1]
]

for l in range(len(matriz)):
    soma = 0
    for c in range(1, len(matriz[l])):
        #print(matriz[l][c])
        soma = soma + matriz[l][c]
    
    print(f'O aluno {matriz[l][0]} tem a soma {soma}')

