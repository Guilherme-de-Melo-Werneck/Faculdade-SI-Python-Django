def bubble_Sort(lista):
    n = len(lista)
    for i in range (n-1): # a lista vai até o penultimo indice
        for j in range(n-1):  #o valor da lista vai até o penultimo valor
            if lista[j] > lista [j+1]: # se o número na posição j for maior que o próximo que seria o j+1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  #inverte os valores 
    
    return lista

y = [1,6,7,8,7,8,9,4,56,67]
print(bubble_Sort(y)) 

#É uma estrutura de ordenação que compara os elementos e se for maior, troca. exemplo, tenho uma lista com 3 elementos [1,4,2], 
# ele vai comparar o 1 com o 4, viu que o 4 é maior vai manter as posições, dps vai comparar o 2 com 4, 
# viu que o 2 é menor e vai comparar com 1 e vai ver que é menor, ai vai ficar [1,2,4].
