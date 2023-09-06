import os

def Conversor():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = """
¡Bienvenido al conversor de monedas!

1 - Pesos Colombianos a Dólares
2 - Dólares a Pesos Colombianos
3 - Finalizar conversor
    """

    # Función para convertir Pesos Colombianos a Dólares
    def pesos_a_dolares():
        pesos = float(input("\n ¿Cuántos Pesos Colombianos tienes?: "))
        valor_dolar = 1 / 4086
        dolares = pesos * valor_dolar
        dolares = round(dolares, 2)
        print(f"Tienes ${dolares} Dólares")

    # Función para convertir Dólares a Pesos Colombianos
    def dolares_a_pesos():
        dolares = float(input("¿Cuántos Dólares tienes?: "))
        valor_pesos = 4086  
        pesos = dolares * valor_pesos
        print(f"Tienes ${pesos} Pesos Colombianos")

    while True:
        print(menu)
        opcion = input("Elige una opción (1/2/3): ")

        if opcion == '1':
            pesos_a_dolares()
        elif opcion == '2':
            dolares_a_pesos()
        elif opcion == '3':
            print("Gracias por usar el conversor de monedas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Llamamos a la función principal del conversor
Conversor()
