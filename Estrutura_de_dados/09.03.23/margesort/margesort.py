def intercala(vet, inicio, meio, fim):
    x = vet[inicio:meio]
    y = vet[meio:fim]
    indx = 0
    indy = 0
    i = inicio
    while i < fim:
        if x[indx] < y[indy]:
            vet[i] = x[indx]
            indx = indx + 1
        else:
            vet[i] = y[indy]
            indy = indy + 1

        i = i + 1
        if indx ==len(x):
            vet[i:fim] = y[indy:len(y)]
            break
        if indy == len(y):
            vet[i:fim] = x[indx:len(x)]
            break


    print(x)
    print(y)
    print(vet)

vet = [1, 5, 7, 9, 3, 4, 6, 8]
n = len(vet)
intercala(vet, 0, n//2,n)
print(vet)