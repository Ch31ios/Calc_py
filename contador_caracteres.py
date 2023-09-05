#Contador Caracteres v1
from menú import finalizar_programa
def contador_caracteres():

    while True:
        phrase = input('Ingrese una palabra y/o frase: ')
        count =len(phrase)
        print(f'La frase tiene {count} caracteres')

        again = input('¿Quiere ingresar otra frase? (s/n) ')
        if again.lower() == 'n':
            finalizar_programa()


