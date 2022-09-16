"""Testes para o modelo de dados do sistema."""
from django.test import TestCase

from ..models import Player


class ModelTest(TestCase):
    """
    Testes para o modelo Player
    """

    def test_product_model(self):
        """
        Testa a criação de um novo jogador.
        """
        player = Player.objects.create(name="Maxwell", height=72, team='RPG', ppg=1.63)
        self.assertEqual(str(player), 'Maxwell')
        print("IsInstance : ", isinstance(player, Player))
        self.assertTrue(isinstance(player, Player))
