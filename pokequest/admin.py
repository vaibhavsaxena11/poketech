from django.contrib import admin

from .models import Player, Pokemon

class PokemonInline(admin.StackedInline):
    model = Pokemon

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Serial no.', {'fields': ['serialno']}),
        ('Player Name', {'fields': ['name']}),
        ('Present', {'fields': ['present']}),
        ('Counter', {'fields': ['counter']}),
        ('Points', {'fields':['points']}),
        ('Score', {'fields':['score']})
    ]
    inlines = [PokemonInline]
    

admin.site.register(Player, PlayerAdmin)