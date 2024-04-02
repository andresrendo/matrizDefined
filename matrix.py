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

    def hacer_diagonalmente_dominante(self, intentos_maximos=10):
        intentos = 0
        while not self.verificar_matriz_bien_definida():
            if intentos >= intentos_maximos:
                break
            for i in range(self.filas):
                suma_fila = sum(abs(self.matriz[i, j]) for j in range(self.columnas) if i != j)
                if abs(self.matriz[i, i]) <= suma_fila:
                    # La fila i no es diagonalmente dominante, encontrar otra fila para intercambiar
                    for j in range(i+1, self.filas):
                        suma_fila = sum(abs(self.matriz[j, k]) for k in range(self.columnas) if j-1 != k)
                        print(suma_fila)
                        if abs(self.matriz[j, i]) > suma_fila:
                            # Intercambiar filas i y j
                            self.intercambiar_filas(i, j)
                            break
            intentos += 1


    def intercambiar_filas(self, i, j):
        print("entramos en la funcion de intercambiar filas")
        # Función para intercambiar filas i y j en la matriz
        for columna in range(self.columnas):
            temp = self.obtener_valor(i, columna)
            self.modificar_valor(i, columna, self.obtener_valor(j, columna))
            self.modificar_valor(j, columna, temp)
        temp_igualdad = self.igualdades[i]
        self.modificar_igualdad(i, self.igualdades[j])
        self.modificar_igualdad(j, temp_igualdad)
        self.mostrar_matriz()