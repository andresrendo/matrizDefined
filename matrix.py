# Create a class for a matrix
class Matriz:
    def __init__(self, filas, columnas, valor_inicial=0, igualdad1 = 0, igualdad2= 0, igualdad3 = 0, igualdad4 = 0):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[valor_inicial for _ in range(columnas)] for _ in range(filas)]

    def mostrar_matriz(self):
        for fila in self.matriz:
            print(fila)

    def obtener_valor(self, fila, columna):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            print("\nÍndices fuera de rango.")
            return None
        return self.matriz[fila][columna]

    def modificar_valor(self, fila, columna, nuevo_valor):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            print("\nÍndices fuera de rango.")
            return
        self.matriz[fila][columna] = nuevo_valor
    
    def modificar_igualdad(self, numFila, igualdad):
        if numFila == 0:
            self.igualdad1 = igualdad
        elif numFila == 1: 
            self.igualdad2 = igualdad
        elif numFila == 2:
            self.igualdad3 = igualdad
        elif numFila == 3:
            self.igualdad4 = igualdad
            


    def mostrar_igualdad(self):
        print(f"\nEl valor de igualdad es: {self.igualdad1}")
        print(f"\nEl valor de igualdad2 es: {self.igualdad2}")
        print(f"\nEl valor de igualdad3 es: {self.igualdad3}")
        print(f"\nEl valor de igualdad4 es: {self.igualdad4}")

