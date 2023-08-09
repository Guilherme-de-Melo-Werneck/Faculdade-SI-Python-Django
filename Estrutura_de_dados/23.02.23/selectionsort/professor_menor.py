def selectionSort2(x):
  n = len(x)
  for i in range(0, n-1):
    atual = i
    for j in range(i+1, n):
      if x[j] < x[atual]:
        atual = j
    x[i], x[atual] = x[atual], x[i]
  return x