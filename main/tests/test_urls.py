"""Realiza testes sobre as URLs do projeto."""
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient

class UrlTest(TenantTestCase):
    """
    Testes sobre a URL do sistema.
    """
    def setUp(self):
        self.client = TenantClient(self.tenant)
        print(f'Criado tenant: {self.client.tenant}')
        super().setUp()

    def test_home_page(self) -> None:
        """
        Testa a página inicial do sistema.
        """
        response = self.client.get('/')
        print(response)

        self.assertEqual(response.status_code, 200)
