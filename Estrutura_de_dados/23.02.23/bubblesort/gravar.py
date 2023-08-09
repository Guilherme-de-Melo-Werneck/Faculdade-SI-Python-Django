def bubblesort(lista):
    n = len(lista)
    for i in range(n-1):
        ordenado = True
        for j in range(n-1):
            if lista[j]> lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                ordenado = False
            if ordenado:
                break
    return lista
y = [8,6,8,9,5,4]
bubblesort(y)
print(y)