from django.contrib import admin

from .models import Race, Character, Theme


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass