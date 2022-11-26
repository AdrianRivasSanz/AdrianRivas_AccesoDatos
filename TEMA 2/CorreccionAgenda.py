'''Implementa una aplicación en Python que permita la administración de una agenda de contactos telefónicos.
Para ello, el programa deberá tener las siguientes funciones:
- Crear el fichero (vacío) que contenga los nombres y teléfonos de clientes. El fichero se llamará “miagenda.txt”.
- Deberá comprobarse si el fichero existe o no.
Si no existe, el programa pedirá si queremos crearlo
Si existe, deberá pedir si queremos dejarlo en blanco

- Podrá añadir al fichero un nuevo cliente, siguiendo la estructura en pareja: nombre,teléfono.
Por ejemplo:
r2d2,6666666666
harry,888888888
neo,811081108
El formato es: Nombre del cliente y teléfono separados por una coma y cada cliente en una línea diferente. No deberán haber saltos de línea al principio o al final del documento. No habrá nombres repetidos. Se deberá distinguir entre mayúsculas y minúsculas.
- Se podrá consultar el número de teléfono de un cliente, para lo cual el programa nos preguntará el nombre del cliente del que
necesitamos saber su teléfono.
- Se podrá eliminar un cliente y su teléfono de la lista, quedando el fichero si dicho cliente.
- Crea un menú que permita gestionar la agenda. El menú deberá llamar a las funciones:
· Crear fichero
· Añadir contacto
· Consultar teléfono
· Borrar contacto
· Salir'''

# -*- coding: utf-8 -*-
import os,sys

def Consultar_telefono(file, cliente):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return("\nEl fichero " + file + " no existe\n")
    else: 
        directorio = f.readlines()
        f.close()   
        directorio = dict((tuple(line.split(',')) for line in directorio))
        if cliente in directorio:
            return directorio[cliente]                  
        else:
            return('El cliente ' + cliente + ' no existe\n')
        
    
def Telefono_nuevo(file, cliente, telf):
    try:
        f = open(file, 'r')
    except FileNotFoundError:
        return("\nEl fichero " + file + " no existe\n")
    else:      
        f.close()  
        f = open(file, 'a')
        f.write(cliente + "," + telf + '\n')
        f.close()
        return("El teléfono se ha añadido. \n")

def crear_fichero(file):
    if os.path.isfile(file):
        answer = input("El fichero " + file + " ya existe. ¿Desea vaciarlo (S/N)? ")
        if answer == "N":
            return "No se ha creado el fichero porque ya existe.\n"
    
    f = open(file, 'w')
    f.close()
    return "Se ha creado el fichero para la agenda"
        
def menu():

    print("Gestión de agenda telefónica")
    print("=======================================")
    print("1 - Consultar un teléfono")
    print("2 - Añadir un teléfono")
    print("3 - Eliminar un teléfono")
    print("4 - Crear agenda")
    print("0 - Terminar")
    opcion1 = str(input("Introduzca el número de la opción deseada: "))
    return opcion1

def lanzarprograma():
    '''Función que lanza las opciones del menú de la aplicación para la gestión de la agenda telefónica
    '''
    fichero = "miagendaclase.txt"
    opcion=str()
    while True:
        opcion=menu()
        if opcion=="1":
            print("Has pulsado 1")
            cliente = str(input("Introduce el nombre del cliente:"))
            print(Consultar_telefono(fichero, cliente))
            
        elif opcion=="2": 
            cliente = str(input("Introduce el nombre del cliente:"))
            telf = str(input("Introduce el teléfono del del cliente:"))

            print(Telefono_nuevo(fichero, cliente, telf))
            
        elif opcion=="3": 
            print("Has pulsado 3")
            
        elif opcion=="4": 
            print(crear_fichero(fichero))           
        else:
            break

#---------------- prog prin
lanzarprograma()