import tkinter as tk
from tkinter import messagebox
import conversiones

class Interface:
    def __init__(self, window):
        l1 = tk.Label(window, text = 'Número: ')
        l1.grid(row = 0, column = 0)
        e1 = tk.Entry(window, bd = 5)
        e1.grid(row = 0, column = 1)

        l2 = tk.Label(window, text = 'Base original: ')
        l2.grid(row = 1, column = 0)
        e2 = tk.Entry(window, bd = 5)
        e2.grid(row = 1, column = 1)

        l3 = tk.Label(window, text = 'Nueva base: ')
        l3.grid(row = 2, column = 0)
        e3 = tk.Entry(window, bd = 5)
        e3.grid(row = 2, column = 1)

        giveResult = tk.Button(window, text="Resultado", width=10, command = lambda: self.calculo(e1.get(), e2.get(), e3.get()))
        giveResult.grid(row = 3, column = 1)
    
    def calculo(self, num, basIni, basFin):
        numero = num
        baseNumero = int(basIni)
        baseNueva = int(basFin)
        resultado = conversiones.base_r_a_base_10( numero, baseNumero )
        resultado = conversiones.base_10_a_base_r( resultado, baseNueva)
        messagebox.showinfo("Resultado", "El numero" + str(num) + " en base " + str(basFin) + " es: " + str(resultado))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conversor de bases")
    program = Interface(root)
    root.mainloop()