# lista = [7,5,1,8,3]

# n = len(lista)
# minimo =  lista[0]
# for i in range(n):
#     if lista[i] < minimo:
#         minimo = lista[i]
# print(minimo)


def selectionSort(lista):
    n = (len(lista))

    for i in range(n-1):  #lista vai do primeiro elemento até o penultimo indice
        minimo = i        #valor minimo muda de acordo com a mundança do i
        for j in range(i, n): #começa no valor de i e vai até n
            if lista[j] < lista[minimo]: #numero da posição j for menor que o numero da posição minimo
                minimo = j    # minimo vai ser o valor de j 
            if lista[i] > lista[minimo]: # o valor de i for maior que o valor de minimo 
                lista[i], lista[minimo] = lista[minimo], lista[i] # vão trocar de posição

    return lista


y = [1,9,9,8,0,5,4]
print(selectionSort(y))


#ele vai pegar o menor valor e vai botar ele no indice 0, e o valor que estava no indice 0 vai para o indice 
# que estava o menor valor, e assim ele faz com todos, até ficar tudo organizado.


