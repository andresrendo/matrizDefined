import numpy as np

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
            X = int(input(f"Introduzca el valor de X en la ecuacion {i+1}: "))
            Y = int(input(f"Introduzca el valor de Y en la ecuacion {i+1}: "))
            Z = int(input(f"Introduzca el valor de Z en la ecuacion {i+1}: "))
            igualdad = int(input(f"Introduzca el valor de igualdad en la ecuacion {i+1}: "))
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

        print("El sistema de ecuaciones es:")
        for i in range(altura):
            print(f"|{matriz.obtener_valor(i, 0)}X {matriz.obtener_valor(i, 1)}Y {matriz.obtener_valor(i, 2)}Z = {matriz.igualdades[i]}|")
        return matriz


    def cuatropor4(matriz, altura):
        for i in range(altura):
            X = int(input(f"Introduzca el valor de X en la ecuacion {i+1}: "))
            Y = int(input(f"Introduzca el valor de Y en la ecuacion {i+1}: "))
            Z = int(input(f"Introduzca el valor de Z en la ecuacion {i+1}: "))
            W = int(input(f"Introduzca el valor de W en la ecuacion {i+1}: "))
            igualdad = int(input(f"Introduzca el valor de igualdad en la ecuacion {i+1}: "))

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

        print("El sistema de ecuaciones es:")
        for i in range(altura):
            print(f"|{matriz.obtener_valor(i, 0)}X {matriz.obtener_valor(i, 1)}Y {matriz.obtener_valor(i, 2)}Z {matriz.obtener_valor(i, 3)}W = {matriz.igualdades[i]}|")
        return matriz


    def verificar_matriz_bien_definida(self):
        for i in range(self.filas):
            suma_fila = sum(abs(self.matriz[i, j]) for j in range(self.columnas) if i != j)
            if abs(self.matriz[i, i]) <= suma_fila:
                return False
        return True





