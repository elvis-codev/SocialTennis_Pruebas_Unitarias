
from django.test import TestCase
from django.db import connections
from django.db.utils import OperationalError
from django.contrib.auth.models import User
from django.urls import reverse

class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        db_conn = connections['default']
        try:
            db_conn.cursor()
            connection_status = True
        except OperationalError:
            connection_status = False

        # Imprimir el mensaje basado en el estado de la conexión
        if connection_status:
            print("La conexión a la base de datos ha sido exitosa.")
        else:
            print("La conexión a la base de datos ha fallado.")

        self.assertTrue(connection_status, "La conexión a la base de datos ha fallado.")


class LoginTest(TestCase):
    def setUp(self):
        self.username = 'renato12'
        self.password = '1234'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_login_with_valid_credentials(self):
        # Intenta autenticar al usuario con las credenciales correctas
        login_successful = self.client.login(username=self.username, password=self.password)
        
        # Imprimir el mensaje basado en el resultado del login
        if login_successful:
            print("Login exitoso con credenciales válidas.")
        else:
            print("Login fallido con credenciales válidas.")
        
        # Verificar que el login fue exitoso
        self.assertTrue(login_successful, "El login con credenciales válidas ha fallado.")
        
        # Verificar que el usuario está autenticado
        response = self.client.get(reverse('home'))  # Asegúrate de que 'home' sea el nombre de una vista válida
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)




        