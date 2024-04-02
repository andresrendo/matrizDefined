from matrix import Matriz
import os
import time
import numpy as np

matriz = None
altura = 0

def clear_screen():
    # Comprobamos el sistema operativo actual
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Posix (Linux, macOS, etc.)
        os.system('clear')
clear_screen()
print('''  
              ------------------------------------
              || ¡¡ BIENVENIDO A Your_MATRIX !! ||
              ------------------------------------ 
''')

while True:
    print('''
Seleccione el sistema de ecuaciones a trabajar:
    
    1. Sistema de 3 ecuaciones.
    2. Sistema de 4 ecuaciones.
    3. Mostrar matriz.
    4. Verificar que la matriz esté bien definida.
    5. Solucionar sistema por Sucesión de Jacobi.
    6. Obtener Matriz Traspuesta.
    7. Obtener Matriz Inversa
    0. Salir''')

    opcion = input("\nIngrese la opción deseada: ")
    if opcion == '1':
        true = 0
        while matriz is not None:
            verify = input("\n\t¿Desea sobreescribir la matriz actual? (S/N): ")
            if verify.lower() == 'n' or verify.lower() == 'no':
                clear_screen()
                true = 1
                print("\n\tCreación de matriz cancelada.")
                break
            elif verify.lower() == 's'or verify.lower() == 'si':
                true = 0
                break
            else: print("\n\tOpción no válida, intente de nuevo.\n\tSolo responda Sí o No. ")
        if true == 0:
            clear_screen()
            print("\n\tIniciando creación de matriz de 3x3...")
            filas = columnas = 3
            matriz = Matriz(filas, columnas)
            altura = filas
            print("\n|X + Y + Z = 0")
            print("|X + Y + Z = 0")
            print("|X + Y + Z = 0\n")        
            matriz.trespor3(altura)        

    elif opcion == '2':
        while matriz is not None:
            verify = input("\n\t¿Desea sobreescribir la matriz actual? (S/N): ")
            if verify.lower() == 'n' or verify.lower() == 'no':
                clear_screen()
                print("\n\tCreación de matriz cancelada.")
                break
            elif verify.lower() == 's' or verify.lower() == 'si':
                break
            else:
                print("\n\tOpción no válida, intente de nuevo.\n\tSolo responda Sí o No.")
        if matriz is None or verify.lower() == 's' or verify.lower() == 'si':
            clear_screen()
            print("\n\tIniciando creación de matriz de 4x4...")
            filas = columnas = 4
            matriz = Matriz(filas, columnas)
            altura = filas
            print("\n|X + Y + Z + W = 0")
            print("|X + Y + Z + W = 0")
            print("|X + Y + Z + W = 0")
            print("|X + Y + Z + W = 0\n")
            matriz.cuatropor4(altura)

    elif opcion == "3":
        clear_screen()
        print("\n\tMostrando matriz...")
        if matriz is not None and altura > 0:
            if matriz.verificar_matriz_nula():
                print("\n\tSe ha generado la matriz nula.")
                print("\n\tRegresando al menú para ingresar otro sistema...")
                time.sleep(2)
            else:
                print("\n\tMatriz generada:") 
                matriz.mostrar_matriz() 
        else:
            print("\n\tNo se ha generado ninguna matriz aún.")


    elif opcion == "4":
        clear_screen()
        print("\n\tVerificando que la matriz esté bien definida...")
        while True:
            if matriz is not None and altura > 0:
                if matriz.verificar_matriz_bien_definida():
                    print("\n\tLa matriz está bien definida.\n")
                else:
                    matriz.hacer_diagonalmente_dominante()
                    if matriz.verificar_matriz_bien_definida():
                        print("\n\tLa matriz se ha ajustado y ahora está bien definida.\n")
                        matriz.mostrar_matriz()
                    else:
                        print("\n\tNo se pudo ajustar la matriz para que sea diagonalmente dominante.\n")
                        print("\n\tLa matriz no está bien definida, no es diagonalmente dominante.\n")
            else:
                print("\n\tNo se ha generado ninguna matriz para verificar.")
            break


    elif opcion == "5":
        clear_screen()
        if matriz is not None and altura > 0:
            if matriz.verificar_matriz_bien_definida():
                print('\n\tIngresando a la Sucesión de Jacobi...')
                matriz.solucion_jacobi()
            else:
                print("\n\tNo se puede realizar la sucesión de Jacobi porque la matriz no es diagonalmente dominante.")
        else:
            print("\n\tNo se ha generado ninguna matriz para solucionar.")


    elif opcion == "6":
        clear_screen()
        mat = matriz.matriz
        trasp = np.transpose(mat)
        print(f'\n\tLa matriz original es: \n{mat}\n\nY la matriz traspuesta es: \n{trasp}')


    elif opcion == "7":
        clear_screen()
        print("\n\tMostrando matriz...\n")
        if matriz is not None and altura > 0:
            if matriz.verificar_matriz_nula():
                print("\n\tSe ha generado la matriz nula.")
                print("\n\tRegresando al menú para ingresar otro sistema...")
                time.sleep(2)
            else:
                print("\n\tMatriz Inversa:") 
                matriz.generar_inversa()
                print("\n\tMatriz Original:") 
                matriz.mostrar_matriz()
        else:
            print("\n\tNo se ha generado ninguna matriz aún.")


    elif opcion == '0':
        print("\n\tSaliendo del programa...")
        time.sleep(2)
        clear_screen()
        print("\n\tGracias por usar el mejor programa de matrices de la UNIMET\n")
        break

    else:
        clear_screen()
        print("\n\tOpción no válida, intente de nuevo.")
