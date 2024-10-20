from django.db import models


class Unit(models.TextChoices):
    KILOGRAM: tuple = 'KG', 'kilogram'
    PIECE: tuple = 'PC', 'piece'
