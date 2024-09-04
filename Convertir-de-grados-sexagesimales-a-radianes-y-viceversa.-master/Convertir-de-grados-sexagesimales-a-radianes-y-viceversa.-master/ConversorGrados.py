import tkinter as tk
from tkinter import messagebox
import math


class AngleConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Ángulos")

        # Etiquetas y entradas para el ángulo y la unidad
        self.label_angle = tk.Label(root, text="Ingresa el ángulo:")
        self.label_angle.grid(row=0, column=0)
        self.entry_angle = tk.Entry(root)
        self.entry_angle.grid(row=0, column=1)

        self.label_unit = tk.Label(root, text="Selecciona la unidad:")
        self.label_unit.grid(row=1, column=0)
        self.unit_var = tk.StringVar(value="grados")
        self.radio_degrees = tk.Radiobutton(root, text="Grados", variable=self.unit_var, value="grados")
        self.radio_degrees.grid(row=1, column=1)
        self.radio_radians = tk.Radiobutton(root, text="Radianes", variable=self.unit_var, value="radianes")
        self.radio_radians.grid(row=1, column=2)

        # Botón para realizar la conversión
        self.convert_button = tk.Button(root, text="Convertir", command=self.convert_angle)
        self.convert_button.grid(row=2, column=0, columnspan=3)

    def convert_angle(self):
        try:
            angle = float(self.entry_angle.get())
            unit = self.unit_var.get()

            converter = AngleConverter(angle, unit)
            result = converter.convert()
            messagebox.showinfo("Resultado", result)

        except ValueError as e:
            messagebox.showerror("Error", str(e))


class AngleConverter:
    def __init__(self, angle, unit):
        self.angle = angle
        self.unit = unit.lower()

    def to_radians(self):
        if self.unit == "grados":
            return self.angle * (math.pi / 180)
        else:
            raise ValueError("La unidad debe ser 'grados' para convertir a radianes.")

    def to_degrees(self):
        if self.unit == "radianes":
            return self.angle * (180 / math.pi)
        else:
            raise ValueError("La unidad debe ser 'radianes' para convertir a grados.")

    def convert(self):
        if self.unit == "grados":
            converted_angle = self.to_radians()
            return f"{self.angle} grados es igual a {converted_angle:.5f} radianes."
        elif self.unit == "radianes":
            converted_angle = self.to_degrees()
            return f"{self.angle} radianes es igual a {converted_angle:.5f} grados."
        else:
            raise ValueError("Unidad no reconocida. Usa 'grados' o 'radianes'.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AngleConverterApp(root)
    root.mainloop()