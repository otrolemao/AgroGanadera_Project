from django.contrib import admin
from .models import Raza, Ternero

@admin.register(Raza)
class RazaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Ternero)
class TerneroAdmin(admin.ModelAdmin):
    list_display = ('numero_identificador', 'raza', 'peso_kg', 'disponible_venta')
    list_filter = ('raza', 'disponible_venta')
    search_fields = ('numero_identificador',)