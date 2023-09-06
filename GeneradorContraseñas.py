import random
import os
import string


def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_contraseña(longitud, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):

    caracteres = string.ascii_letters

    if usar_mayusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("\n --> Error: Debes seleccionar al menos un tipo de caracter. <--\n")
        return None

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def procedimiento():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n--> GENERADOR DE CONTRASEÑAS SEGURAS <--")

    while True:
        try:
            longitud = int(input("\n<-- Longitud de la contraseña: "))
            if longitud <= 0:
                print("\n --> Error: La longitud debe ser mayor que cero. <--\n")
                continue
            break
        except ValueError:
            print("\n --> Error: Ingresa un número válido para la longitud. <--\n")

    while True:
        usar_mayusculas = input("\n<-- Incluir mayúsculas (S/N): ").strip().lower()
        if usar_mayusculas in ["s", "n"]:
            usar_mayusculas = usar_mayusculas == "s"
            break
        else:
            print("\n --> Error: Ingresa 'S' para Sí o 'N' para No. <--\n")

    while True:
        usar_numeros = input("\n<-- Incluir números (S/N): ").strip().lower()
        if usar_numeros in ["s", "n"]:
            usar_numeros = usar_numeros == "s"
            break
        else:
            print("\n --> Error: Ingresa 'S' para Sí o 'N' para No. <--\n")

    while True:
        usar_simbolos = input("\n<-- Incluir símbolos (S/N): ").strip().lower()
        if usar_simbolos in ["s", "n"]:
            usar_simbolos = usar_simbolos == "s"
            break
        else:
            print("\n --> Error: Ingresa 'S' para Sí o 'N' para No. <--\n")

    contraseña_generada = generar_contraseña(longitud, usar_mayusculas, usar_numeros, usar_simbolos)

    if contraseña_generada:
        print(f"\n--> Contraseña generada: {contraseña_generada} ")

if __name__ == "__main__":
    procedimiento()
