import tkinter as tk
from tkinter import messagebox
import conversiones

# A continuación se presenta la clase interface
class Interface:
    # Recibe cómo parámetro la ventana sobre la cuál se manejará
    def __init__(self, window):
        self.window = window

        # Se agregan las 3 etiquetas y cuadros de entrada de datos:
        l1 = tk.Label(self.window, text = 'Número: ')
        l1.grid(row = 0, column = 0)
        e1 = tk.Entry(self.window, bd = 5)
        e1.grid(row = 0, column = 1)

        l2 = tk.Label(self.window, text = 'Base original: ')
        l2.grid(row = 1, column = 0)
        e2 = tk.Entry(self.window, bd = 5)
        e2.grid(row = 1, column = 1)

        l3 = tk.Label(self.window, text = 'Nueva base: ')
        l3.grid(row = 2, column = 0)
        e3 = tk.Entry(self.window, bd = 5)
        e3.grid(row = 2, column = 1)

        # Botón para solicitar la obtención del resultado:
        giveResult = tk.Button(self.window, text="Resultado", width=10, command = lambda: self.calculo(e1.get(), e2.get(), e3.get()))
        giveResult.grid(row = 3, column = 1)
    
    def calculo(self, num, basIni, basFin):
        # Se intenta ejecutar el algoritmo de cambio de base, sino se manda un mensaje de datos inválidos:
        try:
            numero = num
            baseNumero = int(basIni)
            baseNueva = int(basFin)
            resultado = conversiones.base_r_a_base_10( numero, baseNumero )
            resultado = conversiones.base_10_a_base_r( resultado, baseNueva)
            messagebox.showinfo("Resultado", "El numero" + str(num) + " en base " + str(basFin) + " es: " + str(resultado))
        except Exception as e: 
            messagebox.showerror(title = "Erroe", message = "Datos inválidos")
            return

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conversor de bases")
    program = Interface(root)
    root.mainloop()