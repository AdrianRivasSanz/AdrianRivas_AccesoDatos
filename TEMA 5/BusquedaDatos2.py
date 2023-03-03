#CREAMOS UNA LISTA DE NÚMEROS
listaNumeros = [1,2,3,4,8,100,1200,1201]

#BUSCAR 1201 y el 2
numero = int(input("Introduce el numero a buscar"))

def buscar(listaNumeros,numero):
    #DIVIDIMOS LA LISTA PARA PODER HACER UNA BUSQUEDA MAS SENCILLA
    mitad = len(listaNumeros)//2

    print(listaNumeros[mitad:])
    print(listaNumeros[mitad])
    
    if mitad < 1:
        if listaNumeros[mitad] == numero:
            print("Numero Encontrado")
            return numero
        else:
            return print("Numero no encontrado")

    elif listaNumeros[mitad] > numero:
        return buscar(listaNumeros[:mitad],numero)
    else:
        return buscar(listaNumeros[mitad:],numero)

buscar(listaNumeros,numero)


#SOLUCION LUISMI
lista=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26]

def algoritmo (lista, n, izquierda, derecha):
    
    if n> lista[len(lista)-1]:
        return("Nooo encontrado, mayor que el último de la lista")
    
    if izquierda > derecha:
        if n==izquierda:
            return "encontrado"
        else:
            return ("No encontrado")
        
    Indice_Medio = (izquierda + derecha) // 2
    Elemento_medio = lista[Indice_Medio]
    
    print("Elemento medio:",Elemento_medio)
    if Elemento_medio == n:
        return ("Encontrado")
    if n < Elemento_medio:
        return algoritmo(lista, n, izquierda, Indice_Medio - 1)
    else:
        return algoritmo(lista, n, Indice_Medio + 1, derecha)

print(lista[0])
print(len(lista))
print("---")
num=int(input("Buscar:"))
#lista,número a buscar, valor primero, longitud lista
print(algoritmo(lista,num,lista[0],len(lista))) 
