import os
import django
import unittest
from django.test import Client
from users.models import CustomUser
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.app.settings")
django.setup()


class LoginEndpointTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.user = CustomUser.objects.create_user(
            username="test_login_admin", password="admin123"
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_login_successful(self):
        response = self.client.post(
            reverse("login"), {"username": "test_login_admin", "password": "admin123"}
        )
        self.assertEqual(response.status_code, 302)

    def test_login_invalid_password(self):
        response = self.client.post(
            reverse("login"), {"username": "test_login_admin", "password": "wrongpass"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Por favor introduzca un nombre de usuario y una contraseña correctos",
            response.content.decode(),
        )
