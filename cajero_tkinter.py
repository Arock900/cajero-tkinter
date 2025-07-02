import tkinter as tk
from tkinter import messagebox
from proyecto_cajero.login import iniciar_sesion
from proyecto_cajero.usuarios import guardar_usuarios
from proyecto_cajero.funciones import consultar_saldo, depositar_dinero, retirar_dinero
from proyecto_cajero.funciones import cambiar_pin


# ---------- Función para verificar login ----------
def verificar_login():
    nombre_usuario = entry_usuario.get()
    pin = entry_pin.get()
    datos = iniciar_sesion(nombre_usuario, pin)

    if datos:
        mostrar_menu(nombre_usuario, datos)
    else:
        messagebox.showerror("Error", "Usuario o PIN incorrecto")

# ---------- Menú principal tras iniciar sesión ----------
def mostrar_menu(nombre_usuario, datos_usuario):
    menu = tk.Toplevel()
    menu.title("Menú Principal")
    menu.geometry("300x250")

    tk.Label(menu, text=f"Bienvenido, {datos_usuario['nombre']}").pack(pady=10)
    tk.Button(menu, text="Consultar saldo", command=lambda: consultar_saldo(datos_usuario)).pack(pady=5)
    tk.Button(menu, text="Depositar dinero", command=lambda: depositar_dinero(nombre_usuario, datos_usuario, menu)).pack(pady=5)
    tk.Button(menu, text="Retirar dinero", command=lambda: retirar_dinero(nombre_usuario, datos_usuario, menu)).pack(pady=5)
    tk.Button(menu, text="Cambiar PIN", command=lambda: cambiar_pin(nombre_usuario, datos_usuario, menu)).pack(pady=5)
    tk.Button(menu, text="Cerrar sesión", command=menu.destroy).pack(pady=5)

from proyecto_cajero.usuarios import cargar_usuarios, guardar_usuarios

def mostrar_ventana_crear_usuario():
    ventana_crear = tk.Toplevel()
    ventana_crear.title("Crear Usuario")
    ventana_crear.geometry("300x250")

    tk.Label(ventana_crear, text="PIN:").pack(pady=5)
    entry_nuevo_pin = tk.Entry(ventana_crear)
    entry_nuevo_pin.pack()

    tk.Label(ventana_crear, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_crear)
    entry_nombre.pack()

    tk.Label(ventana_crear, text="Saldo inicial:").pack(pady=5)
    entry_saldo = tk.Entry(ventana_crear)
    entry_saldo.pack()

    def crear_usuario():
        pin = entry_nuevo_pin.get()
        nombre = entry_nombre.get()
        try:
            saldo = float(entry_saldo.get())
            if pin == "" or nombre == "":
                raise ValueError("Campos vacíos")

            usuarios = cargar_usuarios()
            if pin in usuarios:
                messagebox.showerror("Error", "Este PIN ya está registrado.")
                return

            usuarios[pin] = {
                "nombre": nombre,
                "saldo": saldo
            }
            guardar_usuarios(usuarios)
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' creado correctamente.")
            ventana_crear.destroy()

        except ValueError:
            messagebox.showerror("Error", "Datos inválidos. Revisa los campos.")

    tk.Button(ventana_crear, text="Crear", command=crear_usuario).pack(pady=10)




    
# ---------- Interfaz principal ----------
ventana = tk.Tk()
ventana.title("Cajero Automático")
ventana.geometry("300x200")

tk.Label(ventana, text="Usuario:").pack(pady=5)
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text="PIN:").pack(pady=5)
entry_pin = tk.Entry(ventana, show="*")
entry_pin.pack()

tk.Button(ventana, text="Iniciar sesión", command=verificar_login).pack(pady=10)
tk.Button(ventana,text="crear nuevo usuario",command=mostrar_ventana_crear_usuario).pack(pady=5)
ventana.mainloop()
