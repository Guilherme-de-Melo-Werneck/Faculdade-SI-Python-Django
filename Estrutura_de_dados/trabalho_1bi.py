import time
import random

tempo_inicial = time.time()
def quickSortInsertion(vet, inicio = 0, fim = None):
    # Se o parâmetro fim não foi especificado, definimos ele como o tamanho do vetor - 1
    fim = fim if fim != None else len(vet) - 1

    # Verifica se o início é menor que o fim, caso contrário o vetor já está ordenado
    if inicio < fim:
        # Chama a função insertionSort caso o tamanho do vetor seja menor ou igual a k
        pivo = insertionSort(vet, inicio, fim)
    else:
        # Define o pivô como o primeiro elemento do vetor
        pivo = inicio
        # Percorre o vetor a partir do segundo elemento
        for i in range(inicio+1, fim+1):
            # Se o elemento atual é menor ou igual ao pivô
            if vet[i] <= vet[inicio]:
                # Incrementa o índice do pivô e realiza a troca de elementos entre o elemento atual e o pivô
                pivo += 1
                vet[i], vet[pivo] = vet[pivo], vet[i]
        # Coloca o pivô em sua posição final
        vet[inicio], vet[pivo] = vet[pivo], vet[inicio]
        # Chama a função quickSortInsertion recursivamente para a metade inferior do vetor (elementos menores que o pivô)
        quickSortInsertion(vet, inicio, pivo - 1)
        # Chama a função quickSortInsertion recursivamente para a metade superior do vetor (elementos maiores que o pivô)
        quickSortInsertion(vet, pivo + 1, fim)

    # Retorna o vetor ordenado
    return vet

        
def insertionSort(x, inicio = 0, fim = None):
    # Define o tamanho do vetor
    n = len(x)
    # Percorre o vetor a partir do segundo elemento
    for i in range(1, n):
        # Armazena o valor do elemento atual
        k = x[i]
        # Define um índice para percorrer o vetor da direita para a esquerda a partir do elemento anterior
        j = i
        # Enquanto o índice j é maior que 0 e o elemento anterior é maior que o valor armazenado
        while j > 0 and x[j-1] > k:
            # Desloca o elemento para a direita
            x[j] = x[j-1]
            # Decrementa o índice j
            j = j - 1
        # Coloca o valor armazenado na posição correta
        x[j] = k
    # Retorna o vetor ordenado
    return x


y= random.sample(range(1, 10001), 10000)
print(quickSortInsertion(y))
print("--- %s segundos ---" % (time.time() - tempo_inicial))

