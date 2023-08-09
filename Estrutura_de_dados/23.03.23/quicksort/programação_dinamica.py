def quicksort(lista, inicio=0, fim=None):
    if fim is None:                   #linha 2 e 3, descobrir o tamanho da lista, pois não pode botar len dentro de parentese aue seria no def
        fim = len(lista)-1            # tamanho da lista, pois pega até o penultimo elemendo, porque o último seria o pivo
    if inicio < fim:                  #Se inicio for menor que fim, há mais de um elemento a ser classificado e o algoritmo QuickSort precisa ser aplicado recursivamente.
        p = partition(lista, inicio, fim)   #os elementos menores que o pivô estejam à esquerda e os elementos maiores que o pivô estejam à direita. A função retorna o índice do pivô na lista.
        # recursivamente na sublista à esquerda (menores)
        quicksort(lista, inicio, p-1)   #é chamada recursivamente para classificar a sublista à esquerda do pivô, que está entre os índices inicio e p-1.
        # recursivamente na sublista à direita (maiores)
        quicksort(lista, p+1, fim)     #é chamada recursivamente para classificar a sublista à direita do pivô, que está entre os índices p+1 e fim.

def partition(lista, inicio, fim):
    pivot = lista[fim]             #Nesta linha, é definido o pivô que será utilizado na separação dos elementos da lista. O pivô é definido como o último elemento da lista.
    i = inicio                     # (linha amarela) A variável i é inicializada como o índice do primeiro elemento da lista, que é o inicio recebido como argumento da função.
    for j in range(inicio, fim):   # (linha roxa) este é um loop for que itera sobre os elementos da lista, começando pelo índice inicio e indo até fim - 1.
        # j sempre avança, pois representa o elementa em análise  e delimita os elementos maiores que o pivô
        if lista[j] <= pivot:       #Nesta linha, é feita uma comparação entre o elemento atual da lista (lista[j]) e o pivô. Se o elemento atual for menor ou igual ao pivô, a linha a seguir é executada.
            lista[j], lista[i] = lista[i], lista[j] #esta é uma operação de swap (troca). Ela troca o elemento atual (lista[j]) com o elemento que está na posição i da lista (lista[i])
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1       #incrementa i para que a próxima posição a ser trocada seja a seguinte.

    lista[i], lista[fim] = lista[fim], lista[i] # responsável por colocar o pivô em sua posição final. O pivô é colocado na posição i, que é a posição onde todos os elementos à esquerda são menores ou iguais a ele e todos os elementos à direita são maiores que ele
    return i  #retorna o índice onde o pivô foi colocado

x = [3, 2, 8, 10, 1, 5, 9, 4]

quicksort(x)
print(x)