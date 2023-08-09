# geralheap vai fazer um sub-heap se transformar em um heap, aonde os pais são maiores que os filhos.

def geralHeap(vet, i, n): #vet = vetor, i=indice, n = tamanho do vetor
    indm = i              #armazena o maior valor entre pai e filho 
    indfe = i * 2 + 1     #indice do filho a esquerda
    indfd = i * 2 + 2     #indice do filho a direita
 
    if indfe < n and vet[indfe] > vet[indm]:   #fe for menor que o tamanho total do vetor e o valor do fe for maior que o valor o indm
        indm = indfe                           #o indm é o valor de indfe

    if indfd < n and vet[indfd] > vet[indm]:  #mesma coisa porém com filho a direita
        indm = indfd

    if indm != i:        #indm for diferente do i, que seria o pai, precisa ser trocado
        vet[i], vet[indm] = vet[indm], vet[i]   #resposável pela troca
        geralHeap(vet, indm, n) #verificar todos


#resposável por pegar o indice 0 do heap, isto é, o maior valor do vetor e botar no final da lista e ir botando 
# os maiores na frente do que já está ordenado até não sobrar nenhum

def heapSort(vet):   #heapsort esta recebendo o valor do vetor
    n = len(vet)     #o valor do vetor inteiro
    for i in range(n//2 - 1, -1, -1):    # para achar o indice do ultimo nó, valor final(isto é) primeiro nó, diminui 1 em cada interação
        geralHeap(vet, i, n)   #verificar em todos


    for i in range(n-1, 0, -1): #último elemento da lista, primeiro elemento da lista,diminui 1 em cada interação
        geralHeap(vet, i, n)   #verificar em todos
        vet[i], vet[0] = vet[0], vet[i] #resposável por trocar os valores 
        geralHeap(vet, 0, i) # para que ele faça com todos, isto é, o segundo maior elemento seja o pai maior(indice 0)
        

vet = [6, 9, 2, 7, 8, 3, 4]
heapSort(vet)
print(vet)


#pega uma árvore binária, orderna ela do maior para o menor pois o pai sempre é maior que os filhos e pega o maior
# valor dela e bota em uma lista ordenada, e dps faz a mesma coisa com exeção desse valor que ja está na outra lista
# Esse código é uma implementação do algoritmo HeapSort, que é um algoritmo de ordenação que utiliza a estrutura de 
# dados chamada de heap.

#chatgpt oq é essa funçaõ 
# A função geralHeap é responsável por criar um heap, que é uma árvore binária completa que obedece uma propriedade de ordem 
# entre seus elementos. Na implementação, o vetor vet é considerado como uma árvore binária, onde o elemento na posição i 
# corresponde ao nó pai dos elementos nas posições 2i+1 e 2i+2, que são os filhos esquerdo e direito, respectivamente.
# Na função geralHeap, é realizado um processo de down-heap, que consiste em comparar o elemento pai com seus filhos e 
# trocar de posição com o maior deles, caso o pai seja menor. Esse processo é realizado recursivamente até que o heap 
# esteja corretamente formado. A função heapSort é responsável por ordenar o vetor vet. Na primeira parte do algoritmo,  
# é criado um heap a partir dos elementos do vetor, começando pelos nós mais baixos e subindo até a raiz.  Em seguida, 
# é realizado um processo de up-heap para ordenar o vetor. Esse processo consiste em trocar o primeiro elemento  
# (que é o maior do heap) com o último elemento não ordenado do vetor, reduzir o tamanho do heap em 1 e aplicar o 
# down-heap  no primeiro elemento, para garantir que o heap seja reorganizado e continue  obedecendo a propriedade de ordem. 
# Ao final, o vetor vet estará ordenado em ordem crescente. No exemplo de entrada  [6, 9, 2, 7, 8, 3, 4], 
# o resultado de  saída será [2, 3, 4, 6, 7, 8, 9]. 



