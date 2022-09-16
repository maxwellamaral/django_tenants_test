from django.contrib import admin

from main.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
