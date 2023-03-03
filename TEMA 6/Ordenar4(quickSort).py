def ordenacion(lista):
    pivote = lista[len(lista) - 1]
    i = -1
    j = 0
    jDos = 0
    if len(lista) < 2:
        listaFinal.append(lista[0])
        return lista[0]
    else:
        while j < len(lista):
            if lista[j] == pivote:
                i += 1
                jDos = j
                lista[j], lista[i] = lista[i], lista[j]

            elif lista[j] < pivote:
                i += 1
                lista[j], lista[i] = lista[i], lista[j]

            j += 1

        print(lista[:jDos])
        return ordenacion(lista[:jDos]),ordenacion(lista[jDos:])

listaNumeros = [40, 21, 4, 10, 9, 35]
listaFinal = []
ordenacion(listaNumeros)
print(listaFinal)

#SOLUCION LUISMI
def QuickSort(vector, bajo, alto):
    if len(vector) == 1:
        return vector
    
    if bajo < alto:
        #Dividir y acomodar el pivote
        vector_partido = Partir(vector, bajo, alto)
        
        QuickSort(vector, bajo, vector_partido-1)
        QuickSort(vector, vector_partido+1, alto)
        

def Partir(vector, bajo, alto):  
    #Pivote el de la derecha
    pivote = vector[alto]
    #apuntador del ultimo elemento más pequeño
    i = (bajo-1)
    
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            #avanzar el apuntador
            i = i+1
            #intercambiar elementos
            vector[i], vector[j] = vector[j], vector[i]
    #Al final intercambiar el pivote        
    vector[i+1], vector[alto] = vector[alto], vector[i+1]
    #Regresa la posición final del pivote
    return (i+1)

vector = [10,7,8,9,1,5,4,12,25,65,3,2,6]
n = len(vector)
QuickSort(vector, 0, n-1)
print(vector)