import json

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def crear_nuevo_usuario(usuarios):
    pin = input("Elige una nueva clave numérica (PIN): ")
    if pin in usuarios:
        print("Ese PIN ya existe. Intenta con otro.")
        return

    nombre = input("Ingresa el nombre del usuario: ")

    try:
        saldo_inicial = float(input("Ingresa el saldo inicial: "))
    except ValueError:
        print("Saldo inválido. Debe ser un número.")
        return

    usuarios[pin] = {
        "nombre": nombre,
        "saldo": saldo_inicial
    }

    guardar_usuarios(usuarios)
    print(f"Usuario '{nombre}' creado exitosamente con PIN {pin}.")
    