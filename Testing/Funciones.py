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
    if not all(char.isalpha() or char.isspace() for char in nombre):
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


def accederPerfil(usuario, nombre, archivo="usuarios.json"):
    """
    Accede a un perfil solo si es usuario tipo Administrador o Soporte
       (Si es General o Visitante no tiene acceso)

    Args:
        usuario (str): General / Visitante / Administrador / Soporte
        nombre (str)
        archivo (str): ruta al archivo que actúa como base de datos de usuarios

    Returns:
        str: mensaje indicando el resultado de la operación
    """
    # Verificar si existe la base de datos
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            try:
                usuarios = json.load(file)
            except json.JSONDecodeError:
                return "Error: El archivo de la base de datos está corrupto o vacío."
    else:
        return "Error: La base de datos no existe."
    
    # Verificar que el tipo de perfil sea válido
    perfiles_validos = ["General", "Visitante", "Administrador", "Soporte"]
    if usuario not in perfiles_validos:
        return "Error: Tipo de perfil no válido. Los tipos permitidos son: General, Visitante, Administrador, Soporte."

    # Restringir acceso a perfiles no permitidos
    if usuario not in ["Administrador", "Soporte"]:
        return "Acceso denegado: Solo usuarios Administrador o Soporte pueden acceder."
    else:
        # Verificar si el usuario existe en la base de datos
        if nombre in usuarios:
            return f"Usuario encontrado. Acceso permitido."
        else:
            return f"Usuario no encontrado en la base de datos."

def registrarEmocion(nombre, emocion, archivo="usuarios.json"):
    """
    Registra una emoción asociada a un usuario en la base de datos de usuarios.

    Args:
        nombre (str): Nombre del usuario.
        emocion (str): Emoción a registrar.
        archivo (str): Archivo JSON que actúa como base de datos.

    Returns:
        str: Mensaje indicando el resultado de la operación.
    """
    emociones_validas = ["feliz", "triste", "enojado", "sorprendido", "neutral"]
    if emocion.lower() not in emociones_validas:
        return f"Error: La emoción '{emocion}' no es válida. Las emociones válidas son: {', '.join(emociones_validas)}."

    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            try:
                usuarios = json.load(file)
            except json.JSONDecodeError:
                return "Error: El archivo de la base de datos está corrupto o vacío."
    else:
        return "Error: La base de datos no existe."

    # Verificar si el usuario existe
    if nombre not in usuarios:
        return f"Error: El usuario '{nombre}' no existe en la base de datos."

    # Agregar emoción al perfil del usuario
    if "emociones" not in usuarios[nombre]:
        usuarios[nombre]["emociones"] = []
    usuarios[nombre]["emociones"].append(emocion.lower())

    with open(archivo, "w") as file:
        json.dump(usuarios, file, indent=4)

    return f"Emoción '{emocion}' registrada para el usuario '{nombre}'."


def eliminarUsuario(nombre, archivo="usuarios.json"):
    """
    Elimina un usuario de la base de datos.

    Args:
        nombre (str): Nombre del usuario a eliminar.
        archivo (str): Archivo JSON que actúa como base de datos.

    Returns:
        str: Mensaje indicando el resultado de la operación.
    """
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            try:
                usuarios = json.load(file)
            except json.JSONDecodeError:
                return "Error: El archivo de la base de datos está corrupto o vacío."
    else:
        return "Error: La base de datos no existe."

    if nombre not in usuarios:
        return f"Error: El usuario '{nombre}' no existe en la base de datos."

    usuarios.remove(nombre)
    with open(archivo, "w") as file:
        json.dump(usuarios, file, indent=4)

    return f"Usuario '{nombre}' eliminado correctamente."
