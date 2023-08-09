#Alterar o Selection sort de maneira que apenas uma troca de posições 
#seja efetuada no vetor a cada interação do laço mais exerto.
def selection_sort(lista):
    n = len(lista)
    for i in range(n-1):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
                lista[i], lista[minimo] = lista[minimo], lista[i]
            if i >= 0 and lista[i] < lista[i-1]:
                break
  
