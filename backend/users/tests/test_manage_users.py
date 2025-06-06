import os
import django
import unittest
from django.test import Client
from django.contrib.auth.models import Group
from users.models import CustomUser
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.app.settings")
django.setup()


class ManageUsersEndpointTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Client()
        cls.admin_group, _ = Group.objects.get_or_create(name="admin") 
        cls.admin_user = CustomUser.objects.create_user(
            username="test_manage_admin", password="admin123"
        )
        cls.admin_user.groups.add(cls.admin_group)
        cls.normal_user = CustomUser.objects.create_user(
            username="test_manage_user", password="user123"
        )

    @classmethod
    def tearDownClass(cls):
        cls.admin_user.delete()
        cls.normal_user.delete()
        cls.admin_group.delete()

    def test_manage_users_as_admin(self):
        self.client.login(username="test_manage_admin", password="admin123")
        response = self.client.get(reverse("manage_users"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Usuarios", response.content.decode())

    def test_manage_users_as_non_admin(self):
        self.client.login(username="test_manage_user", password="user123")
        response = self.client.get(reverse("manage_users"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("dashboard"), response.url)
