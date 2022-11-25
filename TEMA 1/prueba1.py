#impresión normal
"""
print("hey")



a = "sgdf"
print(a)

#True y False en mayúscula
b = False


#listas con []
lista = ["casa", "coche", "bici"]
print(lista)
print(lista[1])


#tuplas, una lista cerrada que no se va a modificar ()
listita = ("casa", "coche", "bici")


#añadir un elemento a la lista
lista.append("triciclo")
lista.append(1234)
#también puedo poner la posición y lo que quiero añadir
lista.insert(3, "cohete")

print(lista)
print(listita)


#separar por caracteres y añadir a la lista
lista.extend("curso de info")

print(lista)



#diccionario
MiDiccionario = {
'Nombre' : 'Margarita',
'Edad' : 55,
'Genero' : 'Femenino'
}

print(MiDiccionario)



c = 4
d = 4

if c == d:
    print("c es igual que d")
print("estoy aqui")


a = 2 + 3
if a == 4: #condicion si a es exactamente cuatro, entonces(:)
    print ("A es igual a cuatro") # Imprimir
else:
    print ("No se cumple la condicion")
#Resultado: "No se cumple la condicion"



e = 2 + 3
if e == 4: #condicion si a es exactamente cuatro, entonces(:)
    print ("A es igual a cuatro") # Imprimir
elif e == 5:
    print ("A es igual a cinco")
elif e == 6:
    print ("A es igual a seis")
else:
    print ("No se cumple la condición")
#Resultado: "A es igual a cinco"


anio = int(input("dime un año:"))
print(anio)



#coge 2años los compara y si la diferencia es menor de 100 años la dif. es menor a un siglo...
anio1 = int(input("dime un año para comparar:"))
anio2 = int(input("dime otro año para comparar:"))

if anio1 == anio2:
    print ("Se trata del mismo año")
else:
    #si creo esta variable va más lento:
    #dif = anio1 - anio2
    #if dif == 100:
    if (anio1-anio2) == 100:
        print("La diferencia es un siglo")
    #elif dif > 100:
    elif (anio1-anio2) > 100:
        print("La diferencia es mayor a un siglo")
    elif (anio2-anio1) > 100:
        print("La diferencia es mayor a un siglo")
    else:
        print("La diferencia es menor de un siglo")

"""

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creamos la lista con números

for num in numeros: #En la variable "num" almacenamos los ítem de la lista
    if num % 2 == 0: #Condición: Si el resto de la división por dos es cero entonces:
        print("Par: ")
        print (num) # Imprimimos la variable num
    else:
        print("Impar: ")
        print (num)


opcion = int(input("Escoge: \n1.Pares \n2.Impares \n3.Todos"))

if opcion == 1: 
    for num in numeros:
        if num % 2 == 0:
            print (num) 
if opcion == 2:
    for num in numeros:
        if num % 2 != 0:
            print (num) 
if opcion == 3:
    for num in numeros:
        print (num) 



Palabras = ['Peine', 'Pelo', 'Ventana', 'Refrigerador', 'Adolescente', 'Dentista', 'Asesino'] 
#Lista de palabras
for caracteres in Palabras: #Creamos el bucle para iterar Palabras y almacenar en caracteres
    print ((caracteres), ('###Longitud:'), (len(caracteres))) 
"""

"""
#Variable con una frase y decir cuantas a hay en el texto
miFrase = "Hola estoy programando en Python"
numA = 0
#letr = "a"
letr = str(input("Introduce una letra: "))
for letra in miFrase:
   # print(letr)
    #if letra == "a":
    if letra == letr:
        numA = numA + 1
print(numA)

"""



#Programa que lea 4 números por teclado y muestre por pantalla el mayor
"""
aux = 0

for i in range(4):
    numero = int(input("Dime 1 número para comparar:"))
    if numero >= aux: 
        aux = numero
print("El mayor es: ", aux)
"""


"""Empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años entra gratis. Entre 4 y 18 años paga 5E y si es mayor de 18 paga 10E."""
"""
edad = int(input("Edad del usuario:"))

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 5
else:
    precio = 10
print("Precio de la entrada: ", precio)
"""

#Funciones
"""
a = 4
b = 7

def sumar(x, y):
    print("La suma es", x + y)
    
#sumar(4,7)
sumar(a,b)
"""


"""Crear una calculadora. Utilizar funciones: suma, resta, multip., división, exponente y otra que te inventes. 
Llamarlas por el prog. principal de forma que te pida dos números y te muestre por pantalla todas las operaciones.
"""

"""
print("Bienvenido a la Calculadora")

def suma(suma1, suma2):
    print("Suma: ", suma1 + suma2) 

def resta(resta1, resta2):
    print("Resta: ", resta1 - resta2) 

def multiplicacion(mult1, mult2):
    print("Multiplicación: ", mult1 * mult2) 

def division(div1, div2):
    print("División", div1 / div2) 

def exponente(exp1, exp2):
    print("Exponente: ", exp1 ** exp2) 



n1 = int(input("Número 1:"))
n2= int(input("Número 2:"))
suma(n1, n2)
resta(n1, n2)
multiplicacion(n1, n2)
division(n1, n2)
exponente(n1, n2)
"""


"""

#WHILE

i = 0 
while(i <= 9):
    i += 1
    print("Este while incrementa un contador: ", i)
    
"""
    
#para poder hacer saltos de línea usamos tres"""   

while True:
    opcion = (input("""¿Qué quieres de desayuno?
             1: Churros con chocolate
             2: Tostada con zumo
             3: Tortilla de patata
             4: Pizza fría
             5. Ayuno intermitente
             6. Salir"""))
    



"""EJERCICIO CALCULADORA PERO CON MENÚ: Crear una calculadora. Utilizar funciones: suma, resta, multip., división, exponente y otra que te inventes. 
Llamarlas por el prog. principal de forma que te pida dos números y te muestre por pantalla todas las operaciones.
"""
    
def suma(suma1, suma2):
    print("Suma: ", suma1 + suma2) 

def resta(resta1, resta2):
    print("Resta: ", resta1 - resta2) 

def multiplicacion(mult1, mult2):
    print("Multiplicación: ", mult1 * mult2) 

def division(div1, div2):
    print("División", div1 / div2) 

def exponente(exp1, exp2):
    print("Exponente: ", exp1 ** exp2) 


def pedirNumeros():
    n1 = int(input("Número 1:"))
    n2 = int(input("Número 2:")) 
    return (n1, n2)
       

op = 0 
while True:
    print("Bienvenido a la Calculadora")
    op = int(input("""¿Qué quieres calcular?
                1: Suma
                2: Resta
                3: Multiplicación
                4: División
                5. Exponente
                6. Salir"""))
    
    print(op)
    if op == 1:
        a1, b1 = pedirNumeros()
        suma(a1, b1)
    elif op == 2:
        a1, b1 = pedirNumeros()
        resta(a1, b1) 
    elif op == 3:
        a1, b1 = pedirNumeros()
        multiplicacion(a1, b1)
    elif op == 4:
        a1, b1 = pedirNumeros()
        division(a1, b1)
    elif op == 5:
        a1, b1 = pedirNumeros()
        exponente(a1, b1)
    elif op == 6:
        break
    else:
        print("Opción no válida")
        break
