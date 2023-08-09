def bubbleSort(x):
    n = len(x)

    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if x[j] < x[j-1]: #troca de posição
                x[j], x[j-1] = x[j-1], x[j]
    return x

y = [9, 3, 2, 1, 7, 8]

print(bubbleSort(y))