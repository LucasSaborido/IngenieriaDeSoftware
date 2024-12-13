import json
import os

def crearUsuario(nombre, archivo="usuarios.json"):
    """
    Crea un user si no existe y el nombre es válido (sólo letras)

    Args:
        nombre (str)
        archivo (str): ruta al archivo que actúa como base de datos de usuarios

    Returns:
        str: mensaje indicando el resultado de la operación
    """
    if not nombre.isalpha():
        return "El nombre de usuario sólo debe contener letras"
    if os.path.exists(archivo):
        with open(archivo,"r") as file:
            usuarios=json.load(file)
    else:
        usuarios = []
    
    if nombre in usuarios:
        return "El usuario ya existe"
    
    usuarios.append(nombre)
    with open(archivo, "w") as file:
        json.dump(usuarios,file,indent=4)
    return "Usuario creado exitosamente"