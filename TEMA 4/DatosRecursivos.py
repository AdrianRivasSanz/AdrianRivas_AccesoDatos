while True:
    print("1. Recursivo  2. Iterativo")
    opc = input()
    
    if opc == "1":
        print("1.Factorial  2.Multiplicar  3.MCD   4.Exponente  5.Resta")
        opc2 = input()
        
        if opc2 == "1":
            def factorial(num):
                if num == 1:
                    return 1
                else:
                    return num*factorial(num - 1)                
            print(factorial(5))
        
        if opc2 == "2":

            def multmayor0(op1, op2):
                
                if op1 == 1:
                    return op2
                elif op2 == 1:
                    return op1
                else:
                    return op1 + multmayor0(op1,op2 -1)
            
            print(multmayor0(2,3))
        
        if opc2 == "3":
            def mcd(op1, op2):

                if op2 == 0:
                    return op1
                return mcd(op2, op1 % op2)

            print(mcd(13,26))
            
        if opc2 == "4":
            def potencia(op1, op2):
                if(op2 == 0):
                    return 1
                else:
                    return op1 * potencia(op1,op2 - 1)    
            print(potencia(2,3))
            
        if opc2 == "5":
            def resta(op1, op2):
                if op1 == 0:
                    return op1
                else:
                    return resta(op1, op2 - 1) - 1
            print(resta(4,2))
       
    
    if opc == "2":
        print("1.Factorial  2.Multiplicar  3.MCD   4.Exponente  5.Resta")
        opc2 = input()
        
        if opc2 == "1":
            def factorial(num):
                resultado = 1
                if num > 1:
                    for i in range(1, num+1):
                        resultado = resultado * i
                    
                    return print(resultado)
            factorial(5)
        
        
        if opc2 == "2":
            def multmayor0(op1, op2):
            
                return op1 * op2
            
            multmayor0(2,3)
        
        
        if opc2 == "3":
            def mcd(op1, op2):
                 contador = 0
                 while op2 != 0:
                    contador = op2
                    op2 = op1 % op2
                    op1 = contador
                 return op1

            mcd(13,26)
            
            
            
        if opc2 =="4":
            def potencia(op1, op2):
                
                return op1 ** op2
            
            potencia(2,3)
        
        
        if opc2 == "5":
            def resta(op1,op2):
                
                return op1 - op2
            resta(4,2)
