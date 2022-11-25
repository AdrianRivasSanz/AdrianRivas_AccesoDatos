"""
Programa con listas que contenga la lista de asignaturas del curso y las muestre por pantalla

"""

asignaturas = ["Programacion", "Acceso a datos", "Ecem", "Inglés"]
print(asignaturas)

#una a una
for i in range(4):
    print(asignaturas[i])
    
    
for item in asignaturas:
    print("yo estudio " + item)
    
    
"""
Pregunte por la nota de cada una de ellas y muestre por pantalla la mota de cada asignatura
"""
listaNotas = []
print("Número de asignaturas:")
print(len(asignaturas))

for cont in asignaturas:
    nota = input("Qué nota tienes en " + cont + ": ")
    #para añadir a la lista
    listaNotas.append(nota)
    
print(listaNotas)


for c in range(len(asignaturas)):
    print(asignaturas[c] + " " + listaNotas[c])
    
    
"""Indicar la media de la nota de todas las asignaturas:
"""
suma = 0
for nota in listaNotas: 
    suma = suma + int(nota)
    
print("Suma: ", suma)   
print("Media asignaturas: ", (suma / len(asignaturas)))