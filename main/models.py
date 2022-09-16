"""Modelo de dados do sistema."""
from django.db import models


# Create your models here.
class Player(models.Model):
    """
    Modelo de dados do jogador.
    """
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    ppg = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self) -> str:
        """
        Retorna o nome do jogador.
        """
        return str(self.name)
