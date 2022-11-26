#Adrián Rivas Sanz
#5 ejercicios con excepciones "clase.py" 
#!/usr/bin/env python
# -*- coding:utf-8 -*-


#EJERCICIO 1:
"""Escribe un programa que pida por teclado un numero positivo entre 1 y 100 y lo guarde en un fichero llamado ejercicio1-100.txt"""

f = open("ejercicios1-100.txt","w")
numero = input("Dime un numero del 1 al 100")
f.write(numero)
f.close()



#EJERCICIO 2:
"""Escribe un progrma aque pida por teclado un numero positivo entre 1 y 10 y guarde en un fillero
llamado ejercicio2-tabla.txt la tabla de multiplicar(sin contar el 0) del numero introducido"""

f = open("ejercicios2-tabla.txt","w")
numero = int(input("Dime un numero del 1 al 10"))
for i in range(1,11):
    f.write(str(numero) + ' X ' + str(i)+'\n')
f.close()



#EJERCICIO 3:
"""Escribe programa que escriba todas las tablas de multiplicar del 1-n"""

numero = int(input("Dime un numero"))
for n1 in range(1,numero +1):
    for n2 in range(0,11):
        print(f'{n1} x {n2} = {n1*n2}')




#EJERCICIO 4:
"""Modifica el ejercicio 2 para que el fichero tenga el nombre del número 
con el que se crea la tabla de multiplicar. Por ejemplo, si se introduce por teclado el 9,
que el fichero se llame "ejercicio2-tabla del 9.txt"""

nTabla = int(input("Introduce un numero positivo entre 1 y 10"))
nombre_fichero = "ejercicio2-tabla-del-" + str(nTabla) + ".txt"

try:
    with open(nombre_fichero, "w") as f:
        for i in range(1,11):
            f.write(str(nTabla) + 'x' + str(i) + '=' + str(nTabla*i) + '\n')
    f.close()
except FileNotFoundError:
    print("No existe")



#EJERCICIO 6:
"""Escribir un programa en python que lea un numero n por teclado y 
a partir de ese numero, lea las n primeras lineas del fichero creado en el ej2"""

numero = int(input("Di un numero del 1 al 10"))
nombre_fichero = 'ejercicio2-tabla del 1.txt'

try:
    with open(nombre_fichero,"r") as f:
        texto = (linea for i, linea in enumerate(f) if i>= 0 and i<numero)
        for linea in texto:
            print(linea)
except FileNotFoundError:
    print("No existe")