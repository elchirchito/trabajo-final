from tkinter import Tk, Label, StringVar, CENTER, ttk, messagebox

def convertir_temperatura():
    try:
        temp = entrada_valor.get()
        if not temp.isdigit():
            raise ValueError("Debe ingresar solo números")
        
        temp = float(temp)
        unidad_desde = combo_desde.get()
        unidad_hasta = combo_hasta.get()

        if unidad_desde == unidad_hasta:
            temp_convertida = temp
        elif unidad_desde == "Celsius" and unidad_hasta == "Fahrenheit":
            temp_convertida = (temp * 9/5) + 32
        elif unidad_desde == "Fahrenheit" and unidad_hasta == "Celsius":
            temp_convertida = (temp - 32) * 5/9
        else:
            raise ValueError("Conversión no soportada")
        
        etiqueta_resultado.config(text=f"{temp_convertida:.2f} {unidad_hasta}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("convertidor temperatura")
root.geometry("400x200")
root.config(bg="green")

# StringVars
entrada_valor = StringVar()
unidad_desde = StringVar()
unidad_hasta = StringVar()

# Widgets
etiqueta_entrada = Label(root, text="Ingrese valor:", bg="green", fg="white")
entrada = ttk.Entry(root, textvariable=entrada_valor)
combo_desde = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly", textvariable=unidad_desde)
combo_desde.set("Celsius")
combo_hasta = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly", textvariable=unidad_hasta)
combo_hasta.set("Fahrenheit")
boton_convertir = ttk.Button(root, text="Convertir", command=convertir_temperatura)
etiqueta_resultado = Label(root, text="", bg="green", fg="white")

# Layout
etiqueta_entrada.pack(pady=5)
entrada.pack(pady=5)
combo_desde.pack(pady=5)
combo_hasta.pack(pady=5)
boton_convertir.pack(pady=10)
etiqueta_resultado.pack(pady=10)

root.mainloop()
