#!/usr/bin/env python3

# Author -> R3B00T

def crear_marco_texto():
    # Solicitar al usuario el texto que desea poner en el centro
    texto_central = input("Ingresa el texto que deseas poner en el centro: ")
    
    # Solicitar al usuario el carácter del marco
    caracter_marco = input("Ingresa el carácter que deseas usar para el marco (*, =, -, etc.): ")

    # Determinar el ancho del cuadro
    ancho_cuadro = 50
    alto_cuadro = 9
    
    # Calcular las posiciones del texto en el centro
    linea_texto_central = (alto_cuadro // 2)
    col_texto_central = (ancho_cuadro - len(texto_central)) // 2
    
    # Crear el cuadro
    cuadro = []
    
    for i in range(alto_cuadro):
        if i == 0 or i == alto_cuadro - 1:
            cuadro.append(caracter_marco * ancho_cuadro)
        else:
            if i == linea_texto_central:
                linea = caracter_marco + " " * (col_texto_central - 1) + texto_central + " " * (ancho_cuadro - len(texto_central) - col_texto_central - 1) + caracter_marco
            else:
                linea = caracter_marco + " " * (ancho_cuadro - 2) + caracter_marco
            cuadro.append(linea)
    
    # Imprimir el cuadro
    for linea in cuadro:
        print(linea)

# Ejecutar la función
crear_marco_texto()

