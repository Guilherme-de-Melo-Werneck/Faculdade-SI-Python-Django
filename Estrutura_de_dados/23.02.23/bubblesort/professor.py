def bubbleSort(x):
    n = len (x)
    for i in range(0, n-1):
        print("********* -- ", i)
        for j in range(n-1, i, -1):
            print(n, n-1, j)
            if x[j] < x[j-1]:
                x[j], x[j-1] = x[j-1], x[j]
    return x

y = [9, 3, 2, 1, 7, 8]
print (bubbleSort(y))

    