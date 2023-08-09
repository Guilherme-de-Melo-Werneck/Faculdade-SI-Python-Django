#Altere os programas bubblesort e selectionsort de maneira que eles parem de executar caso o vetor já esteja ordernado

a = '-'
def bubbleSort2(x):
  n = len(x)
  print("vetor original: ", x)
  print(a*50)
  for i in range(0, n-1):
    ordenado = True
    for j in range(n-1, i, -1):
      if x[j] < x[j-1]:
        x[j], x[j-1] = x[j-1], x[j]
        ordenado = False
    print(i, "vetor: ", x)
    print(a*50)
    if ordenado:
      break
  return x

y = [1,9,3,4,5,6,7,8]
print(bubbleSort2(y))

print(a*50)

def selectionSort2(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
        if i > 0 and lista[i] < lista[i-1]:
            break
    return lista


print(selectionSort2(y))