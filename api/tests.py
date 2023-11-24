from django.test import TestCase
from api.models import General
# Create your tests here.

class GeneralModelTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo General y realiza pruebas
        instancia = General(
            Id_general = 2,
            precios='precio1',
            empanadas='empanada1',
            cortes='corte1',
            guarniciones='guarnicion1',
            postres='postre1',
            salsapastas='salsapasta1',
            alcohol='alcohol1',
            cervezas='cerveza1',
            refrescos='refresco1',
            cafes='cafe1'
        )

        # Verifica cada campo individualmente
        self.assertEqual(instancia.Id_general, 2)
        self.assertEqual(instancia.precios, 'precio1')
        self.assertEqual(instancia.empanadas, 'empanada1')
        self.assertEqual(instancia.cortes, 'corte1')
        self.assertEqual(instancia.guarniciones, 'guarnicion1')
        self.assertEqual(instancia.postres, 'postre1')
        self.assertEqual(instancia.salsapastas, 'salsapasta1')
        self.assertEqual(instancia.alcohol, 'alcohol1')
        self.assertEqual(instancia.cervezas, 'cerveza1')
        self.assertEqual(instancia.refrescos, 'refresco1')
        self.assertEqual(instancia.cafes, 'cafe1')