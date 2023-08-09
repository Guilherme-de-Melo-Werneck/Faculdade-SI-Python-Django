def quicksort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)-1
    if inicio <fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p -1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio 
    for j in range(inicio, fim):
        if lista[j] <=  pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i = i+1
    lista[i], lista[fim] = lista[fim], lista[i]    
    return i 

        



x = [3, 2, 8, 10, 1, 5, 9, 4]

quicksort(x)
print(x)


            
