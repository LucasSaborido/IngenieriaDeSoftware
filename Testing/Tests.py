import unittest
import json
from Funciones import crearUsuario

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

if __name__ == "__main__":
     unittest.main()
