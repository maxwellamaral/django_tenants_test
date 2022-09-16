"""Realiza testes sobre as URLs do projeto."""
from django.test import TestCase


class UrlTest(TestCase):
    """
    Testes sobre a URL do sistema.
    """

    def test_home_page(self) -> None:
        """
        Testa a página inicial do sistema.
        """
        response = self.client.get('/')
        print(response)

        self.assertEqual(response.status_code, 200)
