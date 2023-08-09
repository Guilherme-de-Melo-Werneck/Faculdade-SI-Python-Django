def mergesort(lista, inicio=0, fim=None):
    if fim is None: #=0, none e a linha 2 e 3 serve para, se vc quiser utlizar o mergesort somente e não precisar utlizar a linha 6, 7, 8, não podendo utilizar o len dentro de um parentese, faz um if para ele 
        fim = len(lista)
    if(fim - inicio > 1): #se for maior que 1 ele não sabe resolver, ai ele dividi até ficar com 1 elemento, ai sim ele consgue revolver 
        meio = (fim + inicio)//2   #responsável pela divisão da lista 
        mergesort(lista, inicio, meio)  # ordenar do inicio até o meio da lista (parte da esquerda)
        mergesort(lista, meio, fim)   #ordenar do meio até o fim da lista (parte da direita)
        merge(lista, inicio, meio, fim) #lista completa

#Responsável pela parte da divisão da lista

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio] #pilha da esquerda
    direita = lista[meio:fim]   #pilha da direita
    top_esquerda, top_direita = 0, 0 #topo da lista da esquerda e topo da lista da direita
    for i in range(inicio, fim):
        if top_esquerda >= len(esquerda):
            lista[i] = direita[top_direita] #linha 18,17,16, se o topo da lista da esquerda for maior que a lista da esquerda, assim sabe se estrapolou a lista da esquerda, isto é, usou todos os elementos e só pode usar o da direita 
            top_direita = top_direita + 1

        elif top_direita >= len(direita):  
            lista[i] = esquerda[top_esquerda]   #linha 21,22,23, se o topo da lista da direita for maior que a lista da direita, assim sabe se estrapolou a lista da direita, isto é, usou todos os elementos e só pode usar o da esquerda
            top_esquerda = top_esquerda + 1

        elif esquerda[top_esquerda] < direita[top_direita]: #se o topo da esquerda foi menor que o topo da direita
            lista[i] = esquerda[top_esquerda]  #na posição i vai entrar quem esta na topo da esquerda
            top_esquerda = top_esquerda + 1   #avançar o topo da esquerda

        else:
            lista[i] = direita[top_direita] #se não entra na posição i da lista quem esta no topo da direita
            top_direita = top_direita + 1 #avançar o topo da lista da direita

    


lista = [1,2,3,4,5,6,7,8,9 ]
mergesort(lista)
print(lista)


#É um estrutura de ordenação dividas em duas partes, o mergesort seria para dividir os elementos da lista até chegar em 1 
#elemento em cada lista E o merge seria a parte que faz a junção dos elementos até todos ficarem em uma única lista ordenando







