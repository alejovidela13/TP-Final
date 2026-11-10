from django.test import TestCase
from .utils import calcular_emisiones_carbono

class TestCalculoEmisiones(TestCase):
    
    def test_calculo_nominal(self):
        """Valida la exactitud numérica con factor de emisión por defecto (0.4)."""
        resultado = calcular_emisiones_carbono(1000)
        self.assertEqual(resultado, 400.0)

    def test_calculo_factor_personalizado(self):
        """Valida el cálculo modificando el factor de emisión."""
        resultado = calcular_emisiones_carbono(500, factor_emision=0.5)
        self.assertEqual(resultado, 250.0)

    def test_consumo_negativo_eleva_excepcion(self):
        """Verifica que un consumo negativo levante un ValueError."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-150)