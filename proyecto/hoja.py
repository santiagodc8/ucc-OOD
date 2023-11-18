import tkinter as tk
import re

class Celda:
    def __init__(self, valor=""):
        self.valor = valor

class HojaDeCalculo:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [[Celda() for _ in range(columnas)] for _ in range(filas)]

class HojaDeCalculoApp:
    def __init__(self, root, hoja_de_calculo):
        self.root = root
        self.hoja_de_calculo = hoja_de_calculo
        self.crear_interfaz()

    def crear_interfaz(self):
        for i in range(self.hoja_de_calculo.filas):
            for j in range(self.hoja_de_calculo.columnas):
                celda = self.hoja_de_calculo.celdas[i][j]
                entry = tk.Entry(self.root, width=10)
                entry.grid(row=i, column=j)
                entry.insert(0, celda.valor)
                entry.bind("<FocusOut>", lambda event, i=i, j=j: self.actualizar_celda(event, i, j))

    def actualizar_celda(self, event, i, j):
        nuevo_valor = event.widget.get()
        self.hoja_de_calculo.celdas[i][j].valor = nuevo_valor

        # Verificar si el nuevo valor es una operación matemática y calcular el resultado
        if re.match(r'^[+\-*/\d ]+$', nuevo_valor):
            try:
                resultado = eval(nuevo_valor)
                event.widget.delete(0, tk.END)
                event.widget.insert(0, str(resultado))
            except:
                # En caso de error en la evaluación de la expresión
                pass

if __name__ == "__main__":
    filas = 5
    columnas = 5
    hoja_de_calculo = HojaDeCalculo(filas, columnas)

    root = tk.Tk()
    app = HojaDeCalculoApp(root, hoja_de_calculo)
    root.mainloop()
