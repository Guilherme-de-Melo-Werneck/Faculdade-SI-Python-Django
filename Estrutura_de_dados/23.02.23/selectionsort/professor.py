def selectionSort(x):
  n = len(x)
  k = 0
  for i in range(0, n-1):
    for j in range(i+1, n):
      k = k + 1
      if x[j] < x[i]:
        x[j], x[i] = x[i], x[j]
  return x

y = [6,5,4,3,7]
print(selectionSort(y))
