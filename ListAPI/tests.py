from rest_framework.test import APITestCase
from rest_framework import status

class UserTests(APITestCase):

    def setUp(self):
        # Configura un usuario de prueba
        self.user = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123"
        }
        # Registra al usuario
        self.client.post('/register/', self.user)
        # Inicia sesión para obtener el token
        response = self.client.post('/login/', {
            "email": self.user["email"],
            "password": self.user["password"]
        })
        self.token = response.data['token']

    def test_create_todo_item(self):
        # Usa el token para autenticar la solicitud
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        # Datos del nuevo todo item
        data = {
            "title": "Buy groceries",
            "description": "Buy milk, eggs, and bread"
        }
        
        # Realiza la solicitud para crear un nuevo todo item
        response = self.client.post('/todos/', data)
        
        # Verifica el código de estado
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
