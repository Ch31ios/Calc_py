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

if __name__ == "__main__":
    
    while True:
        
        print("Calculadora de IMC")
        peso = obtener_numero("Ingresa tu peso en kilogramos: ")
        altura = obtener_numero("Ingresa tu altura en metros: ")
        resultado = calcular_imc(peso, altura)
        print(resultado)
        
        continuar = input("¿Deseas calcular otro IMC? (s/n): ")
        continuar = True
        if continuar.lower() != "s":
            continuar = False