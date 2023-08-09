def mergesort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio >1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista,inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    top_esquerda, top_direita = 0,0
    for i in range(inicio, fim):
        if top_esquerda >=len(esquerda):
            lista[i] = direita[top_direita]
            top_direita=top_direita+1
        elif top_direita >= len(direita):
            lista[i] = esquerda[top_esquerda]
            top_esquerda = top_esquerda + 1
        elif esquerda[top_esquerda] < direita[top_direita]:
            lista[i] = esquerda[top_esquerda]
            top_esquerda = top_esquerda + 1
        else:
            lista[i] = direita[top_direita]
            top_direita = top_direita + 1

    return lista


y = [4,3,2,3,4,7]
mergesort(y)
print(y)

    

        




