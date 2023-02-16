#CREAMOS UNA LISTA DE NÚMEROS
listaNumeros = [1,200,300,40,500,60,7,80,1000]
numero = int(input("Introduce el numero a buscar"))

def buscar(listaNumeros,numero):
    #DIVIDIMOS LA LISTA PARA PODER HACER UNA BUSQUEDA MAS SENCILLA
    mitad = len(listaNumeros)//2

    print(listaNumeros[mitad:])
    print(listaNumeros[mitad])

    
buscar(listaNumeros,numero)