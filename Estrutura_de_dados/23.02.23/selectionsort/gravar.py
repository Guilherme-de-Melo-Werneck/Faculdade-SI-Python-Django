def selectionsort(lista):
    n = len(lista)
    for i in range(n-1):
        minimo = i
        for j in range(i+1,n):
            if lista[j]< lista[minimo]:
                minimo = j
                lista[i], lista[minimo] = lista[minimo], lista[i]
            if i >= 0 and lista[i]<lista[i-1]:
                break

                
    return lista

            

    
    
y = [1,9,9,8,0,5,4]
print(selectionsort(y))



            




    

        

