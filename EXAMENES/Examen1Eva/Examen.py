#ADRIAN RIVAS SANZ
#EXAMEN PYTHON 1ª EVA
# -*- coding: utf-8 -*-

#EJERCICIO 1 : D
#EJERCICIO 2 : A
#EJERCICIO 3 : c
#EJERCICIO 4 : D


#EJERCICIO 5
"""5. En la solución correcta al ejercicio anterior, si introduces una letra en lugar de un número,
verás que al ejecutar el programa aparece (fíjate al final) el siguiente TipoDeError: (1 punto)

ValueError: invalid literal for int() with base 10."""

while True:
    try:
        opcion=int(input("Introduce una opción del 1 al 3:"))
        if opcion==1:
            print("opción 1")
        elif opcion==2:
            print("opción 2")
        elif opcion==3:
            print("opcion 3")
        else:
            break
    except ValueError:
        print('Has pulsado una letra, introduce un número')
    
    
#EJERCICIO 6    
"""6. Escribe un programa en Python que pregunte al usuario por teclado un nombre, primer
apellido, edad y teléfono y lo guarde en un diccionario llamado MiDiccionario. (1 punto)
Para los valores, por ejemplo:

Nombre=Harry, Apellido=Potter, edad=18 y teléfono=666666666
tendrá que imprimir por pantalla el mensaje equivalente a:
”Harry Potter tiene 18 años y su teléfono es 666666666”."""


nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
telefono = int(input("Introduce tu teléfono: "))
print(nombre, apellido, "tiene", edad, "años y su teléfono es", telefono)



#EJERCICIO 7
"""7. Escribe un programa en Python que pida por teclado un número mayor que cero y escriba
en un fichero llamado “ficheroexam1.txt” todos los números que hay desde el 0 (incluido)
hasta ese número, cada uno en una línea, de forma que:"""

"""7.a) Cada vez que se ejecute el programa, el fichero inicial se rellenará con el
contenido nuevo (ver mensaje completo más abajo), borrando por completo lo que
había antes. (1 punto)"""
    
num = int(input("Introduce un numero: "))
with open ('C:Escritorio/ficheroexam1.txt','w') as f:
        i = 1
        for i in range(i,num + 1):
                f.write("El numero es: " + str(i) + "\n")
        f.close()

"""7.b) Modifica el programa 7.a para que cada vez que se ejecute el programa, el fichero
inicial se vea incrementado con el contenido nuevo (ver mensaje completo más abajo),
sin eliminar lo que había almacenado.(0,5 puntos)"""
    
num = int(input("Introduce un numero: "))
with open ('C:Escritorio/ficheroexam1.txt','r+') as f:
        i = 1
        contenido = f.read()
        for i in range(i,num + 1):
                f.write("El numero es: " + str(i) + "\n")
        f.close()


#EJERCICIO 8
"""8.a) El programa escribirá tantas líneas como el resultado del cálculo que ha realizado
en un fichero llamado “ficheroexam2.txt”, machacando siempre el contenido que ya
tuviera el fichero. (0,5 puntos)
Ejemplo:
Entrada:
a=2
b=3
c= 4
Cálculos que realiza:(a+b)*c = (2+3)*4=20"""


a = int(input("Introduce primer numero: "))
b = int(input("Introduce segundo numero: "))
c = int(input("Introduce tercer numero: "))
resultado = (a+b)*c
with open ('C:Escritorio/ficheroexam2.txt','w') as f:
        i = 1
        for i in range(i,resultado + 1):
                f.write("El calculo es "+ str(resultado) +" y esta es la linea : " + str(i) + "\n")
        f.close()



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
