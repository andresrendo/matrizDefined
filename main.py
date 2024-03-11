# import numpy as np
# import random
from matrix import Matriz

# Crear una matriz de 3x3 con valores aleatorios entre 0 y 9

def trespor3(matriz, altura):
    for i in range  (altura):
        X = int(input(f"\nIntroduzca el valor de X en la Ecuación {i+1}: "))
        if X > 0:
            Xec = f"{X}"
        elif X == 0:
            Xec = f"+{X}"
        else:
            Xec = f"{X}"
        print(f"{Xec}X + Y + Z = 0 \n")
        Y = int(input(f"\nIntroduzca el valor de Y en la Ecuación {i+1}: "))
        if Y > 0:
            Yec = f"+{Y}"
        elif Y == 0:
            Yec = f"+{Y}"
        else:
            Yec = f"{Y}"
        print(f"{Xec}X {Yec}Y + Z = 0 \n")
        Z = int(input(f"\nIntroduzca el valor de Z en la Ecuación {i+1}: "))
        if Z > 0:
            Zec = f"+{Z}"
        elif Z == 0:
            Zec = f"+{Z}"
        else:
            Zec = f"{Z}"
        print(f"{Xec}X {Yec}Y {Zec}Z = 0 \n")
        matriz.modificar_valor(i, 0, X)
        matriz.modificar_valor(i, 1, Y)
        matriz.modificar_valor(i, 2, Z)
        igualdad = input(f"\nIntroduzca el valor de igualdad en la Ecuación {i+1}: ")
        print(f"{Xec}X {Yec}Y {Zec}Z = {igualdad}\n")
        matriz.modificar_igualdad(i, igualdad)
    print("\n* El Sistema de Ecuaciones es: \n")
    print(f"|{matriz.obtener_valor(0, 0)}X {matriz.obtener_valor(0, 1)}Y {matriz.obtener_valor(0, 2)}Z = {matriz.igualdad1}")
    print(f"|{matriz.obtener_valor(1, 0)}X {matriz.obtener_valor(1, 1)}Y {matriz.obtener_valor(1, 2)}Z = {matriz.igualdad2}")
    print(f"|{matriz.obtener_valor(2, 0)}X {matriz.obtener_valor(2, 1)}Y {matriz.obtener_valor(2, 2)}Z = {matriz.igualdad3}")
    return matriz

def cuatropor4(matriz, altura):
    for i in range  (altura):
        X = input(f"\nIntroduzca el valor de X en la Ecuación {i+1}: ")
        if X > 0:
            Xec = f"{X}"
        elif X == 0:
            Xec = f"+{X}"
        else:
            Xec = f"{X}"
        print(f"{Xec}X + Y + Z + W = 0 \n")
        Y = input(f"\nIntroduzca el valor de Y en la Ecuación {i+1}: ")
        if Y > 0:
            Yec = f"+{Y}"
        elif Y == 0:
            Yec = f"+{Y}"
        else:
            Yec = f"{Y}"
        Z = input(f"\nIntroduzca el valor de Z en la Ecuación {i+1}: ")
        if Z > 0:
            Zec = f"+{Z}"
        elif Z == 0:
            Zec = f"+{Z}"
        else:
            Zec = f"{Z}"
        W = input(f"\nIntroduzca el valor de W en la Ecuación {i+1}: ")
        if W > 0:
            Wec = f"+{W}"
        elif W == 0:
            Wec = f"+{W}"
        else:
            Wec = f"{W}"
        print(f"{Xec}X {Yec}Y {Zec}Z {Wec}W = 0 \n")
        matriz.modificar_valor(i, 0, X)
        matriz.modificar_valor(i, 1, Y)
        matriz.modificar_valor(i, 2, Z)
        matriz.modificar_valor(i, 3, W)
        igualdad = input(f"\nIntroduzca el valor de igualdad en la Ecuación {i+1}: ")
        print(f"{Xec}X {Yec}Y {Zec}Z {Wec}W = {igualdad}\n")
        matriz.modificar_igualdad(i, igualdad)
    print("\n* El Sistema de Ecuaciones es: \n")
    print(f"|{matriz.obtener_valor(0, 0)}X {matriz.obtener_valor(0, 1)}Y {matriz.obtener_valor(0, 2)}Z {matriz.obtener_valor(0, 3)}W = {matriz.igualdad1}")
    print(f"|{matriz.obtener_valor(1, 0)}X {matriz.obtener_valor(1, 1)}Y {matriz.obtener_valor(1, 2)}Z {matriz.obtener_valor(1, 3)}W = {matriz.igualdad2}")
    print(f"|{matriz.obtener_valor(2, 0)}X {matriz.obtener_valor(2, 1)}Y {matriz.obtener_valor(2, 2)}Z {matriz.obtener_valor(2, 3)}W = {matriz.igualdad3}")
    print(f"|{matriz.obtener_valor(3, 0)}X {matriz.obtener_valor(3, 1)}Y {matriz.obtener_valor(3, 2)}Z {matriz.obtener_valor(3, 3)}W = {matriz.igualdad4}")
    return matriz

def main():
    print('''  
                        ------------------------------------
                        || ¡¡ BIENVENIDO A Your_MATRIX !! ||
                        ------------------------------------ 
          ''')
    altura = input("¿Cuántas ecuaciones desea tener 3 ó 4?: ")
    while altura != "3" and altura != "4":
        print("\n- Por favor introduzca un valor valido")
        altura = input("\n¿Cuántas ecuaciones desea tener 3 ó 4?: ")
    altura = int  (altura)
    ancho = int(altura)
    print("\n* El Sistema de Ecuaciones es: \n")

    if ancho == 3:
        print("|X + Y + Z = 0")
        print("|X + Y + Z = 0")
        print("|X + Y + Z = 0")
    elif ancho == 4:
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")

    matriz = Matriz (altura, ancho)  # Crear una matriz de nxm con valores iniciales 0

    if ancho == 3:
        matriz = trespor3(matriz, altura)
    elif ancho == 4:
        matriz = cuatropor4(matriz, altura)
    matriz.mostrar_matriz()

main()

