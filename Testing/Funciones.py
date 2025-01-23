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
    #Verificar que el nombre no está vacío

    if not nombre.strip():
        return "El nombre de usuario sólo debe contener letras"
    
    #Eliminar espacios al inicio y al final
    nombre = nombre.strip()

    #Comprobar si sólo tiene letras y espacios
    if not all(char.isalpha() or char.isspace() for char in nombre):
        return "El nombre de usuario sólo debe contener letras"
    
    #Abrir el archivo de usuarios o crearlo si no existe
    if os.path.exists(archivo):
        with open(archivo,"r") as file:
            usuarios=json.load(file)
    else:
        usuarios = []
    
    #Comprobar si el nombre de usuario ya está en uso
    if nombre in usuarios:
        return "El usuario ya existe"
    
    #Guardar en el archivo de usuarios
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
    # Lista de emociones válidas
    emociones_validas = ["feliz", "triste", "enojado", "sorprendido", "neutral"]
    if emocion.lower() not in emociones_validas:
        return f"Error: La emoción '{emocion}' no es válida. Las emociones válidas son: {', '.join(emociones_validas)}."

    # Manejar la ausencia del archivo creando un archivo vacío
    if not os.path.exists(archivo):
        with open(archivo, "w") as file:
            json.dump({}, file)

    # Cargar datos del archivo
    try:
        with open(archivo, "r") as file:
            usuarios = json.load(file)
    except json.JSONDecodeError:
        return "Error: El archivo de la base de datos está corrupto o vacío."

    # Verificar si el usuario existe
    if nombre not in usuarios:
        return f"Error: El usuario '{nombre}' no existe en la base de datos."

    # Agregar emoción al perfil del usuario
    if "emociones" not in usuarios[nombre]:
        usuarios[nombre]["emociones"] = []
    usuarios[nombre]["emociones"].append(emocion.lower())

    # Guardar los cambios en el archivo
    with open(archivo, "w") as file:
        json.dump(usuarios, file, indent=4)

    return f"Emoción '{emocion}' registrada para el usuario '{nombre}'."

#Función Javier Ortega
def reconocimientoEmocion(texto, nombre, archivo="usuarios.json"):
    """
    Extrae las emociones de una frase y las registra para un usuario.

    Args:
        texto (str): Frase de texto en la que se buscan emociones.
        nombre (str): Nombre del usuario.
        archivo (str): Archivo JSON que actúa como base de datos.

    Returns:
        str: Mensajes indicando el resultado de la operación para cada emoción encontrada.
    """
    emociones_validas = ["feliz", "triste", "enojado", "sorprendido", "neutral"]
    respuestas = []
    
    # Convertir el texto a minúsculas y buscar las emociones
    texto_lower = texto.lower()

    for emocion in emociones_validas:
        if emocion in texto_lower:
            # Llamar a la función registrarEmocion para cada emoción encontrada
            resultado = registrarEmocion(nombre, emocion, archivo)
            respuestas.append(resultado)
    
    # Retornar los mensajes generados por registrarEmocion
    if respuestas:
        return "\n".join(respuestas)
    else:
        return "No se encontraron emociones válidas en el texto."


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

# Function for test cases of Lukas
def generate_personalised_response(name, file_path="users.json"):
    """
    Generates a personalized response for the user based on their emotional history.

    Args:
        name (str): Name of the user.
        file_path (str): Path to the JSON file serving as the user database.

    Returns:
        str: A personalised response or an error message.
    """
    if not os.path.exists(file_path):
        return "Error: The database does not exist."

    # Load the database
    with open(file_path, "r") as file:
        try:
            users = json.load(file)
        except json.JSONDecodeError:
            return "Error: The database file is corrupted or empty."

    # Check if the user exists
    if name not in users:
        return f"Error: The user '{name}' does not exist in the database."

    # Get the user's emotional history
    user_data = users.get(name, {})
    emotions = user_data.get("emotions", [])
    if not emotions:
        return f"Hello {name}, it seems I don't have enough information about your emotions to personalize my response."

    # Analyze the predominant emotion
    predominant_emotion = max(set(emotions), key=emotions.count)

    # Generate a personalised response based on the predominant emotion
    responses = {
        "happy": f"Hello {name}! I'm glad to see you're feeling happy. How can I assist you today?",
        "sad": f"Hi {name}, I noticed you've been feeling a bit sad lately. I'm here to listen if you want to talk.",
        "angry": f"Hi {name}, it seems something might have upset you. Is there anything I can do to make your day better?",
        "surprised": f"Hi {name}! Has something exciting happened? I'd love to hear more about it.",
        "neutral": f"Hello {name}, I hope you're having a good day. How can I help you?"
    }

    return responses.get(predominant_emotion, f"Hello {name}, I'm here to assist you with whatever you need.")

# Example structure of "users.json":
# {
#   "John": {
#       "age": 30,
#       "important_data": "Prefers coffee over tea",
#       "emotions": ["happy", "sad", "happy"]
#   },
#   "Anna": {
#       "age": 25,
#       "important_data": "Enjoys classical music",
#       "emotions": ["neutral", "neutral", "surprised"]
#   }
# }
