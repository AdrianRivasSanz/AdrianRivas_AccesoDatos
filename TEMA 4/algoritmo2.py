listaNumeros = [40, 21, 4, 89, 10, 35]

#ALGORITMO 2     
def ordenar2(lista):
    for i in range (len(listaNumeros)):
        for j in range (len(listaNumeros)):
            if listaNumeros [i] < listaNumeros [j]:
                lista[i], lista[j] = lista[j], lista[i]
                
    print
    