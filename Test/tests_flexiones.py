import unittest
from test_maquina_de_flexiones import MaquinaDeFlexiones  # Asumimos que este es el nombre del archivo donde está la clase

class TestMaquinaDeFlexiones(unittest.TestCase):
    
    def setUp(self):
        self.maquina = MaquinaDeFlexiones()

    def test_iniciar_sesion(self):
        """Verifica el comportamiento al iniciar una sesión nueva."""
        self.maquina.iniciar_sesion()
        self.assertTrue(self.maquina.sesion_activa)
        self.assertEqual(self.maquina.contador_actual, 0)
        self.assertEqual(self.maquina.contador_sesiones, 1)

    def test_iniciar_sesion_dos_veces(self):
        """Verifica que se lanza un error al intentar iniciar una sesión ya activa."""
        self.maquina.iniciar_sesion()
        with self.assertRaises(RuntimeError, msg="Se esperaba un error al intentar iniciar una sesión ya activa"):
            self.maquina.iniciar_sesion()

    def test_finalizar_sesion(self):
        """Verifica que se pueda finalizar una sesión activa."""
        self.maquina.iniciar_sesion()
        self.maquina.finalizar_sesion()
        self.assertFalse(self.maquina.sesion_activa)

    def test_finalizar_sesion_sin_iniciar(self):
        """Verifica que se lanza un error al intentar finalizar una sesión sin que esté activa."""
        with self.assertRaises(RuntimeError, msg="Se esperaba un error al intentar finalizar una sesión sin que esté activa"):
            self.maquina.finalizar_sesion()

    def test_agregar_flexion(self):
        """Verifica que el contador de flexiones aumente correctamente."""
        self.maquina.iniciar_sesion()
        self.maquina.agregar_flexion()
        self.assertEqual(self.maquina.contador_actual, 1)

    def test_agregar_flexion_sin_sesion(self):
        """Verifica que se lanza un error al intentar agregar una flexión sin una sesión activa."""
        with self.assertRaises(RuntimeError, msg="Se esperaba un error al intentar agregar una flexión sin una sesión activa"):
            self.maquina.agregar_flexion()

    def test_establecer_objetivo(self):
        """Verifica que se pueda establecer un objetivo válido."""
        self.maquina.establecer_objetivo(10)
        self.assertEqual(self.maquina.contador_objetivo, 10)

    def test_establecer_objetivo_invalido(self):
        """Verifica que se lanza un error al establecer un objetivo no válido."""
        with self.assertRaises(ValueError, msg="Se esperaba un error al establecer un objetivo menor o igual a 0"):
            self.maquina.establecer_objetivo(-5)
        with self.assertRaises(ValueError, msg="Se esperaba un error al establecer un objetivo no entero"):
            self.maquina.establecer_objetivo("diez")

    def test_verificar_objetivo(self):
        """Verifica que se alcance el objetivo correctamente."""
        self.maquina.iniciar_sesion()
        self.maquina.establecer_objetivo(5)
        for _ in range(5):
            self.maquina.agregar_flexion()
        self.assertTrue(self.maquina.verificar_objetivo())

    def test_progreso_actual(self):
        """Verifica que el progreso se calcule correctamente."""
        self.maquina.iniciar_sesion()
        self.maquina.establecer_objetivo(10)
        for _ in range(5):
            self.maquina.agregar_flexion()
        self.assertAlmostEqual(self.maquina.progreso_actual(), 50.0)

    def test_reiniciar_sesion(self):
        """Verifica que el contador de flexiones se reinicie correctamente."""
        self.maquina.iniciar_sesion()
        self.maquina.establecer_objetivo(10)
        self.maquina.agregar_flexion()
        self.maquina.reiniciar_sesion()
        self.assertEqual(self.maquina.contador_actual, 0)
    
    def test_str(self):
        """Verifica la representación en cadena del objeto MaquinaDeFlexiones."""
        self.maquina.iniciar_sesion()
        self.maquina.establecer_objetivo(5)
        self.maquina.agregar_flexion()
        expected_str = ("Flexiones en la Sesión Actual: 1\n"
                        "Flexiones Objetivo: 5\n"
                        "Progreso: No Alcanzado\n"
                        "Porcentaje de Progreso: 20.00%")
        self.assertEqual(str(self.maquina), expected_str)


if __name__ == '__main__':
    unittest.main()
