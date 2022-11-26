#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Esas dos filas unifican él código de caracteres, las ponemos SIEMPRE!!

#Forma clásica de crear un archivo:

#Creamos el archivo
#la "w" permite que se pueda escribir dentro
#f = open("archivotext.txt", "w")

#Escribimos en él 
#f.write("Creando el archivo de texto en python de forma clásica")

#Cerramos el archivo
#f.close()


#Utilizando el With As:

#Creamos el archivo
with open("archivotext.txt", "w") as f:

#Escribimos en él 
    f.write("Creando el archivo de texto en python usando with as")

#Cerramos el archivo
f.close()


"""Escribe un programa en Python que escriba de la forma clásica en un fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en Python usando la forma clásica,
que es la siguiente:
f = open()
f.write()
f.close()
"""

#f = open("ficheroenpython.txt", "w")
#f.write("Este es mi primer programa de fichero y lo he escrito en Python usando la forma clásica, \nque es la siguiente: \nf = open() \nf.write() \nf.close()")
#f.close()


"""Escribe un programa en Python que escriba de la forma recomendada en un fichero llamado "ficheroenpython.txt" el siguiente mensaje:
Este es mi primer programa de fichero y lo he escrito en Python usando la forma recomendada,
que es la siguiente:
with open() as f
f.write()
f.close()
"""

#with open("ficheroenpython.txt", "w") as f:

    #f.write("Este es mi primer programa de fichero y lo he escrito en Python usando la forma recomendada, \nque es la siguiente: \nwith open() as f \nf.write() \nf.close()")

#f.close()


"""Ejemplo lectura:"""

"""
with open ("ficheroenpython.txt", "r") as f:
    texto = (linea for i,linea in enumerate(f) if i>=1 and i<=3)
    for linea in texto:
        print(linea)"""
        
        
"""Lectura con readLine"""

"""
#Abrimos usando Read(r)
with open ("ficheroenpython.txt", "r") as f:

    #Lo abrimos utilizando el método readlines y lo almacenamos en la variable
    contenido = f.readlines()#lee todas las líneas y las separa con un \n

    #imprimimos la variable que tiene el contenido
    print(contenido)
"""   
    
"""Para leer y añadir algo al final"""
"""
with open ("ficheroenpython.txt", "r+") as f: #Abrimos utilizando Reescribir (r+)
    contenido = f.read()
    #Escribimos la nueva línea
    f.write("\nEscribiendo una nueva línea al final")
f.close()
"""

"""Añadir algo al final, sin leer"""
"""
with open ("ficheroenpython.txt", "a") as f: #Abrimos utilizando Reescribir (r+)
    #Escribimos la nueva línea
    f.write("\nOtra opción")
f.close()
"""

"""Que aparezca 8 veces más escrito "Otra opción" """
"""
with open ("ficheroenpython.txt", "a") as f: #Abrimos utilizando Reescribir (r+)
    for i in range(8):
        #Escribimos la nueva línea
        f.write("\nOtra opción")
f.close()
"""

"""Añade una lista al final"""
"""
lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

#Lo abrimos como Reescribir (r+)
with open ("ficheroenpython.txt", "r+") as f:
    #Lo abrimos utilizando read y lo almacenamos en la variable
    contenido = f.read()
    #Escribimos la lista en el archivo línea a línea
    f.writelines(lista)
f.close()
"""

"""Lo mismo pero sin(r+), mejor opción ahorramos código"""
"""
lista = ["\nEscribiendo \n", "listas \n", "en ficheros"]

with open ("ficheroenpython.txt", "a") as f:
    #Escribimos la lista en el archivo línea a línea
    f.writelines(lista)
f.close()
"""

"""
#Forma clásica de crear un archivo
#Creamos el archivo
f = open("archivotext-excepciones.txt", "w")
#Escribimos en él
f.write("Probando excepciones")
#Cerramos el archivo
f.close()
#Ahora intentamos abrirlo e imprimir su contenido:
nombre_fichero = "archivotext-excepciones.txt"
try:
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero')
"""   
    
    
"""Ejercicio 1:
Escribe un programa que pida por teclado un número positivo entre 1 y 100
y lo guarde en un fichero llamado "ejercicio1-100.txt"
"""

"""Opción 1: clásica"""
"""
#Creamos el archivo
f = open("ejercicio1-100.txt", "w")

numero = str(input(numero = str(input("Introduce un número positivo entre 1 y 100:"))))
#Escribimos en él
f.write(numero)
#Cerramos el archivo
f.close()
"""

"""Opción 2: formal"""
"""
n = int(input('Introduce un número positivo entre 1 y 100:'))
nombre_fichero = 'ejercicio1-100.txt'
with open(nombre_fichero, 'w') as f:
    f.write(str(n))
f.close()
"""

'''Ejercicio 2:
Escribe un programa que pida por teclado un número positivo entre 1 y 10 
y guarde en un fichero llamado "ejercicio2-tabla.txt" la tabla de multiplicar 
(sin contar el 0) del número intrioducido
ejemplo tras introducir el nº9
9x1=9
9x2=18
.
.
.
9x10=90
'''

'''
nTabla = int(input("Introduce un número positivo entre 1 y 10:"))

nombre_fichero = "ejercicio2-tabla.txt"
with open(nombre_fichero, "w") as f:
    for i in range(1,11):
        f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
f.close()
'''

'''Ejercicio 3:
Escribe un programa que pida por teclado un número positivo entre 1 y 10 
y guarde en un fichero llamado "ejercicio3-tabla.txt" la tabla de multiplicar 
de todos los números desde el 1 al elegido. Cada tabla debe estar identificada
mediante un texto en la pantalla.
Tabla del 1:
1x0=0
1x1=1
.
.
.
1x10=10
Tabla del 2:
2x0=0
2x1=2
.
.
.
2x10=20
'''
'''
nTabla = int(input("Hasta qué tabla quieres saber: "))

nombre_fichero = "ejercicio3-tabla.txt"
with open(nombre_fichero, "w") as f:
    for i in range(1,(nTabla+1)):
        f.write(str("Tabla del ") + str(i) + ":" + "\n")
        for j in range(11):
            f.write(str(i) + "x" + str(j) + "=" + str(i*j) + "\n")
        f.write("\n")
f.close()
'''

'''
Ejercicio 4:
Modifica el ejercicio 2 para que el fichero tenga el nombre del número 
con el que se crea la tabla de multiplicar. Por ejemplo, si se introduce por teclado el 9,
que el fichero se llame "ejercicio2-tabla del 9.txt'''
'''
nTabla = int(input("Introduce un número positivo entre 1 y 10 para crear el archivo de esa tabla:"))

nombre_fichero = "ejercicio2-tabla-del-" + str(nTabla) + ".txt"
with open(nombre_fichero, "w") as f:
    for i in range(1,11):
        f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
f.close()'''


'''Ejercicio 5:
Escribe un programa que pida un número entero positivo entre 1 y 10,
y en base al número leído, busque el fichero llamado: "fichero-tabla-del-n.txt".
Este fichero contendrá la tabla de multiplicar del número n introducido por teclado
y deberá mostrarse por pantalla un mensaje que avise del problema.
'''

nTabla = int(input("Para buscar el archivo de una tabla, introduce un número positivo entre 1 y 10:"))
nombreFich = "ejercicio2-tabla-del-" + str(nTabla) + ".txt"

try:
    with open (nombreFich, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("No existe el fichero")
    
    
'''Ejercicio 6:
Escribir un programa en python que lea un número n por teclado y a partir de ese número,
lea las n primeras líneas del fichero creado en el ejercicio 2
'''
#Opción 1
'''
n = int(input("Introduce hasta qué línea deseas leer: "))

with open ("ejercicio2-tabla.txt", "r") as f:
    for i in range(n):
        print(f.readline())
f.close() 
'''

#Opción 2
'''
with open ("ejercicio2-tabla.txt", "r") as f:
    numFilas = int(input("Introduce hasta qué línea deseas leer: "))
    texto = (linea for i,linea in enumerate(f) if i>=0 and i<=(numFilas-1))
    for linea in texto:
        print(linea)
f.close()       
'''   

        