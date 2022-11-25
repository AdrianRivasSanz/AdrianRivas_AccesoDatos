"""
Diccionario
"""
'''
from this import d


miDiccionario ={
    'nombre' : 'Cristina',
    'apellidos' : 'López Perera',
    'alias' : 'Cris',
    'edad' : 24,
    'género' : 'mujer',
    'estado civil' : 'soltera',
    'color de ojos' : 'miel',
    'mascota' : 'no',
    'nombre de mascota' : 'Red'
}

print(miDiccionario)

#para añadir un campo y su valor
miDiccionario['nuevoCampo'] = 1000

#si yo le pido algo y no existe que me devuelva un (en este caso'NO EXISTE')
print(miDiccionario.get('nooombre', 'NO EXISTE'))

print(miDiccionario)
'''

"""
#rellenar el dicionario por teclado:

miDiccionarioDos = {
    'nombre' : '',
    'apellidos' : '',
    'alias' : '',
    'edad' : '',
    'género' : '',
    'estado civil' : '',
    'color de ojos' : '',
    'mascota' : '',
    'nombre de mascota' : ''}

for i in miDiccionarioDos:
    valor = input("Introduce un " + i + ":")
    miDiccionarioDos[i] = valor
    
print(miDiccionarioDos)
"""

"""Crea un diccionario que conteng marcas de zapatillas y su precio. 
    Deberá pedir el número que queremos y ver cánto cuesta.
    Entrada: nombre/marca zapatilla, precio por unidad y cuántas queremos.
    Salida: "El coste total es: " (el de toda la compra) y el "coste por marca es:"
"""

#solución del profe:
#FALTARÍA PEDIR EL Nº DE UNIDADES DE CADA MARCA Y MULTIPLICAR POR SU PRECIO

tienda={}
continuar=True
while continuar:
    marca=input("Introduce una marca: ")
    precio=float(input("introduce un precio para " + marca + ": "))
    tienda[marca]=precio
    continuar=input("¿continuas?:")=="si"
coste=0

for marca,precio in tienda.items():
    print(marca,precio)
    coste+=precio
print("el precio total es:", coste)

