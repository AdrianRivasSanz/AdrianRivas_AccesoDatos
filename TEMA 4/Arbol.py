class arbol:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        
    def esVacio(self):
        if self.valor is None:
            return True
        else:
            return False
        
    def insertar(self, valor):
        if self.esVacio():
            self.valor = valor
        elif valor < self.valor:
            if self.izquierda is None:
                self.izquierda = arbol(valor)
            else:
                self.izquierda.insertar(valor)
        elif valor > self.valor:
            if self.derecha is None:
                self.derecha = arbol(valor)
            else:
                self.derecha.insertar(valor)
                
    def buscar(self, valor):
        if self.esVacio():
            return False
        elif valor == self.valor:
            return True
        elif valor < self.valor:
            if self.izquierda is None:
                return False
            else:
                return self.izquierda.buscar(valor)
        elif valor > self.valor:
            if self.derecha is None:
                return False
            else:
                return self.derecha.buscar(valor)
                
    def eliminar(self, valor):
        if not self.esVacio():
            if valor == self.valor:
                if self.izquierda is None and self.derecha is None:
                    self.valor = None
                elif self.izquierda is None:
                    self.valor = self.derecha.valor
                    self.izquierda = self.derecha.izquierda
                    self.derecha = self.derecha.derecha
                elif self.derecha is None:
                    self.valor = self.izquierda.valor
                    self.derecha = self.izquierda.derecha
                    self.izquierda = self.izquierda.izquierda
                else:
                    suc = self.derecha
                    while suc.izquierda is not None:
                        suc = suc.izquierda
                    self.valor = suc.valor
                    self.derecha.eliminar(suc.valor)
            elif valor < self.valor:
                self.izquierda.eliminar(valor)
            elif valor > self.valor:
                self.derecha.eliminar(valor)

# Ejemplo de uso
arbol = []
arbol.insertar(     )
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

