from django.test import TestCase
from api.models import General, RegistrarForm
# Create your tests here.

class GeneralModelTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo General y realiza pruebas
        instancia = General(
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
        
        
class Registra_usuaTests(TestCase):
    def test_crear_instancia(self):
        # Crea una instancia del modelo General y realiza pruebas
        instancia = RegistrarForm(
            nombre_us='Alfonso',
            apellidos_us='Maldonado',
            correo_us='corte@gmail.com',
            contraseña='12345*A',
            rep_contra='12345*A'
        )
    
        # Verifica cada campo individualmente
        self.assertEqual(instancia.nombre_us,'Alfonso')
        self.assertEqual(instancia.apellidos_us,'Maldonado')
        self.assertEqual(instancia.correo_us,'corte@gmail.com')
        self.assertEqual(instancia.contraseña,'12345*A')
        self.assertEqual(instancia.rep_contra,'12345*A')
        