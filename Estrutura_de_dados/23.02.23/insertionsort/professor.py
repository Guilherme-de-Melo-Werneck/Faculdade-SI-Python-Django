def insertionSort(x):
    n = len(x)
    for i in range(1, n):
        k = x[i]
        j = i
        while j>0 and x[j-1]>k:
            x[j] = x[j-1]
            j = j -1
        x[j] = k
    return x

y = [12, 11, 13, 5, 6]
print(insertionSort(y))

