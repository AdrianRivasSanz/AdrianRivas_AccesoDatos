'''Ampliar el diccionario siguiente con los siguientes campos. Ponerlos directamente en el código.
Apellido, edad(18), género, padres (James y Lilli)
diccionarioHarry = {
    "Nombre" : "Harry",
}
'''
#1
diccionarioHarry = {
    "Nombre" : "Harry",
    "Apellido" : "Potter",
    "Edad" : 18,
    "Género" : "Masculino",
    "Padres" : ["James", "Lilli"]
}

#2.Para imprimirlo
print(diccionarioHarry)

#3.Para imprimir el valor de una clave
print(diccionarioHarry["Apellido"], "\n\n")

#4.Imprimir los padres
print(diccionarioHarry["Padres"])#Imprimo todo(a los dos)
print(diccionarioHarry["Padres"][0:2])#Desde donde hasta donde quiero imprimir(todo en este caso)
print(diccionarioHarry["Padres"][1:2])#Imprimo solo a la madre
print(diccionarioHarry["Padres"][1])#Así imprimo también a la madre

#5.Cambiar la edad a 22
print(diccionarioHarry["Edad"])
diccionarioHarry["Edad"] = 22
print(diccionarioHarry["Edad"])

#6.Añadir un campo nuevo al final
diccionarioHarry["Grupo"] = ""

#7.Cambiar el nombre de una clave por otro. Por ejemplo, cambiae la clave grupo por la clave Casa, sin necesidad de utilizar un for
diccionarioHarry["Casa"] = diccionarioHarry.pop("Grupo")
print(diccionarioHarry)

#8.Borrar un par clave valor
del (diccionarioHarry["Edad"])
print(diccionarioHarry)

#9.Obtener el valor de una clave
print(diccionarioHarry["Apellido"]) #forma 1 
print(diccionarioHarry.get("Apellido")) #forma 2

#10.Añadir a una variable el contenido de una clave
valorVariable = diccionarioHarry.get("Apellido")
print(valorVariable)

#11.Imprimir las claves en lugar de los valores
print(diccionarioHarry.keys())

#12.Impimir todos los valores 
print(diccionarioHarry.values())

#13.Crear tuplas
cosas = ("casa", "puerta", "reloj", "mesa", "silla", "banco", "cuadro", "alfombra")

numeros = (1, 2, 3, 4, 5)

#14.Comó ver el par clave-valor de un diccionario
print(diccionarioHarry.items()) #Lo que devuelve es una tupla


#15.Slice: vamos a imprimir partes(rebanadas) de una tupla
#Vamos a seleccionar (imprimir) los tres primeros elementos de la tupla

#mi tupla
numeros2 = (111, 222, 333, 444, 555, 666)

print(numeros2)#todas
print(numeros2[0:3])#de la primera a la tecera
print(numeros2[1:3])#segunda y tercera
print(numeros2[:-2])#todas menos 2 últimas
print(numeros2[2:])#todas menos 2 primeras
print(numeros2[-2:])#solo las 2 últimas

#16.Cómo saber la longitud de un diccionario
print(len(diccionarioHarry))

#17.Saber la longitud de una clave de un diccionario
print(len(diccionarioHarry["Padres"]))

#18.Split
text = "Partiendo con Split" #si no digo nada busca espacios en blanco
#print(text.split())

#19.
'''Escribe el siguiente texto y partelo:
Python es un lenguaje de programación que permite tipar pero no permite compilar, ya que es un lenguaje interpretado
19.a: Cogiendo las comas como separador
19.b: Cogiendo los espacios en blanco
19.c: Cogiendo la letra 'e'
'''

texto = "Python es un lenguaje de programación que permite tipar pero no permite compilar, ya que es un lenguaje interpretado"
print(texto.split(","))
print(texto.split(" "))
print(texto.split("e"))


'''20.Crea un programa que a partir del ficchero de texto: "prueba1.txt", el cual contiene exactamente esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura y para cada linea del fichero imprima:
20.a: El contenido de la línea 
20.b: El contenido de cada líena desglosado por caracteres: ("A", ", ", ...\n)
20.c: El contenido de cada línea en formato "primer elemento", "segundo elemento" (o lo que es lo mismo clave valor):
("A", "1"\n)
'''

'''Pasos para la resolución del ejercicio:
-Abrir el fichero
-Guardar el contenido del fichero en una variable 
-Cerrar el fichero
-Iterar sobre el contenido de cada línea(recorrer con un for)
-Imprimir lo que se pide:
    a:cada línea
    b:tuplear
    c:tuplear
'''

nombre_fichero = "prueba1.txt"
miContenido = "A,1\nB,2\nC,3\nD,4"

with open(nombre_fichero, 'w') as f:
    f.write(miContenido)
f.close()


#más pistas
miTupla1 = tuple([1,4,6])
print(miTupla1)

miTupla2=tuple("texto")
print(miTupla2)

miTupla3 = tuple({4:"one", 6:"two"})
print(miTupla3)
print(miTupla3[0])


#CÓMO CREAR UN DICCIONARIO DIRECTAMENTE: dict
midict2 = dict(nombre="LM", altura=195, ojos="azules")
print(midict2)


#20 (en este caso lo hemos leído de la forma clásica)
file = "prueba1.txt"
f = open(file, 'r')
contenido = f.readlines()
f.close()

#20.a
line = str()
for line in contenido:
    print("\nEl contenido de cada línea es: ", line)
    #20.b
    print(tuple(line))
    #20.b
    print(tuple(line.split(",")))
    
    


'''21.Crea un programa que a partir del ficchero de texto: "prueba1.txt", el cual contiene exactamente esto:
A,1
B,2
C,3
D,4

Abra el fichero en modo lectura e indique si una letra introducida por teclado está dentro del fichero, y
de estarlo, qué valor tiene asociado. En caso de no estar la letra introducida, mostrará un mensaje indicando
"la letra leída:" letra leída "no se encuentra en el fichero".
'''

letra = str(input("Dime una letra: "))
contenido= dict([tuple(line.split(","))for line in contenido])
#La línea anterior recorre el contenido del fichero que está almacendo en contenido:
#El for recorre contenido y en cada iteración guarda el par clave-valor en line
#Crea una tupla que la parte (split) por las comas
#Genera un diccionario(dict) con la tupla
#El diccionario lo guardo en contenido

if letra in contenido:
    print("Para la letra (clave): " + letra + " y su valor es: " + contenido[letra])
else:
    print("La letra " +  letra + " no está")