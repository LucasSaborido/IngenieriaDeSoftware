import unittest
import json
import os
from Funciones import crearUsuario
from Funciones import accederPerfil

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

if __name__ == "__main__":
     unittest.main()
