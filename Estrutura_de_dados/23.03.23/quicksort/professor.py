def quickSort(vet, inicio = 0, fim = None):
    fim = fim if fim != None else len(vet) - 1

    if inicio < fim:
        pivo = particao(vet, inicio, fim)
        quickSort(vet, inicio, pivo - 1)
        quickSort(vet, pivo + 1, fim)

def particao(vet, inicio, fim):
    pivo = vet[fim]
    i = inicio

    for j in range(inicio, fim):
        if vet[j] <= pivo:
            vet[i], vet[j] = vet[j], vet[i]
            i = i + 1

    vet[i], vet[fim] = vet[fim], vet[i]
    return i

x = [3, 2, 8, 10, 1, 5, 9, 4]

quickSort(x)
print(x)




