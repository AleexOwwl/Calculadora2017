# !/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from Calculadora import Calculadora


class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_es_igual_a_cero(self):
        self.assertEquals(self.calc.obtener_resultado(), 0)

# Sumas

    def test_sumar_2_mas_2_igual_4(self):
        self.assertEquals(self.calc.suma(2, 2), 4)

    def test_sumar_3_mas_3_igual_6(self):
        self.assertEquals(self.calc.suma(3, 3), 6)

    def test_sumar_menos1_mas_2_igual_1(self):
        self.assertEquals(self.calc.suma(-1, 2), 1)

    def test_sumar_L_mas_2_igual_DatosIncorrectos(self):
        self.assertEquals(self.calc.suma('L', 2), 'Datos incorrectos')

    def test_sumar_0_mas_2_igual_NoSeAceptanCeros(self):
        self.assertEquals(self.calc.suma(0, 2), 'No se aceptan ceros')

    def test_sumar_10001_mas_5_igual_NoSeAceptanNumerosMayoresA10000(self):
        self.assertEquals(self.calc.suma(10001, 5), 'No acepta mayores 10000')

# Restas

    def test_restar_2_menos_2_igual_0(self):
        self.assertEquals(self.calc.resta(2, 2), 0)

    def test_restar_4_menos_3_igual_1(self):
        self.assertEquals(self.calc.resta(4, 3), 1)

    def test_restar_menos1_menos_2_igual_menos3(self):
        self.assertEquals(self.calc.resta(-1, 2), -3)

    def test_restar_L_menos_2_igual_DatosIncorrectos(self):
        self.assertEquals(self.calc.resta('L', 2), 'Datos incorrectos')

    def test_restar_0_menos_2_igual_NoSeAceptanCeros(self):
        self.assertEquals(self.calc.resta(0, 2), 'No se aceptan ceros')

    def test_restar_10001_menos_5_igual_NoSeAceptanNumerosMayoresA10000(self):
        self.assertEquals(self.calc.resta(10001, 5), 'No acepta mayores 10000')

# Multiplicaciones

    def test_multiplicar_2_por_8_igual_16(self):
        self.assertEquals(self.calc.multiplicacion(2, 8), 16)

    def test_multiplicar_4_por_5_igual_20(self):
        self.assertEquals(self.calc.multiplicacion(4, 5), 20)

    def test_multiplicar_menos2_por_9_igual_menos18(self):
        self.assertEquals(self.calc.multiplicacion(-2, 9), -18)

# Division

    def test_dividir_8_entre_2_igual_4(self):
        self.assertEquals(self.calc.division(8, 2), 4)

    def test_dividir_24_entre_4_igual_6(self):
        self.assertEquals(self.calc.division(24, 4), 6)

    def test_dividir_88_entre_8_igual_11(self):
        self.assertEquals(self.calc.division(88, 8), 11)

# Potencia

    def test_potenciaDe_4_aLa_4_igual_256(self):
        self.assertEquals(self.calc.potencia(4, 4), 256)

    def test_potenciaDe_10_aLa_2_igual_100(self):
        self.assertEquals(self.calc.potencia(10, 2), 100)

    def test_potenciaDe_8_aLa_4_igual_4096(self):
        self.assertEquals(self.calc.potencia(8, 4), 4096)

# Raiz

    def test_raizDe_9_igual_3(self):
        self.assertEquals(self.calc.raiz(9), 3)

    def test_raizDe_256_igual_16(self):
        self.assertEquals(self.calc.raiz(256), 16)

    def test_raizDe_2_igual_1(self):
        self.assertEquals(self.calc.raiz(2), 1)


if __name__ == '__main__':
    unittest.main()
