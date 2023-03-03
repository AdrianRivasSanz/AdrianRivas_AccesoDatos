#LA IMAGEN DEL GRAFO SE LO ADJUNTO POR CLASSROOM

#1. CREO EL GRAFO
grafo =[
    [0,1,0,0,0],
    [0,0,1,6,9],
    [0,0,0,1,2],
    [0,0,0,0,3],
    [0,0,0,0,0]
]

#2. CREO LOS PUNTOS QUE SON LAS COORDENADAS
puntos = ["A","B","C","D","E"]
posibilidades = []
final = "E"

#3. AÑADO EL LABERINTO
def Dijkstra(laberinto):
    minimo = 100
    posicion = ""

    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            valor = (puntos[i]+puntos[j]+str(laberinto[i][j]))
            if valor[2:] != "0":
                posibilidades.append(valor)

                for k in range(len(posibilidades)-1):
                    print(posibilidades[k])
                    if posibilidades[k][1] == valor[0]:
                        num = int(posibilidades[k][2]) + int(valor[2])
                        posibilidades[len(posibilidades)-1]=posibilidades[len(posibilidades)-1][:2]+str(num)

                    if posibilidades[k][0] == valor[1]:
                        num += int(posibilidades[k][2])
                        posibilidades[k] = posibilidades[k][:2] + str(num)

    for i in posibilidades:
        if i[1] == final and minimo > int(i[2:]):
            minimo = int(i[2:])
            posicion = i
            
    return f'El camino corto es por {posicion}'

print(Dijkstra(grafo))
print(posibilidades)