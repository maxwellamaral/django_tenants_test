"""Testes para o modelo de dados do sistema."""
import pytest

from django.contrib.auth.models import User, Group
from django.urls import reverse
from django_tenants.test.cases import TenantTestCase
from django_tenants.test.client import TenantClient

from ..models import Player


class ModelTest(TenantTestCase):
    """
    Testes para o modelo Player
    """

    def setUp(self):
        self.client = TenantClient(self.tenant)
        print(f'Criado tenant: {self.client.tenant}')
        super(ModelTest, self).setUp()

    def test_player_model(self):
        """
        Testa a criação de um novo jogador.
        """
        player = Player.objects.create(name="Maxwell", height=72, team='RPG', ppg=1.63)
        self.assertEqual(str(player), 'Maxwell')
        print("IsInstance : ", isinstance(player, Player))
        self.assertTrue(isinstance(player, Player))
