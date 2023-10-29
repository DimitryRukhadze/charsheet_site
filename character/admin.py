from django.contrib import admin

from .models import Race, Character


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass
