import tkinter as tk
from tkinter import messagebox
from proyecto_cajero.usuarios import guardar_usuarios, cargar_usuarios

def consultar_saldo(datos_usuario):
    saldo = datos_usuario["saldo"]
    messagebox.showinfo("Saldo actual", f"Tu saldo es: ${saldo:.2f}")

def depositar_dinero(nombre_usuario, datos_usuario, ventana):
    def realizar_deposito():
        try:
            monto = float(entry_monto.get())
            if monto <= 0:
                raise ValueError
            datos_usuario["saldo"] += monto
            usuarios = cargar_usuarios()
            usuarios[nombre_usuario] = datos_usuario
            guardar_usuarios(usuarios)
            messagebox.showinfo("Éxito", f"Se depositaron ${monto:.2f}")
            ventana_deposito.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un monto válido")

    ventana_deposito = tk.Toplevel(ventana)
    ventana_deposito.title("Depositar Dinero")
    ventana_deposito.geometry("250x120")

    tk.Label(ventana_deposito, text="Monto a depositar:").pack(pady=5)
    entry_monto = tk.Entry(ventana_deposito)
    entry_monto.pack()

    tk.Button(ventana_deposito, text="Depositar", command=realizar_deposito).pack(pady=10)

def retirar_dinero(nombre_usuario, datos_usuario, ventana):
    def realizar_retiro():
        try:
            monto = float(entry_monto.get())
            if monto <= 0:
                raise ValueError
            if monto > datos_usuario["saldo"]:
                messagebox.showerror("Error", "Saldo insuficiente")
            else:
                datos_usuario["saldo"] -= monto
                usuarios = cargar_usuarios()
                usuarios[nombre_usuario] = datos_usuario
                guardar_usuarios(usuarios)
                messagebox.showinfo("Éxito", f"Se retiraron ${monto:.2f}")
                ventana_retiro.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un monto válido")

    ventana_retiro = tk.Toplevel(ventana)
    ventana_retiro.title("Retirar Dinero")
    ventana_retiro.geometry("250x120")

    tk.Label(ventana_retiro, text="Monto a retirar:").pack(pady=5)
    entry_monto = tk.Entry(ventana_retiro)
    entry_monto.pack()

    tk.Button(ventana_retiro, text="Retirar", command=realizar_retiro).pack(pady=10)

def cambiar_pin(nombre_usuario, datos_usuario, ventana):
    def realizar_cambio():
        nuevo_pin = entry_nuevo_pin.get()
        if not nuevo_pin:
            messagebox.showerror("Error", "PIN no puede estar vacío")
            return

        usuarios = cargar_usuarios()
        if nuevo_pin in usuarios:
            messagebox.showerror("Error", "Ese PIN ya está registrado")
            return

        usuarios.pop(nombre_usuario)
        usuarios[nuevo_pin] = datos_usuario
        guardar_usuarios(usuarios)
        messagebox.showinfo("Éxito", "PIN cambiado exitosamente")
        ventana_cambio.destroy()

    ventana_cambio = tk.Toplevel(ventana)
    ventana_cambio.title("Cambiar PIN")
    ventana_cambio.geometry("250x120")

    tk.Label(ventana_cambio, text="Nuevo PIN:").pack(pady=5)
    entry_nuevo_pin = tk.Entry(ventana_cambio)
    entry_nuevo_pin.pack()

    tk.Button(ventana_cambio, text="Cambiar", command=realizar_cambio).pack(pady=10)
