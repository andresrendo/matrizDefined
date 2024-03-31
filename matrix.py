import numpy as np

def solo_num(eje,i):
        while True:
            try:
                num = int(input(f"Introduzca el valor de {eje} en la ecuación {i+1}: "))
                break
            except ValueError:
                print("Por favor, introduzca un número entero.")
        return num
class Matriz:
    def __init__(self, filas, columnas, valor_inicial=0):
        self.filas = filas
        self.columnas = columnas
        self.matriz = np.full((filas, columnas), valor_inicial)
        self.igualdades = np.zeros(filas, dtype=int)


    def mostrar_matriz(self):
        print(self.matriz)


    def obtener_valor(self, fila, columna):
        return self.matriz[fila][columna]


    def modificar_valor(self, fila, columna, nuevo_valor):
        self.matriz[fila][columna] = nuevo_valor

    def modificar_igualdad(self, numFila, igualdad):
        self.igualdades[numFila] = igualdad


    def mostrar_igualdad(self):
        print("Igualdades:", self.igualdades)


    def trespor3(matriz, altura):
        for i in range(altura):
            X = solo_num("X",i)
            Y = solo_num("Y",i)
            Z = solo_num("Z",i)
            igualdad = solo_num("igualdad",i)
            # Formatea variables con signos
            Xec = "+" if X > 0 else ""
            Yec = "+" if Y > 0 else ""
            Zec = "+" if Z > 0 else ""
            # Almacena ecuaciones y valor de igualdad
            ecuacion = f"{Xec}{X}X {Yec}{Y}Y {Zec}{Z}Z = {igualdad}"
            matriz.modificar_valor(i, 0, X)
            matriz.modificar_valor(i, 1, Y)
            matriz.modificar_valor(i, 2, Z)
            matriz.modificar_igualdad(i, igualdad)

        print("\nEl sistema de ecuaciones es:")
        for i in range(altura):
            print(f"\t |{matriz.obtener_valor(i, 0)}X\t {matriz.obtener_valor(i, 1)}Y\t {matriz.obtener_valor(i, 2)}Z\t =\t {matriz.igualdades[i]}|\n")
        return matriz


    def cuatropor4(matriz, altura):
        for i in range(altura):
            X = solo_num("X",i)
            Y = solo_num("Y",i)
            Z = solo_num("Z",i)
            W = solo_num("W",i)
            igualdad = solo_num("igualdad",i)

            Xec = "+" if X > 0 else ""
            Yec = "+" if Y > 0 else ""
            Zec = "+" if Z > 0 else ""
            Wec = "+" if W > 0 else ""

            ecuacion = f"{Xec}{X}X {Yec}{Y}Y {Zec}{Z}Z {Wec}{W}W = {igualdad}"
            matriz.modificar_valor(i, 0, X)
            matriz.modificar_valor(i, 1, Y)
            matriz.modificar_valor(i, 2, Z)
            matriz.modificar_valor(i, 3, W)
            matriz.modificar_igualdad(i, igualdad)

        print("\nEl sistema de ecuaciones es:")
        for i in range(altura):
            print(f"\t |{matriz.obtener_valor(i, 0)}X\t {matriz.obtener_valor(i, 1)}Y\t {matriz.obtener_valor(i, 2)}Z\t {matriz.obtener_valor(i, 3)}W\t =\t {matriz.igualdades[i]}|\n")
        return matriz


    def verificar_matriz_nula(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j] != 0:
                    return False
        return True


    def verificar_matriz_bien_definida(self):
        for i in range(self.filas):
            suma_fila = sum(abs(self.matriz[i, j]) for j in range(self.columnas) if i != j)
            if abs(self.matriz[i, i]) <= suma_fila:
                return False
        return True

    def solucion_jacobi(self):
        x = np.zeros_like(self.igualdades)
        D = np.diag(self.matriz)
        R = self.matriz - np.diagflat(D)
        for cuenta_iteracion in range(100):

            x_new = (self.igualdades - np.dot(R,x))/D
            x = x_new

        print("\nSolution:")
        print(f'\t{x}')   
