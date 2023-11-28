
import pytest
from api.models import General, RegistrarForm
# Create your tests here.


def test_crear_instancia():
        instancia = General.objects.create_user (
            Id_genera='A'
            precios='precio1',
            empanadas='empanada1',
            cortes='corte1',
            guarniciones='guarnicion1',
            postres='postre1',
            salsapastas='salsapasta1',
            alcohol='alcohol1',
            cervezas='cerveza1',
            refrescos='refresco1',
            cafes='cafe1',
        )

        # Verifica cada campo individualmente 
        assert instancia.Id_genera == 'A'
        assert instancia.precios == 'precio1'
        
        
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
        