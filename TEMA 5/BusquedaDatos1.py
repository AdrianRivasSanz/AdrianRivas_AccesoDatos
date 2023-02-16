#CREAMOS UNA LISTA DE NÚMEROS
listaNumeros = [1,2,3,4,5,6,7,8,10]
numero = int(input("Introduce el numero a buscar"))

#CREAMOS LA FUNCION QUE LEA LA LISTA Y DIGA SI EL NUMERO ESTÁ EN ELLA O NO
def buscar():
    for i in range(len(listaNumeros)):
        if listaNumeros[i] == numero:
            print(f'Se ha encontrado el numero en {i}')
            break

buscar()