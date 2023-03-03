#CREAMOS UNA LISTA DE NÚMEROS
listaNumeros = [1,8,7,2,15,21,17,4]
numero = int(input("Introduce el numero a buscar"))

#CREAMOS LA FUNCION QUE LEA LA LISTA Y DIGA SI EL NUMERO ESTÁ EN ELLA O NO
def buscar():
    for i in range(len(listaNumeros)):
        if listaNumeros[i] == numero:
            print(f'Se ha encontrado el numero en la posicion{i}')
            break

buscar()