from proyecto_cajero.usuarios import cargar_usuarios

def iniciar_sesion(nombre_usuario, pin):
    usuarios = cargar_usuarios()
    if nombre_usuario in usuarios and str(pin) == str(nombre_usuario):
        return usuarios[nombre_usuario]
    return None

    
