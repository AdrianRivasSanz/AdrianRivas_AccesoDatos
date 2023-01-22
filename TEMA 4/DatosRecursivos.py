'''opcion es para elegir entre forma iterativa o recursiva
   opc es para elegir las opciones del menu'''

while True:
    print("1. Forma_Iterativa  2. Forma_Recursiva")
    opcion = input()

    # FORMA ITERATIVA
    if opcion == "1":
        print("1.FACTORIAL  2.MULTIPLICACION  3.MCD   4.EXPONENTE  5.RESTA")
        opc = input()

        #1.FACTORIAL
        if opc == "1":

            def factorial(num):
                resultado = 1
                if num > 1:
                    for i in range(1, num + 1):
                        resultado = resultado * i
                    return print(resultado)

            factorial()


        #2.MULTILICACION
        if opc == "2":

            def multmayor0(num1, num2):
                return num1 * num2

            multmayor0(2, 5)


        #3.MCD
        if opc == "3":

            def mcd(num1, num2):
                contador = 0
                while num2 != 0:
                    contador = num2
                    num2 = num1 % num2
                    num1 = contador
                return num1

            mcd(7, 14)


        #4.EXPONENTE 
        if opc == "4":

            def potencia(num1, num2):
                return num1 ** num2

            potencia(2, 3)


        #5.RESTA
        if opc == "5":

            def resta(num1, num2):

                return num1 - num2

            resta(5, 2)



    # FORMA RECURSIVA
    if opcion == "2":
        print("1.FACTORIAL  2.MULTIPLICACION  3.MCD   4.EXPONENTE  5.RESTA")
        opc = input()

        #1.FACTORIAL
        if opc == "1":

            def factorial(num):
                if num == 1:
                    return 1
                else:
                    return num * factorial(num - 1)

            print(factorial(5))


        #2.MULTIPLICACION
        if opc == "2":

            def multmayor0(num1, num2):

                if num1 == 1:
                    return num2
                elif num2 == 1:
                    return num1
                else:
                    return num1 + multmayor0(num1, num2 - 1)

            print(multmayor0(2, 5))


        #3.MCD
        if opc == "3":

            def mcd(num1, num2):
                if num2 == 0:
                    return num1
                return mcd(num2, num1 % num2)

            print(mcd(7, 14))


        #4.EXPONENTE
        if opc == "4":

            def potencia(num1, num2):
                if num2 == 0:
                    return 1
                else:
                    return num1 * potencia(num1, num2 - 1)

            print(potencia(2, 3))


        #5.RESTA
        if opc == "5":

            def resta(num1, num2):
                if num1 == 0:
                    return num1
                else:
                    return resta(num1, num2 - 1) - 1

            print(resta(3, 2))
