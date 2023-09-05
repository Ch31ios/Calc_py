from tkinter import *

indice=0

def calculadora():
    
# Modulo que iniciar nuestra ventana
    root=Tk()
    root.title("Calculadora")



    # Creando los input de entrada y le daremos orden a las filas
    display=Entry(root)
    display.grid(row=1, columnspan=6,)# Orden de oeste a este 

    # Declaramos nuestras funciones

    # Capturar numeros
    def get_numbers(n):
        global indice
        display.insert(indice, n)
        indice+=1
        
    # Operadores matematicos

    # Esta variable tiene la funcion de agregar en la parte visual, las operaciones para poder llevar un orden a la hora de hacer la operacion
    def   get_operation(operator) : 
        global indice
        operator_lenght= len(operator)
        display.insert(indice,operator)
        indice+=operator_lenght
        
    # Esta funcion es para limpiar la pantalla
    def clear_display():
        display.delete(0, END)
        
    # Esta funcion es para eliminar un solo elemento y darle funcion a la flecha de borrar
    def undo():
        display_state= display.get()
        if len(display_state):
            display_new_state=display_state[:-1]
            clear_display()
            display.insert(0, display_new_state)
        else:
            clear_display()
            display.insert(0, 'Error') 
        
    # Funcion para calcular
    def calculate():
        display_state = display.get()
        try:
            result = eval(display_state)
            clear_display()
            display.insert(0, result)
        except Exception:
            clear_display()
            display.insert(0, 'Error')

    def clear_display():
        display.delete(0, END)


        

    # Botones numericos
    Button(root, text="1" , command=lambda:get_numbers(1)).grid(row="2", column=0,sticky=W+E)
    Button(root, text="2" , command=lambda:get_numbers(2)).grid(row="2", column=1,sticky=W+E)
    Button(root, text="3" , command=lambda:get_numbers(3)).grid(row="2", column=2,sticky=W+E)

    Button(root, text="4", command=lambda:get_numbers(4)).grid(row="3", column=0,sticky=W+E)
    Button(root, text="5", command=lambda:get_numbers(5)).grid(row="3", column=1,sticky=W+E) #Separamos todo por filas y columnas
    Button(root, text="6", command=lambda:get_numbers(6)).grid(row="3", column=2,sticky=W+E)

    Button(root, text="7", command=lambda:get_numbers(7)).grid(row="4", column=0,sticky=W+E)
    Button(root, text="8", command=lambda:get_numbers(8)).grid(row="4", column=1,sticky=W+E)
    Button(root, text="9", command=lambda:get_numbers(9)).grid(row="4", column=2,sticky=W+E)

    # Botones interactivos
    Button(root, text="AC", command=lambda: clear_display()).grid(row="5", column=0,sticky=W+E)
    Button(root, text="0" , command=lambda:get_numbers(0)).grid(row="5", column=1,sticky=W+E)
    Button(root, text="%" , command=lambda: get_operation("%")).grid(row="5", column=2,sticky=W+E)

    Button(root, text="+", command=lambda: get_operation("+")).grid(row="2", column=3,sticky=W+E)
    Button(root, text="-", command=lambda: get_operation("-")).grid(row="3", column=3,sticky=W+E)
    Button(root, text="*", command=lambda: get_operation("*")).grid(row="4", column=3,sticky=W+E)
    Button(root, text="/", command=lambda: get_operation("/")).grid(row="5", column=3,sticky=W+E)

    Button(root, text="🡨", command=lambda: undo()).grid(row="2", column=4,sticky=W+E, columnspan=2)
    Button(root, text="expo", command=lambda: get_operation("**")).grid(row="3", column=4,sticky=W+E)
    Button(root, text="^2", command=lambda: get_operation("**2")).grid(row="3", column=5,sticky=W+E)
    Button(root, text="(", command=lambda: get_operation("(")).grid(row="4", column=4,sticky=W+E)
    Button(root, text=")", command=lambda: get_operation(")")).grid(row="4", column=5,sticky=W+E)
    Button(root, text="=", command=lambda: calculate()).grid(row="5", column=4,sticky=W+E, columnspan=2)



    root.mainloop()