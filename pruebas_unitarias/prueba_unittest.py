import unittest

from modulos_propios import modulo_prueba_unittest


class PruebaUnittest(unittest.TestCase):

    def test_modulo_prueba_unittest_funcion_suma_ok(self):
        """
        Le damos un valor esperado que se comparará con el retorno de la función,
        si coincide la prueba es exitosa.
        :return:
        """
        num1 = 1
        num2 = 2
        resultado = modulo_prueba_unittest.funcion_suma(num1, num2)
        self.assertEqual(resultado, 3)

    def test_modulo_prueba_unittest_funcion_suma_nok(self):
        """
        La funcion sirve, pero como le estamos dando un parámetro esperado diferente al que retorna,
        sale como error.
        :return:
        """
        num1 = 1
        num2 = 2
        resultado = modulo_prueba_unittest.funcion_suma(num1, num2)
        self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
    # También pueden ejecutarse pruebas individuales.
    # PruebaUnittest().test_modulo_prueba_unittest_funcion_suma_ok()


