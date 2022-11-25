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
    #imprescindible tipar (int)
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
