import unittest
import json
import os
from Funciones import *

# Tests creados por Lucas
class testNombre(unittest.TestCase):
        def testNumeros(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("Juan123"), "El nombre de usuario sólo debe contener letras" , "No debe contener números")
        def testSimbolos(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("Juan@#|"), "El nombre de usuario sólo debe contener letras" , "No puede contener símbolos")
        def testAcentos(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario ("José"), "Usuario creado exitosamente", "Debería poder crearse con acentos")
        def testMismoUsuario(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            crearUsuario("María")
            self.assertEqual(crearUsuario("María"), "El usuario ya existe", "No puede haber usuarios repetidos")
        def testConApellidos(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("José Domínguez Rodríguez"),"Usuario creado exitosamente", "Los usuarios deberían poder añadir sus apellidos")

        #Tests creados por Chatgpt

        def test_nombre_vacio(self):
            """Prueba que no se pueda crear un usuario con un nombre vacío."""
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario(""), "El nombre de usuario sólo debe contener letras", "No debe permitir nombres vacíos")

        def test_espacios_solo(self):
            """Prueba que no se pueda crear un usuario con solo espacios."""
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("   "), "El nombre de usuario sólo debe contener letras", "No debe permitir nombres con solo espacios")
        
        def test_nombre_con_espacios_inicio_y_fin(self):
            """Prueba nombres válidos con espacios al inicio y al final."""
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("  Carlos Pérez  "), "Usuario creado exitosamente", "Debe permitir nombres con espacios al inicio y al final")

        def test_nombre_con_espacios_consecutivos(self):
            """Prueba nombres válidos con múltiples espacios consecutivos."""
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(crearUsuario("Juan  Carlos"), "Usuario creado exitosamente", "Debe permitir nombres con múltiples espacios consecutivos")
        
        def test_archivo_inexistente(self):
            """Prueba cuando el archivo no existe."""
            if os.path.exists("usuarios.json"):
                os.remove("usuarios.json")
            self.assertEqual(crearUsuario("Pedro"), "Usuario creado exitosamente", "Debe manejar la creación de un archivo inexistente correctamente")
        

# Tests creados por Laura
class testAcceso(unittest.TestCase):
        def testGeneral(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(accederPerfil("General","Juan", "usuarios.json"), "Acceso denegado: Solo usuarios Administrador o Soporte pueden acceder.")     
        def testEncontrado(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            crearUsuario("Pedro")
            self.assertEqual(accederPerfil("Administrador","Pedro", "usuarios.json"), "Usuario encontrado. Acceso permitido.")
        def testNOEncontrado(self):
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(accederPerfil("Administrador","Pedro", "usuarios.json"), "Usuario no encontrado en la base de datos.") 
        def testSinUsuario(self):  
            with open("usuarios.json", "w") as file:
                json.dump([], file, indent=4)
            self.assertEqual(accederPerfil("","Pedro", "usuarios.json"), "Error: Tipo de perfil no válido. Los tipos permitidos son: General, Visitante, Administrador, Soporte.") 
        def testBaseDatosInexistente(self):
            if os.path.exists("no_existe.json"):
                os.remove("no_existe.json")
            self.assertEqual(accederPerfil("Administrador", "Pedro", "no_existe.json"), "Error: La base de datos no existe.")
        
        #Test creados con IA
        def testBaseDatosCorrupta(self):
            with open("usuarios.json", "w") as file:
                file.write("Contenido no JSON")  # Archivo corrupto
            self.assertEqual(accederPerfil("Administrador", "Pedro", "usuarios.json"), "Error: El archivo de la base de datos está corrupto o vacío.")

        def testSoporteAcceso(self):
            with open("usuarios.json", "w") as file:
             json.dump(["Juan"], file, indent=4)
            self.assertEqual(accederPerfil("Soporte", "Juan", "usuarios.json"), "Usuario encontrado. Acceso permitido.")

        def testNombreUsuarioVacio(self):
            with open("usuarios.json", "w") as file:
             json.dump(["Juan"], file, indent=4)
            self.assertEqual(accederPerfil("Administrador", "", "usuarios.json"), "Usuario no encontrado en la base de datos.")

        def testBaseDatosVacia(self):
            with open("usuarios.json", "w") as file:
             json.dump([], file, indent=4)  # Base de datos vacía
            self.assertEqual(accederPerfil("Administrador", "Pedro", "usuarios.json"), "Usuario no encontrado en la base de datos.")

        def testPerfilVisitante(self):
            with open("usuarios.json", "w") as file:
             json.dump(["Pedro"], file, indent=4)  # Usuario "Pedro" en la base de datos
            self.assertEqual(accederPerfil("Visitante", "Pedro", "usuarios.json"),  "Acceso denegado: Solo usuarios Administrador o Soporte pueden acceder.")
        
        def testPerfilInvalido(self):
            with open("usuarios.json", "w") as file:
             json.dump([], file, indent=4)
            self.assertEqual(accederPerfil("Invalido", "Pedro", "usuarios.json"), "Error: Tipo de perfil no válido. Los tipos permitidos son: General, Visitante, Administrador, Soporte.")
"""
    COMENTARIOS sobre los tests generados con IA.

    Al pedir a chatgpt que genere más tests para la función accederPerfil 
    sigue la misma estructura de tests que la introducida como referencia pero algunos tests no funcionan correctamente.
    En concreto, ha sido necesario corregir el test testNombreUsuarioVacio.
    
"""
#Test creados por Mateo
class testRegistrarEmocion(unittest.TestCase):
    def setUp(self):
        """
        Se ejecuta antes de cada prueba para garantizar que el archivo de usuarios
        esté correctamente inicializado y sin interferencias.
        """
        with open("usuarios.json", "w") as file:
            json.dump({}, file, indent=4)

    def testRegistroCorrecto(self):
        # Inicializar el archivo con un usuario válido
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)

        self.assertEqual(
            registrarEmocion("Juan", "feliz"),
            "Emoción 'feliz' registrada para el usuario 'Juan'.",
            "Debería registrar correctamente la emoción"
        )

    def testAgregarMultiplesEmociones(self):
        # Inicializar el archivo con un usuario válido
        with open("usuarios.json", "w") as file:
            json.dump({"Luis": {"emociones": []}}, file, indent=4)

        registrarEmocion("Luis", "feliz")
        registrarEmocion("Luis", "triste")

        with open("usuarios.json", "r") as file:
            data = json.load(file)
        self.assertEqual(
            data["Luis"]["emociones"],
            ["feliz", "triste"],
            "Debería agregar múltiples emociones para un usuario existente"
        )

    def testUsuarioNoExistente(self):
        # Archivo inicializado pero sin el usuario específico
        with open("usuarios.json", "w") as file:
            json.dump({}, file, indent=4)

        self.assertEqual(
            registrarEmocion("Pedro", "feliz"),
            "Error: El usuario 'Pedro' no existe en la base de datos.",
            "Debería devolver un error si el usuario no existe"
        )

    def testEmocionInvalida(self):
        # Inicializar el archivo con un usuario válido
        with open("usuarios.json", "w") as file:
            json.dump({"Maria": {"emociones": []}}, file, indent=4)

        self.assertEqual(
            registrarEmocion("Maria", "confundido"),
            "Error: La emoción 'confundido' no es válida. Las emociones válidas son: feliz, triste, enojado, sorprendido, neutral.",
            "Debería detectar emociones inválidas"
        )

    def testArchivoCorrupto(self):
        # Simula un archivo corrupto
        with open("usuarios.json", "w") as file:
            file.write("Texto no JSON")

        self.assertEqual(
            registrarEmocion("Juan", "feliz"),
            "Error: El archivo de la base de datos está corrupto o vacío.",
            "Debería manejar archivos corruptos correctamente"
        )

    # Test creados por IA
    def testAgregarEmocionMayusculas(self):
        # Inicializar el archivo con un usuario válido
        with open("usuarios.json", "w") as file:
            json.dump({"Ana": {"emociones": []}}, file, indent=4)

        self.assertEqual(
            registrarEmocion("Ana", "FELIZ"),
            "Emoción 'feliz' registrada para el usuario 'Ana'.",
            "Debería registrar correctamente emociones en mayúsculas"
        )

    def testAgregarEmocionDuplicada(self):
        # Inicializar el archivo con un usuario válido y una emoción previa
        with open("usuarios.json", "w") as file:
            json.dump({"Carlos": {"emociones": ["feliz"]}}, file, indent=4)

        registrarEmocion("Carlos", "feliz")
        with open("usuarios.json", "r") as file:
            data = json.load(file)
        self.assertEqual(
            data["Carlos"]["emociones"],
            ["feliz", "feliz"],
            "Debería permitir registrar emociones duplicadas"
        )

    def testRegistrarEmocionNombreVacio(self):
        # Inicializar el archivo con usuarios vacíos
        with open("usuarios.json", "w") as file:
            json.dump({}, file, indent=4)

        self.assertEqual(
            registrarEmocion("", "feliz"),
            "Error: El usuario '' no existe en la base de datos.",
            "Debería manejar el caso de un nombre de usuario vacío"
        )

    def testRegistrarEmocionNombreConEspacios(self):
        # Inicializar el archivo con un usuario válido
        with open("usuarios.json", "w") as file:
            json.dump({"Maria Fernanda": {"emociones": []}}, file, indent=4)

        self.assertEqual(
            registrarEmocion("Maria Fernanda", "triste"),
            "Emoción 'triste' registrada para el usuario 'Maria Fernanda'.",
            "Debería registrar correctamente emociones para nombres con espacios"
        )

    def testRegistrarEmocionSinArchivo(self):
        # Asegurar que el archivo no exista antes de la prueba
        if os.path.exists("usuarios.json"):
            os.remove("usuarios.json")

        self.assertEqual(
            registrarEmocion("Pedro", "feliz"),
            "Error: El archivo de la base de datos está corrupto o vacío.",
            "Debería manejar el caso en que el archivo no exista"
        )
#Test creados por Javier O.
class testReconocimientoEmocion(unittest.TestCase):
     def testReconocimientoEmocionCorrecta(self):
        crearUsuario("Juan")
        self.assertEqual(
                reconocimientoEmocion("Hoy estoy muy feliz porque todo ha ido bien.", "Juan", "usuarios.json"),
                "Emoción 'feliz' registrada para el usuario 'Juan'.","Debería registrar correctamente la emoción"
        )

     def testReconocimientoMultiplesEmociones(self):
        crearUsuario("Luis")
        self.assertEqual(
                reconocimientoEmocion("Me siento triste y enojado por lo que pasó ayer.", "Luis", "usuarios.json"),
                "Emoción 'triste' registrada para el usuario 'Luis'.\nEmoción 'enojado' registrada para el usuario 'Luis'.",
                "Debería agregar ambas emociones al usuario 'Luis'."
        )

     def testReconocimientoNoEmociones(self):
        crearUsuario("Pedro")
        self.assertEqual(
            reconocimientoEmocion("Hoy he pasado un buen día.", "Pedro", "usuarios.json"),
            "No se encontraron emociones válidas en el texto.",
            "Debería devolver un mensaje indicando que no se detectaron emociones."
        )

     def testReconocimientoEmocionInvalida(self):
        crearUsuario("Maria")
        self.assertEqual(
            reconocimientoEmocion("Me siento confundida.", "Maria", "usuarios.json"),
            "No se encontraron emociones válidas en el texto.",
            "Debería devolver un mensaje indicando que no se detectaron emociones."
        )

     def testReconocimientoConTextoVacio(self):
        crearUsuario("Sara")
        self.assertEqual(
            reconocimientoEmocion("", "Sara", "usuarios.json"),
            "No se encontraron emociones válidas en el texto.",
            "Debería devolver un mensaje indicando que no se detectaron emociones."
        )

    # Tests generados por la IA
     def testReconocimientoEmocionFeliz(self):
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)
        self.assertEqual(
            reconocimientoEmocion("Hoy me siento muy feliz y lleno de energía.", "Juan", "usuarios.json"),
            "Emoción 'feliz' registrada para el usuario 'Juan'.",
            "Debería registrar correctamente la emoción 'feliz'."
        )

     def testReconocimientoEmocionSorpresa(self):
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)
        self.assertEqual(
            reconocimientoEmocion("¡Estoy sorprendido de lo que sucedió!", "Juan", "usuarios.json"),
            "Emoción 'sorprendido' registrada para el usuario 'Juan'.",
            "Debería registrar correctamente la emoción 'sorprendido'."
        )

     def testReconocimientoEmocionNeutral(self):
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)
        self.assertEqual(
            reconocimientoEmocion("Hoy me siento neutral, ni bien ni mal.", "Juan", "usuarios.json"),
            "Emoción 'neutral' registrada para el usuario 'Juan'.",
            "Debería registrar correctamente la emoción 'neutral'."
        )

     def testReconocimientoSinEmocionEnFrase(self):
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)
        self.assertEqual(
            reconocimientoEmocion("El sol brilla y el cielo está claro.", "Juan", "usuarios.json"),
            "No se encontraron emociones válidas en el texto.",
            "Debería devolver un mensaje indicando que no se detectaron emociones."
        )

     def testReconocimientoEmocionCombinada(self):
        with open("usuarios.json", "w") as file:
            json.dump({"Juan": {"emociones": []}}, file, indent=4)
        self.assertEqual(
            reconocimientoEmocion("Estoy feliz porque todo salió bien, pero también un poco sorprendido por lo que sucedió.", "Juan", "usuarios.json"),
            "Emoción 'feliz' registrada para el usuario 'Juan'.\nEmoción 'sorprendido' registrada para el usuario 'Juan'.",
            "Debería registrar ambas emociones 'feliz' y 'sorprendido'."
        )   


#Test creados por Javi
class testEliminarUsuario(unittest.TestCase):
    def testEliminarUsuarioExistente(self):
        # Prepara el archivo con usuarios
        with open("usuarios.json", "w") as file:
            json.dump(["Carlos", "Ana"], file, indent=4)
        
        self.assertEqual(
            eliminarUsuario("Carlos"),
            "Usuario 'Carlos' eliminado correctamente.",
            "Debería eliminar un usuario existente."
        )

    def testEliminarUsuarioInexistente(self):
        # Prepara el archivo con usuarios
        with open("usuarios.json", "w") as file:
            json.dump(["Carlos", "Ana"], file, indent=4)
        
        self.assertEqual(
            eliminarUsuario("Pedro"),
            "Error: El usuario 'Pedro' no existe en la base de datos.",
            "Debería devolver error si el usuario no existe."
        )

    def testBaseDatosInexistente(self):
        # Asegura que el archivo no exista
        if os.path.exists("usuarios.json"):
            os.remove("usuarios.json")
        
        self.assertEqual(
            eliminarUsuario("Carlos"),
            "Error: La base de datos no existe.",
            "Debería manejar la falta de un archivo correctamente."
        )

    def testBaseDatosCorrupta(self):
        # Prepara un archivo corrupto
        with open("usuarios.json", "w") as file:
            file.write("Contenido inválido")
        
        self.assertEqual(
            eliminarUsuario("Carlos"),
            "Error: El archivo de la base de datos está corrupto o vacío.",
            "Debería manejar un archivo corrupto correctamente."
        )

    def testEliminarUltimoUsuario(self):
        # Prepara el archivo con un solo usuario
        with open("usuarios.json", "w") as file:
            json.dump(["Carlos"], file, indent=4)
        
        self.assertEqual(
            eliminarUsuario("Carlos"),
            "Usuario 'Carlos' eliminado correctamente.",
            "Debería eliminar el último usuario correctamente."
        )

        with open("usuarios.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [], "La base de datos debería estar vacía después de eliminar el último usuario.")

# Test cases for generate_personalised created by Lukas
class TestGeneratePersonalisedResponse(unittest.TestCase):

    # Case 1: Test for file path error
    def test_file_path_error(self):
        self.assertEqual(generate_personalised_response("Max", "no_file.json"), "Error: The database does not exist.")

    # Case 2: Test load the database error
    def test_load_database_error(self):
        # Create an empty test file
        with open("empty_test.json", "w") as f:
            pass  # Leave the file empty to simulate an empty JSON
        self.assertEqual(generate_personalised_response("Max", "empty_test.json"), "Error: The database file is corrupted or empty.")
        os.remove("empty_test.json")  # Clean up the temporary file
    
    # Case 3: Test user does not exist in database
    def test_user_does_not_exist(self):
      # Create a temporary user file
      with open("temp_users.json", "w") as f:
          json.dump({}, f)  # Create an empty database
      self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Error: The user 'Max' does not exist in the database.")
      os.remove("temp_users.json") # Clean up the temporary file

    # Case 4: Test get the user's emotional history with no history saved
    def test_get_user_emotional_history(self):
      # Create a temporary user file
      with open("temp_users.json", "w") as f:
          json.dump({
              "Max": {
                  "age": 30,
                  "important_data": "" }
              }, 
          f)  # Pass 'f' as the file pointer
      self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Hello Max, it seems I don't have enough information about your emotions to personalize my response.")
      os.remove("temp_users.json") # Clean up the temporary file

    # Case 5: Test generate a personalised response for a predetermined user
    def test_generate_personalised_response(self):
      # Create a temporary user file
      with open("temp_users.json", "w") as f:
          json.dump({
              "Max": {
                  "age": 30,
                  "important_data": "Prefers coffee over tea",
                  "emotions": ["happy", "sad", "happy"]
              },
              "Anna": {
                  "age": 25,
                  "important_data": "Enjoys classical music",
                  "emotions": ["neutral", "neutral", "surprised"]
              }
          }, f)  # Pass 'f' as the file pointer
      self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Hello Max! I'm glad to see you're feeling happy. How can I assist you today?")
      self.assertEqual(generate_personalised_response("Anna", "temp_users.json"), "Hello Anna, I hope you're having a good day. How can I help you?")
      os.remove("temp_users.json") # Clean up the temporary file

  # 5 Additional tests created by AI (ChatGPT)
        # Case 6: Test for invalid JSON format in the database file
    def test_invalid_json_format(self):
        with open("invalid_test.json", "w") as f:
            f.write("{invalid_json}")  # Write an invalid JSON string
        self.assertEqual(generate_personalised_response("Max", "invalid_test.json"), "Error: The database file is corrupted or empty.")
        os.remove("invalid_test.json")  # Clean up the temporary file
    
    # Case 7: Test for a user with no emotions recorded
    def test_user_with_no_emotions(self):
        with open("temp_users.json", "w") as f:
            json.dump({
                "Max": {
                    "age": 30,
                    "important_data": "Prefers coffee over tea",
                    "emotions": []
                }
            }, f)
        self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Hello Max, it seems I don't have enough information about your emotions to personalize my response.")
        os.remove("temp_users.json")
    
    # Case 8: Test for a user with only neutral emotions
    def test_user_with_neutral_emotions(self):
        with open("temp_users.json", "w") as f:
            json.dump({
                "Max": {
                    "age": 30,
                    "important_data": "Enjoys hiking",
                    "emotions": ["neutral", "neutral", "neutral"]
                }
            }, f)
        self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Hello Max, I hope you're having a good day. How can I help you?")
        os.remove("temp_users.json")
    
    # Case 9: Test for a user with mixed emotions
    def test_user_with_mixed_emotions(self):
        with open("temp_users.json", "w") as f:
            json.dump({
                "Max": {
                    "age": 30,
                    "important_data": "Loves reading books",
                    "emotions": ["happy", "sad", "neutral", "happy"]
                }
            }, f)
        self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Hello Max! I'm glad to see you're feeling happy. How can I assist you today?")
        os.remove("temp_users.json")
    
    # Case 10: Test for a missing key in the user's data
    def test_user_with_missing_key(self):
        with open("temp_users.json", "w") as f:
            json.dump({
                "Max": {
                    "age": 30
                    # Missing "important_data" and "emotions" keys
                }
            }, f)
        self.assertEqual(generate_personalised_response("Max", "temp_users.json"), "Error: The user's data is incomplete in the database.")
        os.remove("temp_users.json")

if __name__ == "__main__":
     unittest.main()
