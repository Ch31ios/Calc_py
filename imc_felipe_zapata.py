
def obtener_numero(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Solo se permiten numeros...")

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "El peso y la altura deben ser valores positivos."

    imc = peso / (altura ** 2)
    return imc

def procedimiento():
    continuar1 = True
    while continuar1:
        
        print("\nCalculadora de IMC\n")
        peso = obtener_numero("Ingresa tu peso en kilogramos: ")
        altura = obtener_numero("Ingresa tu altura en metros: ")
        resultado = calcular_imc(peso, altura)
        
        if isinstance(resultado, float):
            print(f"")
            if resultado < 18.5:
                print(f"Tu IMC es: {round(resultado):.2f} - tienes bajo peso.\n")
            elif resultado < 24.9:
                print(f"Tu IMC es: {round(resultado):.2f} - tu peso es saludable.\n")
            elif resultado < 29.9:
                print(f"Tu IMC es: {round(resultado):.2f} - tienes sobrepeso.\n")
            else:
                print(f"Tu IMC es: {round(resultado):.2f} - tienes obesidad.\n")
        else:
            print(resultado)
            
        continuar = input("\n¿Deseas calcular otro IMC? (s/n): ")
        
        if continuar.lower() != "s":
            continuar1 = False
                
if __name__ == "__main__":
    procedimiento()