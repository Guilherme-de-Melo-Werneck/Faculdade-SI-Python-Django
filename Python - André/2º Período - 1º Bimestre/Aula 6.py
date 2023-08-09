# lst = [3, 9, 10]

# for i in lst:
#     print(i)

# print()

# for i in range(3):
#     print(lst[i])


lst = []

while True:
    nome = input('Digite o seu nome: ')   
    if nome.upper() == 'SAIR':
        break

    notas = []
    while True:
        nota = float(input('Digite a sua nota: '))     
        if nota == -1:
            break
        notas.append(nota)
    
    registro = (nome, notas)
    lst.append(registro)

print(lst)


lst2 = [
    lst[0], lst[1]
 ]

for i in lst2:
    print(i[0], i[1])
   
    media = sum(i[1])/len(i[1])

    print(f'O aluno {i[0]} tem média {media}')

# v = (1, 0, 3, 2, 5, 4)
# c = ('seg', 'ter', 'qua', 'dom', 'sex', 'sab')

# for i in range(6):
#     print(c[v[i]]) #printa o índice de C baseado nos números informados em V.

