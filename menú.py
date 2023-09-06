
import os
import random, string
import sys
import keyboard # pip install keyboard, en la terminal para descargar el import
from tkinter import *

# Importar los diferentes proyectos

import calculadora as calculator_juan
import conversor as conversor
import imc_felipe_zapata as indice_masa_corporal
import GeneradorContraseñas as GeCon
import contador_caracteres as contador_caracteres

# --------------- Limpiar consola ---------------

def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiar_consola()

# ---------- Finalizar cada herramienta ------------

def finalizar_programa():
    
    print("\n \n" + "Gracias por utilizar el software.")
    print("\n" + "Presiona (Ctrl) para mostrar el menú o (Shift) para salir del programa. \n")
    
    while True:
        
        if keyboard.is_pressed("ctrl"):
            limpiar_consola()
            break
            mostrar_menu()
            
        elif keyboard.is_pressed("shift"):
            limpiar_consola()
            print("\n" + "Saliendo del programa...\n")
            sys.exit()

# ---------------- ------------- ----------------

def mostrar_menu():

    print("\n" + " -------- MENÚ DE HERRAMIENTAS -------- ")
    print("|                                      |")
    print("|  1. Calculadora                      |")
    print("|  2. Conversor de pesos (COP)         |")
    print("|  3. Índice de masa corporal          |")
    print("|  4. Generador de contraseñas         |")
    print("|  5. Contador de caracteres           |")
    print("|  6. Salir                            |")
    print("|                                      |")
    print(" ---------------- ---- ---------------- \n")
    
opcion = "0"

while opcion != "6":

    mostrar_menu()
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
    
        limpiar_consola()

        print("Has seleccionado la Opción 1. ( Calculadora ) \n")
        print("Preciona enter para ejecutar... \n")
        input()
        
        calculator_juan.calculadora()
        finalizar_programa()

    elif opcion == "2":
        
        limpiar_consola()
        
        print("Has seleccionado la Opción 2. ( Conversor de pesos (COP) ) \n")
        print("Preciona enter para ejecutar... \n")
        input()
        
        conversor.Conversor()
        finalizar_programa()

    elif opcion == "3":
        
        limpiar_consola()
        
        print("Has seleccionado la Opción 3. ( Índice de masa corporal ) \n")
        print("Preciona enter para ejecutar... \n")
        input()

        indice_masa_corporal.procedimiento()
        finalizar_programa()
        
    elif opcion == "4":
    
        limpiar_consola()
        
        print("Has seleccionado la Opción 4. ( Generador de contraseñas ) \n")
        print("Preciona enter para ejecutar... \n")
        input()
        
        GeCon.procedimiento()
        finalizar_programa()
        
    elif opcion == "5":

        limpiar_consola()

        print("Has seleccionado la Opción 5. ( Contador de Caracteres ) \n")
        print("Preciona enter para ejecutar... \n")
        input()

        contador_caracteres.contador_caracteres()
        finalizar_programa()
    
    elif opcion == "6":
        
        limpiar_consola()
        
        print("\n" + "Saliendo del programa... \n \n")
        sys.exit()

    else:
        
        limpiar_consola()
        
        print("\n" + "Opción no válida. Por favor, selecciona una opción del menú. \n")
    
# ---------------- ------------- ----------------

