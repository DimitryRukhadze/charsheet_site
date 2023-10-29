from django.db import models
from django.contrib.auth.models import AbstractUser


class Race(models.Model):
    str_mod = models.IntegerField('Модификатор силы', default=0)
    agi_mod = models.IntegerField('Модификатор ловкости', default=0)
    end_mod = models.IntegerField('Модификатор выносливости', default=0)
    int_mod = models.IntegerField('Модификатор интеллекта', default=0)
    wis_mod = models.IntegerField('Модификатор мудрости', default=0)
    cha_mod = models.IntegerField('Модификатор обаяния', default=0)
    race_health_points = models.IntegerField('ПЗ расы', default=0)


class Character(models.Model):
    owner = models.ForeignKey('User', verbose_name='Игрок', on_delete=models.SET_NULL)
    name = models.CharField('Имя', max_length=30)
    race = models.ForeignKey(
        'Race',
        verbose_name='Раса',
        related_name='character',
        on_delete=models.SET_NULL
    )
    strength = models.IntegerField('Сила', default=10)
    agility = models.IntegerField('Ловкость', default=10)
    endurance = models.IntegerField('Выносливость', default=10)
    intelligence = models.IntegerField('Интеллект', default=10)
    wisdom = models.IntegerField('Мудрость', default=10)
    charisma = models.IntegerField('Обаяние', default=10)
