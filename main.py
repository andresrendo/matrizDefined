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
print(f'\n\t\tBienvenid@ al mejor programa de matrices de la UNIMET')
while True:
    print("\nSeleccione el sistema de ecuaciones a trabajar:\n\t1. Sistema de 3 ecuaciones\n\t2. Sistema de 4 ecuacion\n\t3. Mostrar matriz\n\t4. Verificar que la matriz esté bien definida\n\t5. Solucionar sistema por metodo de Jacobi\n\t6. Salir")

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
            else: print("\n\tOpción no válida, intente de nuevo.\n\tSolo responda Si o No. ")
        if true == 0:
            clear_screen()
            print("\n\tIniciando creacion de matriz de 3x3...")
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
                true =1
                print("\n\tCreación de matriz cancelada.")
                break
            elif verify.lower() == 's'or verify.lower() == 'si':
                true = 0
                break
            else: print("\n\tOpción no válida, intente de nuevo.\n\tSolo responda Si o No. ")
        if true == 0:
            clear_screen()
            print("\n\tIniciando creacion de matriz de 4x4...")
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
                    clear_screen()
                    print("\n\tLa matriz está bien definida.\n")
                else:
                    clear_screen()
                    print("\n\tLa matriz no está bien definida, no es diagonalmente dominante.\n")
            else:
                print("\n\tNo se ha generado ninguna matriz para verificar.")
            break


    elif opcion == "5":
        clear_screen()
        print('\n\tIngresando al método de Jacobi...')
        if matriz is not None and altura > 0 and matriz.verificar_matriz_bien_definida:
            matriz.solucion_jacobi()
        if matriz is None:
            print("\n\tNo se ha generado ninguna matriz para solucionar.")


    elif opcion == '6':
        print("\nSaliendo del programa...")
        time.sleep(2)
        clear_screen()
        print("\n\tGracias por usar el mejor programa de matrices de la UNIMET\n")
        break
    else:
        clear_screen()
        print("\n\tOpción no válida, intente de nuevo.")









