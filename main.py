from matrix import Matriz

matriz = None  
altura = 0

while True:
    print("Seleccione el sistema de ecuaciones a trabajar:")
    print("1. Sistema de 3 ecuaciones")
    print("2. Sistema de 4 ecuaciones")
    print("3. Mostrar matriz")
    print("4. Verificar que la matriz esté bien definida")  
    print("5. Solucionar sistema por metodo de Jacobi")  
    print("6. Salir")

    opcion = input("Ingrese la opción deseada : ")
    if opcion == '1':
        filas = columnas = 3
        matriz = Matriz(filas, columnas)
        altura = filas
        print("|X + Y + Z = 0")
        print("|X + Y + Z = 0")
        print("|X + Y + Z = 0")        
        matriz.trespor3(altura)
 
    elif opcion == '2':
        filas = columnas = 3
        matriz = Matriz(filas, columnas)
        altura = filas
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")
        print("|X + Y + Z + W = 0")
        matriz.cuatropor4(altura)          

    elif opcion == "3":
        if matriz is not None and altura > 0:
            print("Matriz generada:") 
            matriz.mostrar_matriz() 
        else:
            print("No se ha generado ninguna matriz aún.")

    elif opcion == "4":
        if matriz is not None and altura > 0:
            if matriz.verificar_matriz_bien_definida():
                print("La matriz está bien definida.")
            else:
                print("La matriz no está bien definida, no es diagonalmente dominante.")
        else:
            print("No se ha generado ninguna matriz para verificar.")

    elif opcion == "5":
        if matriz is not None and altura > 0 and matriz.verificar_matriz_bien_definida:
            matriz.solucion_jacobi()


    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.")









