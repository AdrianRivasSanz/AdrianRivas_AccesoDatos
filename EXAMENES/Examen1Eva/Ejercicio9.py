#EJERCICIO 9
"""9. El planteamiento que tienen es realizar una interfaz (menú) que contemple tres
opciones:

1. Consulta_Errores
Esta opción sólo tendrá que imprimir por pantalla el contenido del fichero de
desvío “ficheroexam4.txt”, comprobando si el fichero existe o no, ya que si no
existe, es debido a la ausencia de errores en la trayectoria.

2. Existe_Error. Busca coincidencias entre el fichero de control y el fichero de
desvío.
Esta opción recibe los dos ficheros (envío y control) y tras tratarlo de forma
correcta, comprueba si en el fichero de control ficheroexam3.txt están los
datos del fichero de desvío ficheroexam4.txt.

3. Borrar_Errores. Eliminar coincidencias del fichero de control
Esta opción elimina aquellos datos del fichero de desvío que existan en el
fichero de control.

4. Salir"""

#1. Consulta_Errores
def consulta_Errores(file):
    print("Consulta errores")
    contador = 0
    try:
        with open (file,"r") as f:
            fichero = f.readlines()
            for linea in fichero:
                contador += 1
                print(linea)
        f.close()
        print(f"Existen {contador} errores\n")
    except FileNotFoundError:
        print("No hay documento")


#2.Existe_Error        
def Existe_Error(file1,file2):
    print("Existe error")
    contador = 0
    try:
        with open (file2, "r") as f:
            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        with open (file1, "r") as fi:
            total = fi.readlines()
            total = dict([tuple(line.split(',')) for line in total])
        fi.close()
        for i in errores:
            if i in total:
                if errores[i] == total[i]:
                    contador+=1
        print(f"Se han encontrado {contador} errores")
    except FileNotFoundError:
        print("No hay documentos")


#3. Borrar_Errores      
"""def Borrar_Errores(file1,file2):
    print("Borrar Errores")
    try:
        with open (file2, "r") as f:
            errores = f.readlines()
            errores = dict([tuple(line.split(',')) for line in errores])
        f.close()
        with open (file1, "r") as fi:
            total = fi.readlines()
        fi.close()"""
        

#4. Menu
def menu():
    print("¿Que quieres hacer?")
    print("1. Consultar Errores")
    print("2. Existe Error")
    print("3. Borrar Errores")
    print("4. Salir")
    elegir = int(input())
    return elegir

#5. Inicio
def inicio():
    ficheroTotal = "ficheroexam3.txt"
    ficheroErrores = "ficheroexam4.txt"
    while True:
        opcion = menu()
        if opcion == 1:
            consulta_Errores(ficheroErrores)
        elif opcion == 2:
            Existe_Error(ficheroTotal,ficheroErrores)
        elif opcion == 3:
            Borrar_Errores(ficheroTotal,ficheroErrores)
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opcion invalida")

inicio()