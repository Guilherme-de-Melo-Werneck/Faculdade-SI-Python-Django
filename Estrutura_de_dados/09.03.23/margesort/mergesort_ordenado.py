from margesort import intercala
def merge(vet, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim)//2
        merge(vet, inicio, meio)
        merge(vet, meio, fim)
        intercala(vet, inicio, meio, fim)
def mergeSort(vet):
    merge(vet, 0, len(vet))

vet = [3, 4, 11, 15, 6, 8, 1, 5, 7, 9, 10]
mergeSort(vet)
print(vet)