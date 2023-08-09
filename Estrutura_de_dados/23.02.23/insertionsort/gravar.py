def insertionsort(lista):
    n = len(lista)
    for i in range(1,n):
        chave = lista[i]
        j = i-1
        while j >= 0 and lista[j] > chave:
            lista[j+1]= lista[j]
            j = j -1
        lista[j+1] = chave
    return lista

y = [1,5,4,3,4,5,6]
insertionsort(y)
print(y)






        


           

