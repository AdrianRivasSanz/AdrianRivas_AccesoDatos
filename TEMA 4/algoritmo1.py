listaNumeros = [40, 21, 4, 89, 10, 35]

#ALGORITMO 1
def ordenar1(lista):
    for i in range (len(listaNumeros)):
        for j in range (len(listaNumeros)-1):
            if listaNumeros[j]>listaNumeros[j+1]:
                aux = listaNumeros[j]
                listaNumeros[j] = listaNumeros [j+1]
                listaNumeros[j+1] = aux
                
                
        print(listaNumeros)
        
   
 