def insertion_sort(lista):

    n = len(lista)

    for i in range(1, n): #parte da lista que não esta ordenada, começa no segundo indice até o penaultimo indice
        chave = lista[i]    #número atual
        j = i - 1           #controlador para se a chave for maior que a lista ja ordenada, parar, começa pelo indice 0, "sublista"

        while j >= 0 and lista[j] > chave:   #quando o j for maior ou igual a 0, pois ainda tem itens para comparar e se o j(posição) for maior que chave
            lista[j+1] = lista[j]   # avançar a posição j que seria a sub-lista ordenada 1 posição e vai fazendo isso, até poder inserir a chave
            j = j - 1   # não faz nada 
        
        lista[j+1] = chave  #precisa disso pois ele termina uma posição antes, pq está -1, e atraves dessa linha ele vai +1 e inserir a chave
    
    return lista #retornar a lista la em cima

y = [1, 4, 6, 7, 8, 9, 9, 9, 5]
print(insertion_sort(y))

#essa estrutura e ordenação compara o valor no indice 1 com o indice 0, se for menor, troca, se não, mantem, dps vai comparar 
# o valor do indice 2 com os dois que está ordenado, porém se ele for maior já que o valor do indice 1,
# ele já não vai comparar com o indice 0, pois ele ja sabe que é menor, pq o indice 0 e 1 ja estava ordenado.
#entao basicamente ele faz um sublista com os valores ordenados e assim vai comparando 